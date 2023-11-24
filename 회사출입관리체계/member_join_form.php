<!doctype html>
<html>
<head>
    <meta charset="utf-8">
	    <style>
        table { width:680px; text-align:center; margin-left:auto; margin-right:auto;}
        th    { border: 1px solid; background-color:white; }
		td    { border: 1px solid; background-color:powderblue; }
    </style>
</head>
<body style="background-color:powderblue;">
	<h1 style="background-color:white">
	<p align="center" style="font-size:40px;">계정 신청</p>
	</h1>
 
 <form action="member_join.php" method="post">
	    <table>
        <tr>
            <th>아이디</th>
            <td><input type="text" name="id" maxlength="80" style="background-color:powderblue"></td>
        </tr>
        <tr>
            <th>비밀번호</th>
            <td><input type="password" name="pw" maxlength="20" style="background-color:powderblue"></td>
        </tr>
        <tr>
            <th>이름</th>
            <td><input type="text" name="name" maxlength="20" style="background-color:powderblue"></td>
        </tr>
		<tr>
            <th>가입코드(없을 시 1)</th>
            <td><input type="text" name="code" maxlength="20" style="background-color:powderblue"></td>
        </tr>
    </table>
	<p align="center">
	<input type="submit" value="가입">
	<input type="button" value="로그인화면으로" onclick="history.back()"><br>
	</p>
 </form>
 
 </body>
 </html>