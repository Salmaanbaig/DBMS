CREATE TABLE bike_rentals.bike(
    bike_id int,
    bike_brand VARCHAR(50),
    bike_type VARCHAR(50),
    bike_price float,
    hrs int
); 
 CREATE TABLE bike_rentals.shop(
    user_name VARCHAR(50),
    bike_id INT,
    user_id INT,
    hrs INT
); 

 CREATE TABLE bike_rentals.user(
    user_id INT,
    user_name VARCHAR(50),
    contact_no INT,
    email_id VARCHAR(50),
    gov_proof VARCHAR(50)
); 

CREATE TABLE bike_rentals.rents(
    hrs INT,
    from_loc VARCHAR(50),
    to_loc VARCHAR(50),
    dist_cov VARCHAR(50)
);