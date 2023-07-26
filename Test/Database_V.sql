CREATE TABLE users (
id int primary key,
username varchar (50) not null,
email varchar (100),
phonenumber varchar (15),
uservalid int(15)
);
CREATE TABLE products (
id int primary key,
name varchar(255) not null,
description varchar(255),
price DOUBLE(10, 2) not null,
quantity int not NULL,
);
CREATE TABLE transactions(
id int primary key,
product_id int not null,
date_time varchar(255) not null,
FOREIGN KEY (product_id) REFERENCES products(id)
);
CREATE TABLE accounts (
id int primary key,
password varchar(255) not null,
email varchar(255) not null,
);

