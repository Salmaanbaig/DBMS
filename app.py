from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def fetch_data(bike_id="", shop="", user_id="", brand=""):
    
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = 'bike_rentals'
    )
    cursor = mydb.cursor()
    # get all the employee details
    if len(bike_id)>1:
        query = """
                select Bike.*,Shop.*, Rents.*

                from bike_rentals.bike  Bike

                Join bike_rentals.shop Shop
                on Bike.bike_id = Shop.bike_id and Bike.bike_id={id}
    
                Join bike_rentals.rents Rents
                ON Rents.hrs = Shop.hrs and Shop.bike_id = {id};

                """
        
        
        main_query = query.format(id=int(bike_id))
        cursor.execute(main_query)
        sequence = cursor.column_names
        main_data = tuple()
        for result in cursor:
            main_data+=result
        return(sequence, main_data)
        
"""
    
    # get all the employee salaries greater than given input
    if len(salary)>1:
        query = "select * from emp_salary where salary = "+str(salary)
        cursor.execute(query)
    


 
    # get the projects and managers
    if len(project)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)

    
    # get the project details where income is greater than given input
    if len(income)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)


    # get the employee data who deals with the project greater than the income given
    if len(project)>1 and len(income)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)



    # get the details of the employees with there projects based on the salary
    if len(salary)>1 and len(project)>1:
        query = "select * from emp_data where emp_id = "+str(data)
        cursor.execute(query)
"""


@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        bike_id = request.form['bike_id']
        shop = request.form['shop']
        project = request.form['user_id']
        brand = request.form['brand']
        headings, data = fetch_data(bike_id, shop, project, brand)
        return render_template("index.html", headings=headings, data=data)
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)
    