# net_text

python3 で mosqultto_sub で mosquitto からメッセージを受けとって、
それを mysql のテーブルに書きこむ IoTAgent みたいなやつ。

python3
mosquitto
mysql

をインストールしておく必要あり。
mysql は、下記の操作をして iot データベースと sensor_data テーブルを作成しておく。

CREATE TABLE iot.sensor_data (time DATETIME, temp FLOAT); 

適当なユーザを作成して、アクセス権を付与しておく。

$ mysql -u root -p
Enter password:

> CREATE DATABASE iot;
> CREATE USER kani IDENTIFIED BY 'dbpassword';
> GRANT ALL PRIVILEGES ON dbname.* TO kani;

こんな感じで。

データの確認は select でやる。

mysql> use iot
mysql> select * from sensor_data;
+---------------------+-------+
| time                | temp  |
+---------------------+-------+
| 2019-02-27 06:09:20 |  1.23 |
| 2019-02-27 06:49:21 |  11.1 |
| 2019-02-27 06:49:29 |  12.5 |
| 2019-02-27 06:56:54 |  12.5 |
| 2019-02-27 06:56:58 |  13.5 |
| 2019-02-27 06:57:01 |  15.5 |
| 2019-02-27 11:30:50 | 11.12 |
| 2019-02-27 11:30:57 | 11.13 |
+---------------------+-------+
8 rows in set (0.00 sec)

時刻は VPS のあるリージョンの時刻になっているので注意。
