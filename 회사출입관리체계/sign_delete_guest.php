<?php
	$num = $_REQUEST["num"];
	$page = $_REQUEST["page"] ?? 1;

	require("db_connect.php");
	$query = $db->exec("delete from guestid where num=$num");
	
	
	header("Location:sign_list_guest.php?page=$page");

	
?>