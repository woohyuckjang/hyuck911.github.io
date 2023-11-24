<?php
    session_start();
?>

<!doctype html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="background-color:powderblue;">
	<h1 style="background-color:white">
	<?php require("header.php");?>
	</h1>


		<div style="float: right;">
        <form action="logout.php" method="post">
            <strong><?=$_SESSION["userName"]?></strong>님 로그인 
            <input type="submit" value="로그아웃">
            <input type="button" value="회원정보 수정" 
                   onclick="window.open('member_update_form.php', 'popup', 'width=800, height=400')">
        </form>
		</div>
		<br><br>
		
		<p align="center">
		<input type="button" name="access" value ="출입신청" onclick="location.href='comeapplication_2.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
	
		<p align="center">
		<input type="button" name="access_status" value ="출입신청현황" onclick="location.href='all_application.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
		
		<!--
		<p align="center">
		<input type="button" name="regi" value ="등록현황" onclick="location.href='regi_2.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
	
	
		<p align="center">
		<input type="button" name="payment" value ="결제현황" onclick="location.href='paym.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p> -->

</body>
</html>
