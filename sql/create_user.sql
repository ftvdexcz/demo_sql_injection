CREATE DB:
CREATE DATABASE demo

CREATE TABLE Users (
    id int IDENTITY(1,1) PRIMARY KEY,
    name nvarchar(255) not null unique,
    password nvarchar(255) not null,
);

INSERT INTO Users VALUES('Admin', '1234')
INSERT INTO Users VALUES('John', '1234')
INSERT INTO Users VALUES('Nick', 'asdf')
INSERT INTO Users VALUES('Joe', 'vadde')
INSERT INTO Users VALUES('Anna', 'jfdaf')