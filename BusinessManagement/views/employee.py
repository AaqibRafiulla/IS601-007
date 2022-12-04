from flask import Blueprint, render_template, request, flash, redirect
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # Added SQL query to retrieve employee data using left join operator - Aaqib Rafiulla, ar2576, Nov 28, 2022
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name as company_name from IS601_MP2_Employees e
     LEFT JOIN IS601_MP2_Companies c ON e.company_id=c.id WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_list = [(v,v) for v in allowed_columns]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # Added code and print statement to search the employee'data from request args - Aaqib Rafiulla, ar2576, Nov 28,2022
    requestArgs = request.args.to_dict()
    print('Employee search request args:',requestArgs)
    # TODO search-3 append like filter for first_name if provided
    # Added code to append using like filter for first_name - Aaqib Rafiulla, ar2576, Nov 28,2022
    if requestArgs.get('first_name'):
        query+=" AND first_name like %s"
        args.append("%"+requestArgs.get('first_name')+"%")
    # TODO search-4 append like filter for last_name if provided
    # Added code to append using like filter for last_name - Aaqib Rafiulla, ar2576, Nov 28,2022
    if requestArgs.get('last_name'):
        query+=" AND last_name like %s"
        args.append("%"+requestArgs.get('last_name')+"%")
    # TODO search-5 append like filter for email if provided
    # Added code to append using like filter for email - Aaqib Rafiulla, ar2576, Nov 28,2022
    if requestArgs.get('email'):
        query+=" AND email like %s"
        args.append("%"+requestArgs.get('email')+"%")
    # TODO search-6 append equality filter for company_id if provided
    # Added code to append using equality filter for company_id - Aaqib Rafiulla, ar2576, Nov 28,2022
    if requestArgs.get('company'):
        query+=" AND company_id=%s"
        args.append(requestArgs.get('company'))
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # Added code to sort if column and order are provided and also within allowed column and allowed order options - Aaqib Rafiulla, ar2576, Nov 28,2022
    if requestArgs.get('column') and requestArgs.get('order') and (requestArgs.get('column') in allowed_columns):
        query+=" ORDER BY "+requestArgs.get('column') +" "+requestArgs.get('order')
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    # Added code to append limit (default 10) or limit greater than 1 and less than or equal to 100
    # and print an proper error message if limit isn't a number or if it's out of bounds - Aaqib Rafiulla, ar2576, Nov 28,2022
    
    if requestArgs.get('limit'):
        if int(requestArgs.get('limit'))>1 and int(requestArgs.get('limit'))<=100:
            query+=" limit "+requestArgs.get('limit')
        else:
            flash('Request Limit is invalid','danger')
    else:
        query+=" limit 10"
    
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
            print('The result of employee search:',rows)
    except Exception as e:
        # TODO search-10 make message user friendly
        # Added code to make message user friendly - Aaqib Rafiulla, ar2576, Nov 28,2022
        print('Error while fetching data:',e)
        flash('There was an error fetching the required data', "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_list=allowed_list)

@employee.route("/add", methods=["GET","POST"])
def add():
    print('Employee add',request.form.to_dict())
    if request.method == "POST":
        has_error = False
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # Added code to retrieve form data - Aaqib Rafiulla, ar2576, Nov 28,2022
        requestArgs = request.form.to_dict()
        # TODO add-2 first_name is required (flash proper error message)
        # Added code to get first_name and print flash error message - Aaqib Rafiulla, ar2576, Nov 28,2022
        if(not requestArgs.get('first_name')):
            flash('First name is required!','danger')
            has_error=True
        # TODO add-3 last_name is required (flash proper error message)
        # Added code to get last_name and print flash error message - Aaqib Rafiulla, ar2576, Nov 28,2022
        if(not requestArgs.get('last_name')):
            flash('Last name is required!','danger')
            has_error=True
        # TODO add-4 company (may be None)
        # Added code to check if company data is none - Aaqib Rafiulla, ar2576, Nov 28,2022
        if(not requestArgs.get('company')):
            requestArgs['company']=None
        # TODO add-5 email is required (flash proper error message)
        # Added code to get email and print flash error message - Aaqib Rafiulla, ar2576, Nov 28,2022
        if(not requestArgs.get('email')):
            flash('Email is required!','danger')
            has_error=True
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(company)s)
                """,
                requestArgs) # <-- TODO add-6 add query and add arguments
                # Added SQL query to insert data into employees and by adding arguments - Aaqib Rafiulla, ar2576, Nov 28,2022
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                # Added code to make message user friendly - Aaqib Rafiulla, ar2576, Nov 28,2022
                print('An error occurred while addding new Employee',e)
                flash('An error occurred while addding new Employee', "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    row = []
    employee_id = request.args.get('id')
    # TODO edit-1 request args id is required (flash proper error message)
    form_data = {}
    if employee_id: # TODO update this for TODO edit-1
        has_error = False
        if request.method == "POST":
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            # Added code to retrieve form data for fn,ln .... - Aaqib Rafiulla, ar2576, Nov 28,2022
            form_data= request.form.to_dict()
            # TODO edit-2 first_name is required (flash proper error message)
            # Added code to get first_name and print flash error message - Aaqib Rafiulla, ar2576, Nov 28,2022
            if not form_data.get('first_name'):
                flash('First name is required!','danger')
                has_error=True
            # TODO edit-3 last_name is required (flash proper error message)
            # Added code to get last_name and print flash error message - Aaqib Rafiulla, ar2576, Nov 28,2022
            if not form_data.get('last_name'):
                flash('Last name is required!','danger')
                has_error=True
            # TODO edit-4 company may be None
            # TODO edit-5 email is required (flash proper error message)
            # Added code to get email and print flash error message - Aaqib Rafiulla, ar2576, Nov 28,2022
            if not form_data.get('email'):
                flash('Email is required!','danger')
                has_error=True
            if(has_error):
                return render_template("edit_employee.html",row={},value=None)
            data = [form_data.get('first_name'), form_data.get('last_name'), form_data.get('company',None),\
                form_data.get('email',''),employee_id]
            print('The arguments for emplyee edit:',data)
            try:
                # TODO edit-6 fill in proper update query
                # Added an SQL query to update the records to employee - Aaqib Rafiulla, ar2576, Dec 3,2022
                result = DB.update("""
                UPDATE IS601_MP2_Employees SET first_name=%s, last_name=%s, 
                company_id=%s, email=%s WHERE id=%s
                """, *data)
                if result.status:
                    print('Updated result:',result)
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-7 make this user-friendly
                # Added code to make flash error message as user friendly - Aaqib Rafiulla, ar2576, Dec 3,2022
                print('Error updating employee record:',e)
                flash('There was an error updating the record. Please try again later', "danger")
        try:
            # TODO edit-8 fetch the updated data (including company_name)
            # company_name should be 'N/A' if the employee isn't assigned to a copany
            # Added query to fetch updated records and also to print message if the employee isn't assigned to a company - Aaqib Rafiulla, ar2576, Dec 3,2022
            result = DB.selectOne("""SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, c.name as company_name from IS601_MP2_Employees e
     LEFT JOIN IS601_MP2_Companies c ON e.company_id=c.id WHERE e.id=%s""", employee_id)
            if result.status:
                row = result.row
                print('Employee data fetched:',row)
        except Exception as e:
            # TODO edit-9 make this user-friendly
            # Added code to make it user friendly - Aaqib Rafiulla, ar2576, Dec 3,2022
            print('Error fetching employee data:',e)
            flash('There was an error fetching the data', "danger")
    # TODO edit-10 pass the employee data to the render template
    # Added code to pass the company data to render template - Aaqib Rafiulla, ar2576, Dec 3,2022
    return render_template("edit_employee.html", row=row, val=row.get('company_id',None))

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    employee_id = request.args.get('id')
    has_error = False
    if employee_id:
        try:
            result = DB.delete("DELETE FROM IS601_MP2_Employees where id=%s", employee_id)
        except Exception as e:
            flash('There was an error deleting the employee','danger')
            has_error=True
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # Added code to todo items for delete-1,2,3,4 - Aaqib Rafiulla, ar2576, Dec 3,2022
    if not has_error:
        flash('Employee deleted successfully','success')
        return redirect('/employee/search')
    