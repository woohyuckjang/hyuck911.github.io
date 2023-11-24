<?php
	$page = $_REQUEST["page"] ?? 1;

	$g_name = "";
	$g_birth = "";
	$g_tel = "";
	$action = "guest_insert.php";
	

	$num = $_REQUEST["num"] ?? 0;
	
	if ($num > 0) {
		require("db_connect.php");
		$query = $db->query("select * from guestid where num=$num");
		
		while ($row = $query->fetch()) {
		$g_name = $row["g_name"];
		$g_birth = $row["g_birth"];
		$g_tel = $row["g_tel"];
		$action = "guest_update.php?num=$num&page=$page";
		}
	}
?>
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        table { width:680px; text-align:center; margin-left:auto; margin-right:auto;}
        th, td{border: 1px solid; background-color:powderblue;}
    </style>
</head>
<body style="background-color:powderblue;">
<h1 style="background-color:white">
<p align="center" style="font-size:40px;">외부인원 ID신청</p>
</h1>

<form method="post" action="<?=$action?>">
    <table>
        <tr>
            <th>이름</th>
            <td><input type="text" name="g_name" maxlength="80" value="<?=$g_name?>" style="background-color:powderblue"></td>
        </tr>
        <tr>
            <th>생년월일</th>
            <td><input type="text" name="g_birth" maxlength="20" value="<?=$g_birth?>" style="background-color:powderblue"></td>
        </tr>
        <tr>
            <th>전화번호</th>
            <td><input type="text" name="g_tel" maxlength="20" value="<?=$g_tel?>" style="background-color:powderblue"></td>
        </tr>
    </table>


	<div style = "text-align:center;">
    <br><br>
	<input type="button" value="외부인원 신청 현황 보기" onclick="location.href='guest_access_list.php'">
    <input type="submit" value="저장">
    <input type="button" value="취소" onclick="history.back()">
	</div>
</form>

</body>
</html>
