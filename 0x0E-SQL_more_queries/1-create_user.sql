-- create user

CREAT USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL privilages ON *.* TO 'user_0d_1'@'localhost';
