CRUD OPERATIONS :
In SQL-Sever, CRUD stands for CREATE,READ,UPDATE, and DELETE statements.

CREATE :You can add new rows to your table by using Create.

INSERT INTO `bike` VALUES (37402,'bajaj','cruiser',2468,10);
INSERT INTO `rents` VALUES (10,'guntur','vijayawada','18km');
INSERT INTO `shop` VALUES ('krishna',37402,12220,10);
INSERT INTO `user` VALUES (12220,'krishna',97864457,'krishna54@gmail.com','Aadhar');

UPDATE :

ALTER TABLE bike_rentals.bike ADD PRIMARY KEY(bike_number);
ALTER TABLE bike_rentals.rents ADD PRIMARY KEY(hrs);
ALTER TABLE bike_rentals.user ADD PRIMARY KEY(user_id);
ALTER TABLE bike_rentals.bike FOREIGN KEY (hrs) REFERENCES bike_rentals.rents(hrs);
ALTER TABLE bike_rentals.shop ADD FOREIGN KEY (car_number) REFERENCES bike_rentals.car(car_number);
ALTER TABLE bike_rentals.shop ADD FOREIGN KEY (user_id) REFERENCES bike_rentals.user(user_id);

DELETE :

DROP TABLE IF EXISTS `bike`;
DROP TABLE IF EXISTS `rents`;
DROP TABLE IF EXISTS `shop`;
DROP TABLE IF EXISTS `user`;

READ : Allows you to read values.

select Bike.*,Shop.*, Rents.*
                from bike_rentals.bike  Bike
                Join bike_rentals.shop Shop
                on Bike.bike_id = Shop.bike_id and Bike.bike_id={id}
                Join bike_rentals.rents Rents
                ON Rents.hrs = Shop.hrs and Shop.bike_id = {id};
