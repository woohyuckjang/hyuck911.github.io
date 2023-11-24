<?php
	$id = $_REQUEST["id"];
	$pw = $_REQUEST["pw"];
	
	require("db_connect.php");
	
	$query = $db->query("select * from memberlog where id='$id' and pw='$pw' and code=0");
	if ($row = $query->fetch()) {
			session_start();
			$_SESSION["userId"  ] = $row["id"  ];
			$_SESSION["userName"] = $row["name"];
			
		
			header("Location:./login_main.php");
			exit;
	}

?>

<!doctype html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
<!--
<form action="comeapplication.php" method="post">
			<p align="center" style="font-size:50px;>출입신청<input type="button" name="ca1">&ensp;</p>
			<p align="center">비밀번호: <input type="password" name="pw">&ensp;</p>
			<p align="center"><input type = "submit" value = "로그인">
		</form>
-->
<script>
	alert('아이디 또는 비밀번호가 틀렸습니다.');
	history.back();
</script>

</body>
</html>
