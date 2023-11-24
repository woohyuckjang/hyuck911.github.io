<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        table     { width:1000px; text-align:center; margin-left:auto; margin-right:auto;}
        th        { background-color:white; }
        
        .name    { width:150px; }
        .birth   { width:200px; }
		.tel	  { width:200px; }

        a         { text-decoration:none; }
        a:link    { color:blue; }
        a:visited { color:gray; }
        a:hover   { color:red;  }
	
        .center     { text-align:center; }
    </style>
</head>
<body style="background-color:powderblue;">
		<h1 style="background-color:white">
		<p align="center" style="font-size:40px;">직원ID 현황</p>
		</h1>
<table>
    <tr>
        <th class="name"  >이름    </th>
        <th class="birth" >생년월일  </th>
        <th class="tel">전화번호</th>
    </tr>
<?php
	$listSize = 5;

	$page = $_REQUEST["page"] ?? 1;
	
	$start = ($page - 1) * $listSize;
	
	require("db_connect.php");
	
	$query = $db->query("select * from signin_emp limit $start, $listSize");
	while ($row = $query->fetch()) {
?>
    <tr>
        <td><?=$row["name"]?></td>
        <td><?=$row["birth"]?></td>
        <td><?=$row["tel"]?></td>
    </tr>
<?php
	}
?>

</table>

<div style = "text-align:center;">
<br>
<input type="button" value="홈으로" onclick="location.href='login_main.php'">
</div>
</body>
</html>
