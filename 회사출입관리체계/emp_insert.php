<?php
    $name = $_REQUEST["name"];
    $birth = $_REQUEST["birth"];
	$tel = $_REQUEST["tel"];
	
	if ($name && $birth && $tel) {
		$regtime = date("Y-m-d H:i:s");
		
		require("db_connect.php");
		$query = $db->exec("insert into empid (name, birth, tel, regtime) 
							values ('$name', '$birth', '$tel', '$regtime')");
							
		header("Location:emp_write.php");
		exit;
	}
	
?>
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>

<script>
	alert('모든 항목이 빈칸없이 입력되어야 합니다.');
	history.back();
</script>

</body>
</html>
