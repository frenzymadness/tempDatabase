-- Not necessary for sqlite
--CREATE DATABASE 'tempreatures';

-- Main table for all records
CREATE TABLE records(date CHAR(15) PRIMARY KEY, position CHAR(100) NOT NULL, tempreature REAL NOT NULL, condition CHAR(150));

-- Tables for averages values for day, month and year
CREATE TABLE days(date CHAR(15) PRIMARY KEY, position CHAR(100) NOT NULL, tempreature REAL NOT NULL, condition CHAR(150));
CREATE TABLE months(date CHAR(15) PRIMARY KEY, position CHAR(100) NOT NULL, tempreature REAL NOT NULL, condition CHAR(150));
CREATE TABLE years(date CHAR(15) PRIMARY KEY, position CHAR(100) NOT NULL, tempreature REAL NOT NULL, condition CHAR(150));
