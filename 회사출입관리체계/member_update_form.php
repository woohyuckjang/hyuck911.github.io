<?php
    session_start();
    $id = $_SESSION["userId"];
    
    require("db_connect.php");

    $query = $db->query("select * from memberlog where id='$id'");
    $row = $query->fetch();
        
    $pw   = $row["pw"  ];
    $name = $row["name"];
?>

<!doctype html>
<html>
<head>
    <meta charset="utf-8">
	<style>
		table { width:680px; text-align:center; margin-left:auto; margin-right:auto;}
		th    { width:100px; border:1px solid gray; background-color:white; }
        td    { text-align:left; border:1px solid gray; }
    </style>
</head>
<body style="background-color:powderblue;">
	<h1 style="background-color:white">
	<p align="center" style="font-size:40px;">회원정보수정</p>
	</h1>
<form action="member_update.php" method="post">
    <table>
        <tr>
            <td>아이디</td>
            <td><input type="text" name="id" readonly value="<?=$id?>"></td>
        </tr>
        
        <tr>    
            <td>비밀번호</td>
            <td><input type="password" name="pw" value="<?=$pw?>"></td>
        </tr>
        
        <tr>
            <td>이름</td>
            <td><input type="text" name="name" value="<?=$name?>"></td>
        </tr>
        </table>
		<p align="center">
    <input type="submit" value="등록"> </p>
</form>
</body>
</html>
