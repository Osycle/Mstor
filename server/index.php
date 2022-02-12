<?
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, PATCH, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization, Access-Control-Allow-Methods, Access-Control-Request-Headers');


const DB_HOST = "localhost";
const DB_LOGIN = "root";
const DB_PASSWORD = "";
const DB_NAME = "test_mstor";

$link = mysqli_connect(DB_HOST, DB_LOGIN, DB_PASSWORD, DB_NAME) or die(mysqli_connect_error());

/* 
	Основные настроики 
*/

function clear_str($str){
	global $link;
	$str = trim(strip_tags($str));
	return mysqli_real_escape_string($link, $str);
}

function giveId($id){
	global $link;
	$sql = "SELECT *FROM cells WHERE id =$id";
	$result = mysqli_query($link, $sql);
	//echo $sql;
	if($result){
		$row = mysqli_fetch_all($result, MYSQLI_ASSOC);
		return $row;
	}else {
		return $result;
	}
}

/* 
	Сохранение записи в БД 
*/

$json = file_get_contents('php://input');
$arr = json_decode($json, true);




if($arr["action"] === "insert"){
	$params = $arr["params"];
	$title = clear_str($params["title"]);
	$description = clear_str($params["description"]);
	$tags = json_encode($params["tags"]);
	for ($i=0; $i < count($params["tags"]); $i++) { 
		echo $params["tags"][$i];
	}
	var_dump($params["tags"]);	
	//print_r($tags);
	//$sql = "INSERT INTO tags (name) VALUES ('$tags')";
	//$response = mysqli_query($link, $sql);
	return;
	$sql = "INSERT INTO cells (title, description, tags) VALUES ('$title', '$description', '$tags')";
	$response = mysqli_query($link, $sql);
	//echo $response;
	if($response){
		// Получить последний добавленный элемент
		$cell = giveId(mysqli_insert_id($link));
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
	$sql = "DELETE FROM cells WHERE id = '$id'";
	$res = mysqli_query($link, $sql);
	if($res){
		$arr = array('status' => $res);
		echo json_encode($arr);
	}
}
if($arr["action"] === "fetch"){
	$sql = 'SELECT * FROM cells';
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