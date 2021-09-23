# Flask with mysql project
In this project we are gonna build a super simple app commit by commit, to learn the basic of flask with mysql.
The project is conducted on mac M1.

### Prerequisite
- python3
- mysql (see __mysql-installation.md__ to install mysql on mac M1)

### Installations

Let's start with installing flask-
```bash
pip3 install flask
```
Then we need flask-mysqldb package-
```bash
pip3 install flask-mysqldb
```

### Execution

To run __app.py__-
```bash
python3 app.py
```

Now if we go to __localhost:5000__, we can see that it says __Not Found The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.__

After adding the route, it will say __Hello World__

### MySQL database building

Go to the terminal and login to your mysql server
```bash
mysql -u root -p
```
Give your password. Then inside `mysql` shell, create a database named `flaskapp`-
```sql
CREATE DATABASE flaskapp;
```
Set the created database as the default database-
```sql
USE flaskapp
```
Now create a table in `flaskapp` that has two columns `user` and `email`-
```sql
CREATE TABLE users(name varchar(20), email varchar(40));
```
