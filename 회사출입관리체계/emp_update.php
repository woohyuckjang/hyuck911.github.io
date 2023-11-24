<?php
	$num = $_REQUEST["num"];
	$page = $_REQUEST["page"] ?? 1;

    $name = $_REQUEST["name"];
    $birth = $_REQUEST["birth"];
	$tel = $_REQUEST["tel"];
	
	if ($name && $birth && $tel) {
		$regtime = date("Y-m-d H:i:s");
		
		require("db_connect.php");
		$query = $db->exec("update empid set name='$name', birth='$birth', tel='$tel',
					           				 regtime='$regtime' where num=$num");
							
		header("Location:emp_access_list.php?num=$num&page=$page");
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
