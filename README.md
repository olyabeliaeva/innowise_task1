# innowise_task1


This application represents a simple system of loading data from JSON files into a database and export data in JSON or XML format.


***Configure your database:***

```
DB_NAME = 'your_database_name',
DB_USER = 'your_database_user',
DB_PASSWORD = 'your_database_password',
DB_PORT = 'your_database_port'.
```

***To start the application execute the following command, you shold choose format for output files:*** 
```
$ python main.py --students-json students.json --rooms-json rooms.json --query 1 --output-format JSON/XML
```

The repository contains 5 queries to the database:
1) List of rooms and the number of students in each of them.
2) 5 rooms where the average age of students is the smallest.
3) 5 rooms with the largest difference in student age.
4) List of rooms where mixed-sex students live.

Also proposed is the option of optimizing queries using indexes.