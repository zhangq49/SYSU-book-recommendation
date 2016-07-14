drop database bookrec;
create database bookrec;
use bookrec;

select * from bookLabel2 where name = 'hao' order by useCount limit 1;

drop table bookLabel2;
CREATE TABLE bookLabel2(
    uid INT primary key,
    name VARCHAR(200) NOT NULL,
    useCount INT DEFAULT 1
) DEFAULT CHARSET=utf8;

CREATE TABLE labelOfBook2(
    bookUid INT NOT NULL,
    bookLabelUid INT NOT NULL
) DEFAULT CHARSET=utf8;

rename table bookLabel to oldLabel;
rename table labelOfBook to oldRel;

rename table bookLabel2 to bookLabel;
rename table labelOfBook2 to labelOfBook;