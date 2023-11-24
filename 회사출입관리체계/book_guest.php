<?php
    $g_name = $_REQUEST["g_name"];
    $g_birth = $_REQUEST["g_birth"];
	$g_tel = $_REQUEST["g_tel"];
	
	if ($g_name && $g_birth && $g_tel) {

		require("db_connect.php");
		$query = $db->exec("insert into signin_guest (g_name, g_birth, g_tel) 
							values ('$g_name', '$g_birth', '$g_tel')");
							
		header("Location:sign_list_guest.php");
		exit;
	}
	
?>

