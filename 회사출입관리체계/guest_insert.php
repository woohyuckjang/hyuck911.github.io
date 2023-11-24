<?php
    $g_name = $_REQUEST["g_name"];
    $g_birth = $_REQUEST["g_birth"];
	$g_tel = $_REQUEST["g_tel"];
	
	if ($g_name && $g_birth && $g_tel) {
		$regtime = date("Y-m-d H:i:s");
		
		require("db_connect.php");
		$query = $db->exec("insert into guestid (g_name, g_birth, g_tel, regtime) 
							values ('$g_name', '$g_birth', '$g_tel', '$regtime')");
							
		header("Location:guest_write.php");
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
