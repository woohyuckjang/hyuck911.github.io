<?php
	$num = $_REQUEST["num"];
	$page = $_REQUEST["page"] ?? 1;
	$action = "book_guest.php";
	
	require("db_connect.php");
	$query = $db->query("select * from guestid where num=$num");
	if ($row = $query->fetch()) {
		$g_name = $row["g_name"];
		$g_birth = $row["g_birth"];
		$g_tel = $row["g_tel"];
		$regtime = $row["regtime"];
		$g_sign = $row["g_sign"];
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
<form method="post" action="<?=$action?>">
<table>
    <tr>
        <th>이름</th><td><?=$g_name?><input type="hidden" name="g_name" value="<?=$g_name?>"></td>
    </tr>
    <tr>
        <th>생년월일</th><td><?=$g_birth?><input type="hidden" name="g_birth" value="<?=$g_birth?>"></td>
    </tr>
    <tr>
        <th>전화번호</th><td><?=$g_tel?><input type="hidden" name="g_tel" value="<?=$g_tel?>"></td>
    </tr>
    <tr>
        <th>신청일시</th><td><?=$regtime?></td>
    </tr>
	<tr>
        <th>결재내역</th><td><?=$g_sign?></td>
    </tr>
</table>

<br><br><br>
<div style = "text-align:center;">
<input type="button" value="목록보기" onclick="location.href='sign_list_guest.php?page=<?=$page?>'"><br>
<input type="submit" value="결재하기">
<input type="button" value="결재누락"     onclick="location.href='sign_delete_guest.php?num=<?=$num?>&page=<?=$page?>'">
</div>
</body>
</html>



</body>
</html>
