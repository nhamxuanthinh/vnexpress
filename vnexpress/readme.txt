1, install scrapy: pip3 install Scrapy
2, install postgresql: use homebrew
3, create database:
    CREATE DATABSE vnexpress;
4, create user:
    CREATE ROLE vnex WITH SUPERUSER CREATEDB CREATEROLE LOGIN ENCRYPTED PASSWORD 'root';
5, create table:

    CREATE TABLE article_info(
        id serial PRIMARY KEY,
        url VARCHAR (500) UNIQUE,
        title VARCHAR (500),
        article TEXT,
        date VARCHAR (500) UNIQUE
    );
6, pip3 install python-crontab