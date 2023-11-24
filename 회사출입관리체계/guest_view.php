<?php
	$num = $_REQUEST["num"];
	$page = $_REQUEST["page"] ?? 1;
	
	require("db_connect.php");
	$query = $db->query("select * from guestid where num=$num");
	if ($row = $query->fetch()) {
		$g_name = $row["g_name"];
		$g_birth = $row["g_birth"];
		$g_tel = $row["g_tel"];
		$regtime = $row["regtime"];
	}
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

<table>
    <tr>
        <th>이름</th><td><?=$g_name?></td>
    </tr>
    <tr>
        <th>생년월일</th><td><?=$g_birth?></td>
    </tr>
    <tr>
        <th>전화번호</th><td><?=$g_tel?></td>
    </tr>
    <tr>
        <th>신청일시</th><td><?=$regtime?></td>
    </tr>
</table>

<br><br><br>
<div style = "text-align:center;">
<input type="button" value="목록보기" onclick="location.href='guest_access_list.php?page=<?=$page?>'">
<input type="button" value="수정"     onclick="location.href='guest_write.php?num=<?=$num?>&page=<?=$page?>'">
<input type="button" value="삭제"     onclick="location.href='guest_delete.php?num=<?=$num?>&page=<?=$page?>'">
</div>
</body>
</html>



</body>
</html>