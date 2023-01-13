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
                <h1>GLB勤怠管理アプリ for Member</h1>
                <form action="index.php" method="post">
                    <p>出勤Bot</p>
                    <button type="submit" name="script01">出勤（リモート）</button><br>
                    <button type="submit" name="script02">出勤（出社）</button><br>
                    <button type="submit" name="script03">出勤（リモート&出社）</button><br><br>
                    <p>退勤Bot</p>
                    <button type="submit" name="script04">退勤（リモート）</button><br>
                    <button type="submit" name="script05">退勤（退社）</button><br><br>
                    <p>勤務場所を「在宅勤務」へ一括変更Bot</p>
                    <button type="submit" name="script06">「在宅勤務」へ一括変更</button><br>

                </form>
            </div>
            <h2>/------実行ログ-------/</h2>
            <div class="result">
                <?php
                    $result = "";
                    if (isset($_POST['script01'])) {
                        $result = "kintai_change_start_remote.pyを実行します";
                        $cmd = 'python /var/app/kintai_change_start_remote.py';
                    }
                    elseif (isset($_POST['script02'])) {
                        $result = "kintai_change_start_syussya.pyを実行します";
                        $cmd = 'python /var/app/kintai_change_start_syussya.py';
                    }
                    elseif (isset($_POST['script03'])) {
                        $result = "kintai_change_start_both.pyを実行します";
                        $cmd = 'python /var/app/kintai_change_start_both.py';
                    }
                    elseif (isset($_POST['script04'])) {
                        $result = "kintai_change_finish_remote.pyを実行します";
                        $cmd = 'python /var/app/kintai_change_finish_remote.py';
                    }
                    elseif (isset($_POST['script05'])) {
                        $result = "kintai_change_finish_taikan.pyを実行します";
                        $cmd = 'python /var/app/kintai_change_finish_taikan.py';
                    }
                    elseif (isset($_POST['script06'])) {
                        $result = "kintai_change_status_zaitaku.pyを実行します";
                        $cmd = 'python /var/app/kintai_change_status_zaitaku.py';
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
