<?php
    $name = $_REQUEST["name"];
    $birth = $_REQUEST["birth"];
	$tel = $_REQUEST["tel"];
	
	if ($name && $birth && $tel) {

		require("db_connect.php");
		$query = $db->exec("insert into signin_emp (name, birth, tel) 
							values ('$name', '$birth', '$tel')");
							
		header("Location:sign_list.php");
		exit;
	}
	
?>

