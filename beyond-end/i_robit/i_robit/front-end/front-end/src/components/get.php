<?php
$name = isset($_POST['account']) ? htmlspecialchars($_POST['account']) : '';
$city = isset($_POST['password']) ? htmlspecialchars($_POST['password']) : '';
echo '用户名: ' . $name;
echo "\n";
echo '密码: ' .$city;
?>
