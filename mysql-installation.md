# MySQL installation on Mac M1

* From [here](https://dev.mysql.com/downloads/mysql/), download mysql community server. Choose the file **macOS 11 (ARM, 64-bit), DMG Archive** if you have M1 chip architecture in your mac.
* After downloading, install mysql. Keep the default choices and hit `Continue`.
* After it is installed, go to System Preferences. You will find the MySQL server running.
* Now if you type `mysql` from your terminal, you will get a message __mysql: command not found__. So you have to give the path to mysql to your `~/.profile`, then it will recognize mysql. To do so,
```bash
sudo open -a TextEdit ~/.profile
```
Then inside the `~/.profile`, add the following-
```bash
export PATH=$PATH:/usr/local/mysql/bin
```
Save the file and close it. Then restart your bash profile with this command-
```bash
source ~/.profile
```
Now you should be able to run the command mysql
* Hitting the command `mysql` will give __Access denied for user__ error unless we login. To login-
```bash
mysql -u root -p
```
Then give the password that you created during installation. Finally you will be able to see the `mysql>` prompt in your terminal. You can use the prompt to write any mysql query.
```sql
show databases;
```
It will show you the existing databases. 
To exit the mysql prompt, simply type
```sql
exit
```
