CREATE DATABASE bookrec IF NOT EXISTS
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# using utfmb4 to include emoji character.

CREATE TABLE book(
    uid INT primary key auto_increment,
    name VARCHAR(200) NOT NULL,
    imgUrl VARCHAR(200),
    isbn VARCHAR(20),
    author VARCHAR(100),
    press VARCHAR(100),
    doubanPoint FLOAT DEFAULT 0,
    doubanRateSum INT DEFAULT 0,
    bookDescription VARCHAR(2000),
    authorDescription VARCHAR(2000),
    sysuLibUrl VARCHAR(200),
    #
    relevantBooks VARCHAR(300)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE bookLabel(
    uid INT primary key auto_increment,
    name VARCHAR(200) NOT NULL,
    useCount INT DEFAULT 1
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE labelOfBook(
    bookUid INT NOT NULL,
    bookLabelUid INT NOT NULL
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE user(
    uid INT primary key auto_increment,
    token VARCHAR(100) NOT NULL,
    recBooks VARCHAR(300)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE userBookView(
    userUid INT NOT NULL,
    bookUid INT NOT NULL,
    viewCount INT DEFAULT 1
) DEFAULT CHARSET=utf8mb4;

