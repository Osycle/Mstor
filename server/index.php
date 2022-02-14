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

	public $tbl_name_cells = "cells";
	public $tbl_name_tags = "tags";

	function clear_str($str){
		global $link;
		$str = trim(strip_tags($str));
		return mysqli_real_escape_string($link, $str);
	}
	function tag_add($tag){
		global $link;
		$tag = $this->clear_str($tag);
		$sql = "INSERT INTO $this->tbl_name_tags (name) VALUES ('$tag')";
		$response = mysqli_query($link, $sql);
		if($response){
			return $this->give_tag_id(mysqli_insert_id($link), true);
		}else{
			printf("Ошибка тег не добавлен %s\n", mysqli_error($link));
		}
	}
	function tag_match_name($tag){
		global $link;
		$sql = "SELECT * FROM $this->tbl_name_tags WHERE name = '$tag'";
		$response = mysqli_query($link, $sql);
		if($response){
			return mysqli_fetch_array($response, MYSQLI_ASSOC);
		}else{
			return false;	
		}
	}
	function give_id($table, $id){
		global $link;
		$sql = "SELECT * FROM $table ";
		if($id){
			$sql .= "WHERE id=$id";
		}
		$result = mysqli_query($link, $sql);
		if($result){
			if($array)
				$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				$row = mysqli_fetch_all($result, MYSQLI_ASSOC);
			return $row;
		}else {
			return $result;
		}
	}
	function give_cell_id($id, $array = false){
		global $link;
		$sql = "SELECT * FROM $this->tbl_name_cells WHERE id=$id";
		$result = mysqli_query($link, $sql);
		if($result){
			if($array)
				$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				$row = mysqli_fetch_all($result, MYSQLI_ASSOC);
			return $row;
		}else {
			return $result;
		}
	}
	function give_tag_id($id, $array = false){
		global $link;
		$sql = "SELECT * FROM $this->tbl_name_tag WHERE id=$id";
		$result = mysqli_query($link, $sql);
		if($result){
			if($array)
				$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
			else
				$row = mysqli_fetch_all($result, MYSQLI_ASSOC);
			return $row;
		}else {
			return $result;
		}
	}
	// function give_table($table, $array = false){
	// 	global $link, $tbl_name_cells, $tbl_name_tags;
	// 	$sql = "SELECT * FROM $table";
	// 	$result = mysqli_query($link, $sql);
	// 	if($result){
	// 		if($array)
	// 			$row = mysqli_fetch_array($result, MYSQLI_ASSOC);
	// 		else
	// 			$row = mysqli_fetch_all($result, MYSQLI_ASSOC);
	// 		return $row;
	// 	}else {
	// 		return $result;
	// 	}
	// }
}

$lib = new Lib();


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
	//$tags = json_encode($params["tags"]);
	$tags = [];
	for ($i=0; $i < count($params["tags"]); $i++) { 
		$current_tag = $lib->tag_match_name($params["tags"][$i]);
		if($current_tag){
			$tags[] = $current_tag;
		}else{
			$tags[] = $lib->tag_add($params["tags"][$i]);
		}
	}
	
	for ($i=0; $i < count($tags); $i++) { 
		$tags_ids[] = $tags[$i]['id'];
	}
	print_r($tags);
	$tags_ids = implode("|", $tags_ids);
	$sql = "INSERT INTO $lib->tbl_name_cells (description, tags) VALUES ('$description', '$tags_ids')";
	$response = mysqli_query($link, $sql);
	if($response){
		// Получить последний добавленный элемент
		$cell = $lib->give_cell_id(mysqli_insert_id($link));
		if($cell){
			$arr = array(
				'status' => $response,
				'cell' => $cell[0]
			);
			echo json_encode($arr);
		}else {
			printf("Ошибка при возвращении поледнего добавленного  %s\n", mysqli_error($link));
		}
	}else {
		printf("Ошибка при добавлении  %s\n", mysqli_error($link));
		//echo 'Ошибка при добавлении \n'.$response;
	}
}
if($arr["action"] === "delete"){
	$params = $arr["params"];
	$id = $lib->clear_str($params["id"]);
	$sql = "DELETE FROM $lib->tbl_name_cells WHERE id = '$id'";
	$res = mysqli_query($link, $sql);
	if($res){
		$arr = array('status' => $res);
		echo json_encode($arr);
	}
}
if($arr["action"] === "fetch"){
	$sql = "SELECT * FROM $lib->tbl_name_cells";
	$response = mysqli_query($link, $sql);
	$data = mysqli_fetch_all($response, MYSQLI_ASSOC);
	if($response){
		$arr = array(
			'status' => $response,
			'cells' => $data
		);
		echo json_encode($arr);
	}else {
		printf("Ошибка  %s\n", mysqli_error($link));
	}

}

// $sql = "SELECT * FROM cells WHERE tags REGEXP '^12$'";

// $result = mysqli_query($link, $sql);

// // mysqli_close($link);
// // // Обрабатываем результат
//  $row = mysqli_fetch_all($result, MYSQLI_ASSOC);
//  $row = json_encode($row);

// echo $row;