-- a script that creates the database hbtn_0d_2 and the user user_0d_2.

-- creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating user and flush
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- granting permissions to user_0d_2 for the database hbtn_0d_2 and flush
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
