<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        table     { width:680px; text-align:center; margin-left:auto; margin-right:auto;}
        th        { background-color:white; }
        
        .num      { width: 80px; }
        .title    { width:230px; }
        .writer   { width:100px; }
        .regtime  { width:180px; }

        a         { text-decoration:none; }
        a:link    { color:blue; }
        a:visited { color:gray; }
        a:hover   { color:red;  }
	
        .center     { text-align:center; }
    </style>
</head>
<body style="background-color:powderblue;">
		<h1 style="background-color:white">
		<p align="center" style="font-size:40px;">직원ID신청현황</p>
		</h1>
<table>
    <tr>
        <th class="num"    >번호    </th>
        <th class="name"  >이름    </th>
        <th class="birth" >생년월일  </th>
        <th class="tel">전화번호</th>
		<th class="regtime">신청일시</th>
    </tr>
<?php

	$listSize = 5;

	$page = $_REQUEST["page"] ?? 1;
	
	$start = ($page - 1) * $listSize;
	
	require("db_connect.php");
	
	$query = $db->query("select * from empid order by num desc limit $start, $listSize");
	while ($row = $query->fetch()) {
?>
    <tr>
        <td><?=$row["num"]?></td>
        <td style="text-align:center;"><a href="emp_view.php?num=<?=$row["num"]?>&page=<?=$page?>"><?=$row["name"]?></a></td>
        <td><?=$row["birth"]?></td>
        <td><?=$row["tel"]?></td>
        <td><?=$row["regtime"]?></td>
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
	$numPages = ceil($numRecords / $listSize);
	if ($lastLink > $numPages) {
		$lastLink = $numPages;
	}
	
	if ($firstLink > 1) {
		$link = $firstLink - 1;
		echo "<a href=\"emp_access_list.php?page=$link\">이전</a> ";
	}
	
	for($i = $firstLink; $i <= $lastLink; $i++) {
		if ($i == $page) {
			echo "<a href=\"emp_access_list.php?page=$i\"><u>$i</u></a> ";
		} else {
			echo "<a href=\"emp_access_list.php?page=$i\">$i</a> ";
		}
	}
	
	if ($lastLink < $numPages) {
		$link = $lastLink + 1;
		echo "<a href=\"emp_access_list.php?page=$link\">다음</a> ";
	}

?>



<br><br><br>
<input type="button" value="홈으로" onclick="location.href='login_main_2.php'">
<input type="button" value="직원출입신청하기" onclick="location.href='emp_write.php'">
</div>
</body>
</html>
