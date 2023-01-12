<?php
    $result = "";
    if (isset($_POST['script01'])) {
        $result = "kintai_check_registration.pyを実行します";
        $cmd = 'python /var/app/kintai_check_registration.py';
    }
    elseif (isset($_POST['script02'])) {
        $result = "script_zaitaku.pyを実行します";
        $cmd = 'python /var/app/script_zaitaku.py';
    }
    elseif (isset($_POST['script03'])) {
        $result = "test-seleinum.pyを実行します";
        $cmd = 'python /var/app/test-seleinum.py';
    }
    echo $result;
    print("<br/>");
    exec($cmd, $out);
    foreach ($out as $value) {
      print($value);
      print("<br/>");
  }


?>
<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>GLB勤怠アプリ</title>
    </head>
    <body>
        <form action="index.php" method="post">
            <button type="submit" name="script01">Script01</button>
            <button type="submit" name="script02">Script02</button>
            <button type="submit" name="script03">Script03</button>
        </form>
    </body>
</html>
