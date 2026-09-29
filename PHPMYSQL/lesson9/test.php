<?php
if (isset($_GET['username'])) {
    $username = $_GET['username'];
    echo $username;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="test.php" method="get">
        <input type="text" id="username" name="username">
        <input type="submit" value="Submit">
    </form>
</body>
</html>