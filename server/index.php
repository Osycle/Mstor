<?
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization, Access-Control-Allow-Methods, Access-Control-Request-Headers');


const DB_HOST = "localhost";
const DB_LOGIN = "root";
const DB_PASSWORD = "";
const DB_NAME = "test_mstor";

$tbl_name_cells = "cells";
$tbl_name_tags = "tags";

$link = mysqli_connect(DB_HOST, DB_LOGIN, DB_PASSWORD, DB_NAME) or die(mysqli_connect_error());

/* 
	Основные настроики 
*/

function clear_str($str){
	global $link, $tbl_name_cells, $tbl_name_tags;
	$str = trim(strip_tags($str));
	return mysqli_real_escape_string($link, $str);
}

function give_id($id, $table, $array){
	global $link, $tbl_name_cells, $tbl_name_tags;
	$sql = "SELECT * FROM $table WHERE id = $id";
	$result = mysqli_query($link, $sql);
	//echo $sql;
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
function tag_add($tag){
	global $link, $tbl_name_tags;
	$sql = "INSERT INTO $tbl_name_tags (name) VALUES ('$tag')";
	$response = mysqli_query($link, $sql);
	if($response){
		return give_id(mysqli_insert_id($link), $tbl_name_tags, true);
	}else{
		return false;	
	}
}

function tag_match_name($tag){
	global $link, $tbl_name_tags;
	$sql = "SELECT * FROM $tbl_name_tags WHERE name = '$tag'";
	$response = mysqli_query($link, $sql);
	if($response){
		return mysqli_fetch_array($response, MYSQLI_ASSOC);
	}else{
		return false;	
	}
}


/* 
	Сохранение записи в БД 
*/

$json = file_get_contents('php://input');
$arr = json_decode($json, true);




if($arr["action"] === "insert"){
	$params = $arr["params"];
	$description = clear_str($params["description"]);
	//$tags = json_encode($params["tags"]);
	$tags = [];
	for ($i=0; $i < count($params["tags"]); $i++) { 
		//$tags[] = tag_add($params["tags"][$i]);
		$current_tag = tag_match_name($params["tags"][$i]);
		if($current_tag)
			$tags[] = $current_tag;
		else{
			$tags[] = tag_add($params["tags"][$i]);
		}
	}
	//$z = tag_add($tag);
	print_r($tags);
	//$tags = implode("|", $tags);
	return;
	//var_dump($tags);	
	//print_r($tags);
	//$sql = "INSERT INTO tags (name) VALUES ('$tags')";
	//$response = mysqli_query($link, $sql);
	//return;
	$sql = "INSERT INTO $tbl_name_cells (description, tags) VALUES ('$description', '$tags')";
	$response = mysqli_query($link, $sql);
	//echo $response;
	if($response){
		// Получить последний добавленный элемент
		$cell = give_id(mysqli_insert_id($link), $tbl_name_cells);
		//echo $cell.'asd';
		//mysqli_close($link);
		if($cell){
			$arr = array(
				'status' => $response,
				'cell' => $cell[0]
			);
			echo json_encode($arr);
		}else {
			echo 'Ошибка при возвращении поледнего добавленного \n'.$cell;	
		}
	}else {
		echo 'Ошибка при добавлении \n'.$response;
	}
}
if($arr["action"] === "delete"){
	$params = $arr["params"];
	$id = clear_str($params["id"]);
	$sql = "DELETE FROM $tbl_name_cells WHERE id = '$id'";
	$res = mysqli_query($link, $sql);
	if($res){
		$arr = array('status' => $res);
		echo json_encode($arr);
	}
}
if($arr["action"] === "fetch"){
	$sql = "SELECT * FROM $tbl_name_cells";
	$result = mysqli_query($link, $sql);
	mysqli_close($link);

	$row = mysqli_fetch_all($result, MYSQLI_ASSOC);
	$row = json_encode($row);
	echo $row;
}

// $sql = "SELECT * FROM cells WHERE tags REGEXP '^12$'";

// $result = mysqli_query($link, $sql);

// // mysqli_close($link);
// // // Обрабатываем результат
//  $row = mysqli_fetch_all($result, MYSQLI_ASSOC);
//  $row = json_encode($row);

// echo $row;