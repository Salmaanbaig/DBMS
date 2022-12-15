
INSERT INTO bike_rentals.bike(bike_id, bike_brand, bike_type, bike_price, hrs) VALUES (37402, "bajaj", "cruiser", 2468, 10);
INSERT INTO bike_rentals.bike(bike_id, bike_brand, bike_type, bike_price, hrs) VALUES (37404, "honda", "touring", 9999, 24);
INSERT INTO bike_rentals.bike(bike_id, bike_brand, bike_type, bike_price, hrs) VALUES (37406, "KTM", "dual sport", 3668, 17);
INSERT INTO bike_rentals.bike(bike_id, bike_brand, bike_type, bike_price, hrs) VALUES (37408, "aprillia", "cafe racer", 8630, 12);
INSERT INTO bike_rentals.bike(bike_id, bike_brand, bike_type, bike_price, hrs) VALUES (37500, "royal enfield", "chopper", 6490, 14);



INSERT INTO bike_rentals.shop(user_name, bike_id, user_id, hrs) VALUES ("krishna", 37402, 12220, 10);
INSERT INTO bike_rentals.shop(user_name, bike_id, user_id, hrs) VALUES ("pavan", 37404, 12221, 24);
INSERT INTO bike_rentals.shop(user_name, bike_id, user_id, hrs) VALUES ("kiran", 37406, 12222, 17);
INSERT INTO bike_rentals.shop(user_name, bike_id, user_id, hrs) VALUES ("vamshi", 37408, 12223, 12);
INSERT INTO bike_rentals.shop(user_name, bike_id, user_id, hrs) VALUES ("srinu", 37500, 12224, 14);



INSERT INTO bike_rentals.user(user_id, user_name, contact_no, email_id, gov_proof) VALUES (12220, "krishna", 97864457, "krishna54@gmail.com", "Aadhar");
INSERT INTO bike_rentals.user(user_id, user_name, contact_no, email_id, gov_proof) VALUES (12221, "pavan", 9557757, "pavan987@gmail.com", "Voter");
INSERT INTO bike_rentals.user(user_id, user_name, contact_no, email_id, gov_proof) VALUES (12222, "kiran", 84866517, "kiran18@gmail.com", "PAN");
INSERT INTO bike_rentals.user(user_id, user_name, contact_no, email_id, gov_proof) VALUES (12223, "vamshi", 80862357, "vamshi458@gmail.com", "License");
INSERT INTO bike_rentals.user(user_id, user_name, contact_no, email_id, gov_proof) VALUES (12224, "srinu", 97340062, "srinu234@gmail.com", "Passport");



INSERT INTO bike_rentals.rents(hrs, from_loc, to_loc, dist_cov) VALUES (10, "guntur", "vijayawada", "18km");
INSERT INTO bike_rentals.rents(hrs, from_loc, to_loc, dist_cov) VALUES (24, "vizag", "maharashtra", "56km");
INSERT INTO bike_rentals.rents(hrs, from_loc, to_loc, dist_cov) VALUES (17, "hyderabad", "srisailam", "12km");
INSERT INTO bike_rentals.rents(hrs, from_loc, to_loc, dist_cov) VALUES (12, "cheerala", "Amaravathi", "42km");
INSERT INTO bike_rentals.rents(hrs, from_loc, to_loc, dist_cov) VALUES (14, "hyderabd", "thirupathi", "23km");

