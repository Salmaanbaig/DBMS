Table Name : bike_rentals_bike.sql
bike_rentals_bike.sql contains five fields, (bike_id,bike_brand,bike_type,bike_price,hrs)
This table gives  idea about bike features. Example if we know the bike id we can determine the brand of the bike and type it belongs to.
bike_id here will accepts the integer values as it is described as INT datatype.
bike_brand here will accepts the String/Char values as it is described as CHAR datatype.
bike_type here will accepts the Character values as it is described as CHAR datatype.
bike_price here will accepts the integer values as it is described as INT datatype.
hrs here will accepts the integer values as it is described as INT datatype.

PRIMARY KEYS:
 bike_id,bike_brand together here is the primary key. As they together uniquly identifies the all rows of the bike_rentals_bike.sql.

FUNCTIONAL DEPENDENCIES:
bike_id --> bike_brand
bike_brand --> bike_type
bike_brand --> bike_price
bike_id -->hrs

Check whether the table in 3NF:
Here bike_id and bike_brand together forms a key.
so,left hand side is a key, there is no violation for 3NF.Since, no violation for 3NF, the table is in 3NF form.

SAMPLE DATA:
bike_id,bike_brand,bike_type,bike_price,hrs
37402,'bajaj','cruiser',2468,10

Table Name : bike_rentals_rents.sql
bike_rentals_rents.sql contains five fields, (hrs,from_loc,to_loc,dist_cov)
This tables gives idea about bike rents. Example if we know the from_loc and to_loc we can determine the dist_cov and hrs.
hrs here will accepts the integer valves as it is described as INT datatype.
from_loc here will accepts the character values as it is described as CHAR datatype
to_loc here will accepts the character values as it is described as CHAR datatype
dist_cov here will accepts the character values as it is described as CHAR datatype.

PRIMARY KEYS:
dis_cov is the primary key. As we know the dis_cov it will uniquely identify all the rows of the bike_rentals_bike.sql.


FUNCTIONAL DEPENDENCIES:
dis_cov --> from_loc
dist_cov --> to_loc
dist_cov --> hrs

check whether the table in 3NF:
Here dis_cov is the only key and that lays on left hand side of each and every FD. So there is no violation for 3NF


SAMPLE DATA:
hrs,from_loc,to_loc,dist_cov
10,'guntur','vijayawada','18km'

Table Name : bike_rentals_shop.sql
bike_rentals1_shop.sql contains four fields, (user_name,bike_id,user_id,hrs)
This table gives idea about customer spent hrs on the bike. For example if we know the bike_id here we can determine the hrs
he spent on the bike.
user_name here will accepts the character values as it is described as CHAR datatype.
bike_id here will accepts the integer values as it is described as INT datatype.
user_id here will accepts the interger values as it is described as INT datatype.
hrs here will accepts the integer values as it is described as INT datatype.

PRIMARY KEYS:
Here user_name is the Primary Key. If we know the User_name we can uniquely identify the all rows of the table.

FUNCTIONAL DEPENDENCIES:
user_name --> bike_id
user_name --> user_id
user_name --> hrs

Check whether the table in 3NF:
Here user_name is the only key and it lays on left hand of the FD's. So, it is in the 3NF.

SAMPLE DATA:
'krishna',37402,12220,10

Table Name : bike_rentals_user.sql
bike_rentals_user.sql contains five feilds,(user_id, user_name,contact_no,email_id,gov_proof)
This table gives idea about customer details. For example if we know the user_id we can get all the information about the customer.
user_id here will accept only the integer values as it is described as INT datatype.
user_name here will accept only the character values as it is decribes as CHAR datatype.
contact_no here will accept only the integer values as it is described as INT datatype.
email_id here will accept only the character values as it is described as CHAR datatype.
gov_proof here will accept only the character values as it is described as CHAR datatype.

PRIMARY KEYS:
user_id,user_name together here is the primary key. If we know the user_id and user_name we can determine the all other rows.

FUNCTIONAL DEPENDENCIES:
user_id --> user_name
user_id --> contact_no
user_name --> email_id
user_id --> gov_proof

Check Whether the table in 3NF:
here user_id and user_name together is the key. Here left hand side of FD's are keys. So, there is violation of 3NF.

SAMPLE DATA:
12220,'krishna',97864457,'krishna54@gmail.com','Aadhar'
