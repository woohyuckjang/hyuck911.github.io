<?php
	$page = $_REQUEST["page"] ?? 1;

	$name = "";
	$birth = "";
	$tel = "";
	$action = "emp_insert.php";
	
	$num = $_REQUEST["num"] ?? 0;
	
	if ($num > 0) {	
		require("db_connect.php");
		$query = $db->query("select * from empid where num=$num");
		
		while ($row = $query->fetch()) {
		$name = $row["name"];
		$birth = $row["birth"];
		$tel = $row["tel"];
		$action = "emp_update.php?num=$num&page=$page";
		}
	}
?>
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
<p align="center" style="font-size:40px;">직원ID신청</p>
</h1>

<form method="post" action="<?=$action?>">
    <table>
        <tr>
            <th>이름</th>
            <td><input type="text" name="name" maxlength="80" value="<?=$name?>" style="background-color:powderblue"></td>
        </tr>
        <tr>
            <th>생년월일</th>
            <td><input type="text" name="birth" maxlength="20" value="<?=$birth?>" style="background-color:powderblue"></td>
        </tr>
        <tr>
            <th>전화번호</th>
            <td><input type="text" name="tel" maxlength="20" value="<?=$tel?>" style="background-color:powderblue"></td>
        </tr>
    </table>

    <br><br>
	<div style = "text-align:center;">
	<input type="button" value="직원 신청 현황 보기" onclick="location.href='emp_access_list.php'">
    <input type="submit" value="저장">
    <input type="button" value="취소" onclick="history.back()">
	</div>
</form>

</body>
</html>
