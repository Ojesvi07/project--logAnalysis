# LOG ANALYSIS

PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. 

This project aims at getting answers by making queries in postgresql and writing a code for the same (that connects it to the web server log).The database here contains information on newspaper articles.

## What this code finds?
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?


QUERY 1:

The view new1 counts the total number of paths against each  path  and replace function is used to get the slug from the path.
```
create view  new1 as (select replace(path,'/article/',''),count(path) from log group by path);
```
 
The view new2 combines a table article with view new1 to get the slug and count against each slug.
```
create view new2 as( select slug,count from articles,new1 where articles.slug=new1.replace);
```

QUERY 2:

The view one here combines the tables authors and articles to get name of authors and slug from the author title respectively.
```
create view one as(select name,slug from authors,articles where authors.id=articles.author);
```

The view two here counts the number of time a path is visited and the replace function is used to get the slug from the path .
```
create view two as(select replace(path,'/article/',''),count(path) from log group by path);
```


The answer view here combines the views one and two to get the name of authors and the number of page views their article got.
```
create view ans as(select name,count from one,two where one.slug=two.replace);
```

The view output2 sums up the view against each author.
```
create view output2 as(select name,sum(count) from one,two where one.slug=two.replace group by name);
```


QUERY 3:

The view errorcount extracts the date from time and tells us hoq many error requests re generated on a particular date.
```
create view errorcount as( select date(time),count(status) from log where status!='200 OK' group by date);
```

 
The view totalcount extracts the date and counts the total number of requests generated on a particular date.
```
create view totalcount as(select date(time),count(status) as total from log group by date);
```


the view combine is used to get the view of error count as well as total count on a particular date.
```
create view combine as (select errorcount.date,errorcount.count,totalcount.total from errorcount,totalcount where errorcount.date=totalcount.date);
```

The view result1 is used to get perecentage of errors on each date.
A truncate function is used to get  the percentage value upto one decimal place only.
```
create view result1 as(select date,trunc((count:: decimal/total)*100,1) as res  from combine order by res desc);
```

## How to use this?
This is a simple python code so all you need to do is copy the code to the same location as your databse.Run the command

`$ python3 project.py`








