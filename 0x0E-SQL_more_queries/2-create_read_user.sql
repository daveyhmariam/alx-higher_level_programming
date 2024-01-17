-- create database and user with set privelages

CREATE DATABASE IF NOT EXISTs hbtn_0d_2;
CREAT USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO 'user_0d_2'@'localhost';
