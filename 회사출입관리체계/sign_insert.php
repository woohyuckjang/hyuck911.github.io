<?php
    $name = $_REQUEST["name"];
    $birth = $_REQUEST["birth"];
	$tel = $_REQUEST["tel"];
	
	if ($name && $birth && $tel) {
		$regtime = date("Y-m-d H:i:s");
		
		require("db_connect.php");
		$query = $db->exec("insert into signin_emp (name, birth, tel) 
							values ('$name', '$birth', '$tel')");
							
		header("Location:sign_view.php");
		exit;
	}
	
?>
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>


</body>
</html>
