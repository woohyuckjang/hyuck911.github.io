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

<?php
    if (empty($_SESSION["userId"])) {
		
		
?>      <div style="float: right;">
		<input type="button" value="회원 가입" 
            onclick="location.href='member_join_form.php'">
		</div><br>
		<center>
        <form action="login.php" method="post">
			<b> 관리자 로그인 </b><br>
            아이디:   <input type="text"     name="id">&ensp;<br>
            비밀번호: <input type="password" name="pw">&ensp;<br><br>
            <input type="submit" value="관리자로그인">
            
        </form>
		<br><br>
		<form action="login_user.php" method="post">
			<b> 사용자 로그인 </b><br>
			아이디:   <input type="text"     name="id">&ensp;<br>
            비밀번호: <input type="password" name="pw">&ensp;<br><br>
		<input type="submit" value="일반 사용자 로그인" >
		</form>
		<br><br>
		
		</center>
<?php
    } else {
?>		<div style="float: right;">
        <form action="logout.php" method="post">
            <strong><?=$_SESSION["userName"]?></strong>님 로그인
            <input type="submit" value="로그아웃">
            <input type="button" value="회원정보 수정" 
                   onclick="window.open('member_update_form.php', 'popup', 'width=800, height=400')">
        </form>
		</div>
		<br><br>
		<!--
		<p align="center">
		<input type="button" name="access" value ="출입신청" onclick="location.href='comeapplication_2.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
	
		<p align="center">
		<input type="button" name="access_status" value ="출입신청현황" onclick="location.href='all_application.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
		-->
		
		<p align="center">
		<input type="button" name="regi" value ="등록현황" onclick="location.href='registration.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
	
	
		<p align="center">
		<input type="button" name="payment" value ="결재현황" onclick="location.href='sign.php'"
		style="WIDTH: 400pt; HEIGHT: 80pt; font-size:20pt;">
		</p>
<?php        
    }
?>
</body>
</html>
