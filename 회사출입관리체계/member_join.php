<!doctype html>
<html>
<head>
<body style="background-color:powderblue;">
<h1 style="background-color:white">
    <meta charset="utf-8">
</head>
<body>

<?php
	$id = $_REQUEST["id"];
	$pw = $_REQUEST["pw"];
	$name = $_REQUEST["name"];
	$code = $_REQUEST["code"];
	
	require("db_connect.php");
	
	if ( !($id && $pw && $name && $code)){
?>
	<script>
		alert('빈칸없이 입력해야합니다.');
		history.back();
	</script>
<?php
	} else if ($db->query("select * from memberlog where id='$id'")->fetch()) { // 이미 있는 아이디이면
?>
	<script>
		alert('이미 등록된 아이디입니다.');
		history.back();
	</script>

<?php
	} else {
		
		
		$db->exec("insert into memberlog values ('$id', '$pw', '$name', '$code')");
?>
		<p align="center">가입이 완료되었습니다.<br></h1></p>
		<p align="center"><input type="button" value="로그인 화면으로" onclick="location.href='login_main.php'"></p>
<?php
	}
?>

</body>
</html>