<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        table     { width:1000px; text-align:center; margin-left:auto; margin-right:auto;}
        th        { background-color:white; }
        
        .num      { width: 80px; }
        .g_name    { width:230px; }
        .g_birth   { width:300px; }
		.g_tel	  { width:300px; }
        .regtime  { width:280px; }
		.g_sign	  { width:100px; }

        a         { text-decoration:none; }
        a:link    { color:blue; }
        a:visited { color:gray; }
        a:hover   { color:red;  }
	
        .center     { text-align:center; }
    </style>
</head>
<body style="background-color:powderblue;">
		<h1 style="background-color:white">
		<p align="center" style="font-size:40px;">외부인원 ID 결재</p>
		</h1>
<table>
    <tr>
        <th class="num"    >번호    </th>
        <th class="g_name"  >이름    </th>
        <th class="g_birth" >생년월일  </th>
        <th class="g_tel">전화번호</th>
		<th class="regtime">신청일시</th>
		<th class="g_sign">결재현황</th>
    </tr>
<?php

	$listSize = 5;

	$page = $_REQUEST["page"] ?? 1;
	
	$start = ($page - 1) * $listSize;
	
	require("db_connect.php");
	
	$query = $db->query("select * from guestid order by num desc limit $start, $listSize");
	while ($row = $query->fetch()) {
?>
    <tr>
        <td><?=$row["num"]?></td>
        <td><?=$row["g_name"]?></a></td>
        <td><?=$row["g_birth"]?></td>
        <td><?=$row["g_tel"]?></td>
        <td><?=$row["regtime"]?></td>
		<td><a href="sign_view_guest.php?num=<?=$row["num"]?>&page=<?=$page?>"><?=$row["g_sign"]?></td>
    </tr>
<?php
	}
?>

</table>

<br><br><br>
<div style = "text-align:center;">

<?php
	$paginationSize = 2;
	
	$firstLink = floor(($page - 1) / $paginationSize) * $paginationSize + 1;
	$lastLink = $firstLink + $paginationSize - 1;
	
	$query = $db->query("select count(*) from empid");
	$row = $query->fetch();
	$numRecords = $row[0];
	// $numRecords = $db->query("select count(*) from board")->fetch()[0];
	$numPages = ceil($numRecords / $listSize);
	if ($lastLink > $numPages) {
		$lastLink = $numPages;
	}
	
	if ($firstLink > 1) {
		$link = $firstLink - 1;
		echo "<a href=\"sign_list_guest.php?page=$link\">이전</a> ";
	}
	
	for($i = $firstLink; $i <= $lastLink; $i++) {
		if ($i == $page) {
			echo "<a href=\"sign_list_guest.php?page=$i\"><u>$i</u></a> ";
		} else {
			echo "<a href=\"sign_list_guest.php?page=$i\">$i</a> ";
		}
	}
	
	if ($lastLink < $numPages) {
		$link = $lastLink + 1;
		echo "<a href=\"sign_list_guest.php?page=$link\">다음</a> ";
	}

?>



<br><br><br>
<input type="button" value="홈으로" onclick="location.href='login_main.php'">
</div>
</body>
</html>
