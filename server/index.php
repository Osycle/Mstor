<?
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization, Access-Control-Allow-Methods, Access-Control-Request-Headers');


const DB_HOST = "localhost";
const DB_LOGIN = "root";
const DB_PASSWORD = "";
const DB_NAME = "test_mstor";



$link = mysqli_connect(DB_HOST, DB_LOGIN, DB_PASSWORD, DB_NAME) or die(mysqli_connect_error());

class Lib{
	public $link;
	public $tbl_name_cells = "cells";
	public $tbl_name_tags = "tags";

	function clear_str($str){
		$str = trim(strip_tags($str));
		return mysqli_real_escape_string($this->link, $str);
	}
	function match_tag_name($tag){
		$sql = "SELECT * FROM $this->tbl_name_tags WHERE name = '$tag'";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return mysqli_fetch_array($response, MYSQLI_ASSOC);
		}else{
			return false;	
		}
	}
	function give_cell_id($id){
		$ids_array = explode(",", $id);
		$sql = "SELECT * FROM $this->tbl_name_cells WHERE id IN ('$id')";
		$result = mysqli_query($this->link, $sql);
		if($result){
			if(count($ids_array) == 1)
				return mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				return mysqli_fetch_all($result, MYSQLI_ASSOC);
		}else {
			printf("give_cell_id %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function give_tag_id($id){
		if(!$id)
			return;
		$ids_array = explode(",", $id);
		$sql = "SELECT * FROM $this->tbl_name_tags WHERE id IN ($id)";
		$result = mysqli_query($this->link, $sql);
		if($result){
			if(count($ids_array) == 1)
				return mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				return mysqli_fetch_all($result, MYSQLI_ASSOC);
		}else {
			printf("give_tag_id %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function give_table($table, $array = false){
		$sql = "SELECT * FROM $table";
		$result = mysqli_query($this->link, $sql);	
		if($result){
			if($array)
				return mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				return mysqli_fetch_all($result, MYSQLI_ASSOC);
		}else {
			printf("give_table %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function remove_cell($id){
		$id = $this->clear_str($id);
		$sql = "DELETE FROM $this->tbl_name_cells WHERE id = $id";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return true;
		}else{
			printf("remove_cell %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function add_tag($tag){
		$tag = $this->clear_str($tag);
		$sql = "INSERT INTO $this->tbl_name_tags (name) VALUES ('$tag')";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return $this->give_tag_id(mysqli_insert_id($this->link));
		}else{
			printf("Ошибка тег не добавлен %s\n", mysqli_error($this->link));
		}
	}
	function add_cell($description, $tags){
		//$tags_ids = [];
		$f_tags = [];
		//if($tags){
		for ($i=0; $i < count($tags); $i++) { 
				$current_tag = $this->match_tag_name($tags[$i]);
			if($current_tag){
				$f_tags[] = $current_tag;
			}else{
				$f_tags[] = $this->add_tag($tags[$i]);
			}
		}
		for ($i=0; $i < count($f_tags); $i++) { 
			$tags_ids[] = $f_tags[$i]['id'];
		}
		$tags_ids = implode(",", $tags_ids);
		//}

		$sql = "INSERT INTO $this->tbl_name_cells (description, tags_ids) VALUES ('$description', '$tags_ids')";
		$response = mysqli_query($this->link, $sql);
		if($response){
			// Получить последний добавленный элемент
			$cell = $this->give_cell_id(mysqli_insert_id($this->link));
			$cell['tags'] = $this->give_tag_id($cell['tags_ids']);
			if($cell){
				$arr = array(
					'status' => $response,
					'cell' => $cell
				);
				return $arr;
			}else {
				printf("Ошибка при возвращении поледнего добавленного  %s\n", mysqli_error($this->link));
			}
		}else {
			printf("Ошибка при добавлении  %s\n", mysqli_error($this->link));
			//echo 'Ошибка при добавлении \n'.$response;
		}
	}
}

$lib = new Lib();
$lib->link = $link;

/* 
	Основные настроики 
*/



/* 
	Сохранение записи в БД 
*/

$json = file_get_contents('php://input');
$arr = json_decode($json, true);




if($arr["action"] === "insert"){
	$params = $arr["params"];
	$description = $lib->clear_str($params["description"]);
	$tags = $params["tags"];

	//print_r($tags);
	die(json_encode($lib->add_cell($description, $tags)));
}
if($arr["action"] === "delete"){
	$params = $arr["params"];
	$result = $lib->remove_cell($params["id"]);
	echo json_encode(array(
		'status' => $result
	));
}
if($arr["action"] === "fetch"){
	$cells = $lib->give_table($lib->tbl_name_cells);
	for ($i=0; $i < count($cells); $i++) { 		
		if(!count($cells[$i]['tags_ids']))
			return;
		$cells[$i]['tags'] = $lib->give_tag_id($cells[$i]['tags_ids']);
	}
	if($cells){
		echo json_encode(array(
			'status' => true,
			'cells' => $cells
		));
	}else {
		printf("Ошибка в fetch");
	}

}

// $sql = "SELECT * FROM cells WHERE tags REGEXP '^12$'";

// $result = mysqli_query($link, $sql);

// // mysqli_close($link);
// // // Обрабатываем результат
//  $row = mysqli_fetch_all($result, MYSQLI_ASSOC);
//  $row = json_encode($row);

// echo $row;