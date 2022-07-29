CREATE DATABASE railwaytrain_db
USE railwaytrain_db
create table stops(stop_id INT PRIMARY KEY,
stop VARCHAR(50))

INSERT INTO stops VALUES 
('0','Trivandrum'),
('1','Alapuzha'),
('2','Ernakulam'),
('3','Kozhikkode');


CREATE TABLE trains(train_id INT PRIMARY KEY IDENTITY,
train_name VARCHAR(50),
end_id INT NOT NULL FOREIGN KEY REFERENCES stops(stop_id),
berth_filled INT NOT NULL,
wait_list_filled INT NOT NULL);

INSERT INTO trains(train_name, end_id, berth_filled,wait_list_filled) VALUES
('TVM_ALP','1','0','0'),
('TVM_ERN','2','0','0'),
('TVM_KZM','3','0','0');




CREATE TABLE passengerdetails(passenger_id INT PRIMARY KEY IDENTITY,
passenger_name VARCHAR(50) NOT NULL, 
stop_id INT FOREIGN KEY REFERENCES stops(stop_id),
train_id INT NOT NULL FOREIGN KEY REFERENCES trains(train_id))



CREATE TABLE waitlist(passenger_id INT PRIMARY KEY IDENTITY,
passenger_name VARCHAR(50) NOT NULL,
stop_id INT FOREIGN KEY REFERENCES stops(stop_id),
train_id INT NOT NULL FOREIGN KEY REFERENCES trains(train_id));

SELECT * FROM trains
SELECT * FROM stops
SELECT * FROM waitlist
SELECT * FROM passengerdetails
