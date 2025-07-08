CREATE TABLE attendance_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    name VARCHAR(100) NOT NULL,
    temperature FLOAT NOT NULL
);

INSERT INTO attendance_log (timestamp, name, temperature)
VALUES (NOW(), 'Ramya', 37.8);