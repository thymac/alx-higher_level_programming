-- Creates the user user_0d_1 with all privileges.
CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost' 
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost'
       	WITH GRANT OPTION;
CREATE USER
	'user_0d_1'@'%' 
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'%'
       	WITH GRANT OPTION;
