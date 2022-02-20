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

	public $tbl_cells, $tbl_tags, $tbl_ids_ct;
	

	function clear_str($str){
		$str = trim(strip_tags($str));
		return mysqli_real_escape_string($this->link, $str);
	}
	function match_tag_name($tag){
		$tag = $this->clear_str($tag);
		$sql = "SELECT * FROM $this->tbl_tags WHERE name = '$tag'";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return mysqli_fetch_array($response, MYSQLI_ASSOC);
		}else{
			return false;	
		}
	}
	function give_cells($id){
		$ids_array = explode(",", $id);
		$sql = "SELECT * FROM $this->tbl_cells WHERE id IN ('$id')";
		$result = mysqli_query($this->link, $sql);
		if($result){
			if(count($ids_array) == 1)
				return mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				return mysqli_fetch_all($result, MYSQLI_ASSOC);
		}else {
			printf("give_cells %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function give_tags($ids){
		$ids_arr = explode(",", $ids);
		
		if(strlen($ids_arr[0]) == 0)
			return;
		$sql = "SELECT * FROM $this->tbl_tags WHERE id IN ($ids)";
		$result = mysqli_query($this->link, $sql);
		if($result){
			//print_r(mysqli_fetch_array($result, MYSQLI_ASSOC));
			return mysqli_fetch_all($result, MYSQLI_ASSOC);
		}else {
			printf("give_tags %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function give_table($table){
		$sql = "SELECT * FROM $table";
		$result = mysqli_query($this->link, $sql);	
		if($result){
			return mysqli_fetch_all($result, MYSQLI_ASSOC);
		}else {
			printf("give_table %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function give_cell_tags($cell_id){
		$sql = 
			"SELECT * FROM $this->tbl_tags WHERE id IN ".
			"(SELECT tag_id FROM $this->tbl_ids_ct WHERE cell_id = $cell_id)";
		$response = mysqli_query($this->link, $sql);
		if($response)
			return mysqli_fetch_all($response, MYSQLI_ASSOC);
		else
			printf("%s\n", mysqli_error($this->link));
	}
	function remove_cell($id){
		$id = $this->clear_str($id);
		$sql = "DELETE FROM $this->tbl_cells WHERE id = $id";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return true;
		}else{
			printf("remove_cell %s\n", mysqli_error($this->link));
			return false;
		}
	}
	function add_ids_ct($cell_id, $tag_id){
		$sql = "INSERT INTO $this->tbl_ids_ct (cell_id, tag_id) VALUES ('$cell_id', '$tag_id')";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return true;
		}else{
			printf("%s\n", mysqli_error($this->link));
		}
	}
	function add_tag($tag){
		$tag = $this->clear_str($tag);
		$sql = "INSERT INTO $this->tbl_tags (name) VALUES ('$tag')";
		$response = mysqli_query($this->link, $sql);
		if($response){
			return $this->give_tags(mysqli_insert_id($this->link))[0];
		}else{
			printf("Тег не добавлен %s\n", mysqli_error($this->link));
		}
	}
	function add_cell($description, $tags){
		//print_r($tags_ids);
		$sql = "INSERT INTO $this->tbl_cells (description) VALUES ('$description')";
		$response = mysqli_query($this->link, $sql);
		if($response){
			// Получить последний добавленный id
			$cell_id = mysqli_insert_id($this->link);

			// Добавление тегов
			if(count($tags)){
				for ($i=0; $i < count($tags); $i++) { 
					$tag = $this->match_tag_name($tags[$i]);
					if(!$tag)
						$tag = $this->add_tag($tags[$i]);
					$this->add_ids_ct($cell_id, $tag['id']);
				}
			}

			$cell = $this->give_cells($cell_id);			
			$cell['tags'] = $this->give_cell_tags($cell_id);

			if($cell){
				return array(
					'status' => true,
					'cell' => $cell
				);
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
$lib->tbl_cells = "cells";
$lib->tbl_tags = "tags";
$lib->tbl_ids_ct = "ids_cells_tags";

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
	$cells = $lib->give_table($lib->tbl_cells);
	for ($i=0; $i < count($cells); $i++) {
		$cells[$i]['tags'] = $lib->give_cell_tags($cells[$i]['id']);
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
//$asd = explode(",", ",23");
//print_r(strlen($asd[0]));
// $sql = "SELECT * FROM cells WHERE tags REGEXP '^12$'";

// $result = mysqli_query($link, $sql);

// // mysqli_close($link);
// // // Обрабатываем результат
//  $row = mysqli_fetch_all($result, MYSQLI_ASSOC);
//  $row = json_encode($row);

// echo $row;