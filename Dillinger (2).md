# Dillinger

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. 

QUERY 1:

The view new1 counts the total number of paths against each  path  and replace function is used to get the slug from the path.

create view  new1 as (select replace(path,'/article/',''),count(path) from log group by path);
CREATE VIEW
 select * from new1;
 
 The view new2 combines a table article with view new1 to get the slug and count against each slug.
 
 create view new2 as( select slug,count from articles,new1 where articles.slug=new1.replace);
CREATE VIEW
 select * from new2;
           slug            | count  
---------------------------+--------
 goats-eat-googles         | 169812
 balloon-goons-doomed      | 169114
 trouble-for-troubled      | 169620
 candidate-is-jerk         | 677294
 bears-love-berries        | 507602
 bad-things-gone           | 340196
 so-many-bears             | 169008
 media-obsessed-with-bears | 168766
(8 rows)

The final query gives us the top three articles .

select * from new2 order by count desc limit 3;
        slug        | count  
--------------------+--------
 candidate-is-jerk  | 677294
 bears-love-berries | 507602
 bad-things-gone    | 340196
(3 rows)


QUERY 2:

The view one here combines the tables authors and articles to get name of authors and slug from the author title respectively.

create view one as(select name,slug from authors,articles where authors.id=articles.author);
select * from one;
name          |           slug            
------------------------+---------------------------
 Anonymous Contributor  | bad-things-gone
 Markoff Chaney         | balloon-goons-doomed
 Ursula La Multa        | bears-love-berries
 Rudolf von Treppenwitz | candidate-is-jerk
 Ursula La Multa        | goats-eat-googles
 Ursula La Multa        | media-obsessed-with-bears
 Rudolf von Treppenwitz | trouble-for-troubled
 Ursula La Multa        | so-many-bears
(8 rows)


The view two here counts the number of time a path is visited and the replace function is used to get the slug from the path .

create view two as(select replace(path,'/article/',''),count(path) from log group by path);
CREATE VIEW
select * from two;

The answer view here combines the views one and two to get the name of authors and the number of page views their article got.

create view ans as(select name,count from one,two where one.slug=two.replace);
CREATE VIEW
select * from ans;
          name          | count  
------------------------+--------
 Ursula La Multa        | 169812
 Markoff Chaney         | 169114
 Rudolf von Treppenwitz | 169620
 Rudolf von Treppenwitz | 677294
 Ursula La Multa        | 507602
 Anonymous Contributor  | 340196
 Ursula La Multa        | 169008
 Ursula La Multa        | 168766
(8 rows)

The view output2 sums up the view against each author.

create view output2 as(select name,sum(count) from one,two where one.slug=two.replace group by name);
CREATE VIEW
select * from output2;
          name          |   sum   
------------------------+---------
 Markoff Chaney         |  169114
 Anonymous Contributor  |  340196
 Ursula La Multa        | 1015188
 Rudolf von Treppenwitz |  846914
(4 rows)

The final query answers the names of authors in decreasing order of page views.

select * from output2 order by sum desc;
          name          |   sum   
------------------------+---------
 Ursula La Multa        | 1015188
 Rudolf von Treppenwitz |  846914
 Anonymous Contributor  |  340196
 Markoff Chaney         |  169114
(4 rows)


QUERY 3:

The view errorcount extracts the date from time and tells us hoq many error requests re generated on a particular date.

create view errorcount as( select date(time),count(status) from log where status!='200 OK' group by date);
CREATE VIEW
 select * from errorcount;
    date    | count 
------------+-------
 2016-07-31 |   658
 2016-07-06 |   840
 2016-07-17 |  2530
 2016-07-12 |   746
 2016-07-10 |   742
 2016-07-25 |   782
 2016-07-14 |   766
 2016-07-28 |   786
 2016-07-30 |   794
 2016-07-22 |   812
 2016-07-09 |   820
 2016-07-27 |   734
 2016-07-23 |   746
 2016-07-01 |   548
 2016-07-08 |   836
 2016-07-26 |   792
 2016-07-19 |   866
 2016-07-24 |   862
 2016-07-07 |   720
 2016-07-05 |   846
 2016-07-13 |   766
 2016-07-15 |   816
 2016-07-03 |   802
 2016-07-11 |   806
 2016-07-02 |   778
 2016-07-16 |   748
 2016-07-29 |   764
 2016-07-18 |   748
 2016-07-04 |   760
 2016-07-21 |   836
 2016-07-20 |   766
(31 rows)

The view totalcount extracts the date and counts the total number of requests generated on a particular date.

create view totalcount as(select date(time),count(status) as total from log group by date);
CREATE VIEW
select * from totalcount;
    date    | total 
------------+-------
 2016-07-01 | 66295
 2016-07-02 | 94635
 2016-07-03 | 94088
 2016-07-04 | 94138
 2016-07-05 | 93567
 2016-07-06 | 93874
 2016-07-07 | 93823
 2016-07-08 | 94448
 2016-07-09 | 94733
 2016-07-10 | 93369
 2016-07-11 | 93377
 2016-07-12 | 94000
 2016-07-13 | 94629
 2016-07-14 | 94593
 2016-07-15 | 94225
 2016-07-16 | 93412
 2016-07-17 | 96111
 2016-07-18 | 95375
 2016-07-19 | 94891
 2016-07-20 | 93480
 2016-07-21 | 94733
 2016-07-22 | 94678
 2016-07-23 | 94084
 2016-07-24 | 94509
 2016-07-25 | 93616
 2016-07-26 | 93159
 2016-07-27 | 93414
 2016-07-28 | 93973
 2016-07-29 | 94136
 2016-07-30 | 94384
 2016-07-31 | 78600
(31 rows)

the view combine is used to get the view of error count as well as total count on a particular date.

create view combine as (select error.date,error.count,total.total from error,total where error.date=total.date);
CREATE VIEW
select * from combine;
    date    | count | total 
------------+-------+-------
 2016-07-01 |   548 | 66295
 2016-07-02 |   778 | 94635
 2016-07-03 |   802 | 94088
 2016-07-04 |   760 | 94138
 2016-07-05 |   846 | 93567
 2016-07-06 |   840 | 93874
 2016-07-07 |   720 | 93823
 2016-07-08 |   836 | 94448
 2016-07-09 |   820 | 94733
 2016-07-10 |   742 | 93369
 2016-07-11 |   806 | 93377
 2016-07-12 |   746 | 94000
 2016-07-13 |   766 | 94629
 2016-07-14 |   766 | 94593
 2016-07-15 |   816 | 94225
 2016-07-16 |   748 | 93412
 2016-07-17 |  2530 | 96111
 2016-07-18 |   748 | 95375
 2016-07-19 |   866 | 94891
 2016-07-20 |   766 | 93480
 2016-07-21 |   836 | 94733
 2016-07-22 |   812 | 94678
 2016-07-23 |   746 | 94084
 2016-07-24 |   862 | 94509
 2016-07-25 |   782 | 93616
 2016-07-26 |   792 | 93159
 2016-07-27 |   734 | 93414
 2016-07-28 |   786 | 93973
 2016-07-29 |   764 | 94136
 2016-07-30 |   794 | 94384
 2016-07-31 |   658 | 78600
(31 rows)

The view result1 is used to get perecentage of errors on each date.
A truncate function is used to get  the percentage value upto one decimal place only.

create view result1 as(select date,trunc((count:: decimal/total)*100,1) as res  from combine order by res desc);
CREATE VIEW
select * from result1;
    date    | res 
------------+-----
 2016-07-17 | 2.6
 2016-07-24 | 0.9
 2016-07-19 | 0.9
 2016-07-05 | 0.9
 2016-07-06 | 0.8
 2016-07-08 | 0.8
 2016-07-09 | 0.8
 2016-07-11 | 0.8
 2016-07-13 | 0.8
 2016-07-14 | 0.8
 2016-07-15 | 0.8
 2016-07-16 | 0.8
 2016-07-31 | 0.8
 2016-07-02 | 0.8
 2016-07-03 | 0.8
 2016-07-04 | 0.8
 2016-07-25 | 0.8
 2016-07-26 | 0.8
 2016-07-28 | 0.8
 2016-07-29 | 0.8
 2016-07-30 | 0.8
 2016-07-01 | 0.8
 2016-07-20 | 0.8
 2016-07-21 | 0.8
 2016-07-22 | 0.8
 2016-07-12 | 0.7
 2016-07-18 | 0.7
 2016-07-10 | 0.7
 2016-07-23 | 0.7
 2016-07-07 | 0.7
 2016-07-27 | 0.7
(31 rows)

The final query shows the ouput where  requests for a particular date lead to rorrs  more than 1%.

 select * from result1 where res>1.0;
    date    | res 
------------+-----
 2016-07-17 | 2.6
(1 row)








