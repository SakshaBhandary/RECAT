<!DOCTYPE html>
<html>
<head>
  <title>Covid Secure Recat Dashboard</title>
</head>
<body>
  <h1>Attendance & Temperature Log</h1>
  <table border="1">
    <tr><th>Timestamp</th><th>Name</th><th>Temperature</th></tr>
    <?php
    $file = fopen("attendance_log.csv", "r");
    while (($data = fgetcsv($file)) !== FALSE) {
        echo "<tr><td>{$data[0]}</td><td>{$data[1]}</td><td>{$data[2]}</td></tr>";
    }
    fclose($file);
    ?>
  </table>
</body>
</html>