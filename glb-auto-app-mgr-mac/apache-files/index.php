<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>GLB勤怠アプリ</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div>
            <div class="header">
                <h1>GLB勤怠管理アプリ for Mgr</h1>
                <form action="index.php" method="post">
                    <button type="submit" name="script01">勤怠打刻確認</button>
                    <button type="submit" name="script02">勤怠申請提出確認</button>
                    <button type="submit" name="script03">残業45時間チェック</button>
                </form>
            </div>
            <h2>/------実行ログ-------/</h2>
            <div class="result">
                <?php
                    $result = "";
                    if (isset($_POST['script01'])) {
                        $result = "勤怠打刻確認を実行します";
                        $cmd = 'python /var/app/kintai_check_start_timestomp.py';
                    }
                    elseif (isset($_POST['script02'])) {
                        $result = "勤怠申請提出確認を実行します";
                        $cmd = 'python /var/app/kintai_check_registration.py';
                    }
                    elseif (isset($_POST['script03'])) {
                        $result = "残業45時間チェックを実行します";
                        $cmd = 'python /var/app/kintai_check_over_45_hours.py';
                    }

                    echo $result;
                    print("<br/>");
                    exec($cmd, $out);
                    foreach ($out as $value) {
                    print($value);
                    print("<br/>");
                    }
                ?>
            </div>
        </div>
    </body>
</html>
