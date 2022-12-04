from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count for the company
    # don't do SELECT *
    # Added SQL query to retrieve company data - Aaqib Rafiulla, ar2576, Nov 30, 2022

    query = """
    SELECT id, name, address, city, country, state, zip, website FROM IS601_MP2_Companies WHERE 1=1
    """
    args = [] # <--- append values to replace %s placeholders
    print('The query params:',args)
    allowed_columns = ["name", "city", "country", "state"]
    allowed_list = [(v,v) for v in allowed_columns]
    # TODO search-2 get name, country, state, column, order, limit request args
    # Added code to get company records from request args - Aaqib Rafiulla, ar2576, Nov 30,2022
    requestArgs = request.args.to_dict()
    # TODO search-3 append a LIKE filter for name if provided
    # Added code to append using like filter for name - Aaqib Rafiulla, ar2576, Nov 30,2022
    if requestArgs.get('name'):
        query+=" AND name like %s"
        args.append("%"+requestArgs.get('name')+"%")
    # TODO search-4 append an equality filter for country if provided
    # Added code to append using equality filter for country - Aaqib Rafiulla, ar2576, Nov 30,2022
    if requestArgs.get('country'):
        query+=" AND country=%s"
        args.append(requestArgs.get('country'))
    # TODO search-5 append an equality filter for state if provided
    # Added code to append using equality filter for state - Aaqib Rafiulla, ar2576, Nov 30,2022
    if requestArgs.get('state'):
        query+=" AND state=%s"
        args.append(requestArgs.get('state'))
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # Added code to sort if column and order are provided and also within allowed column and allowed order asc, desc - Aaqib Rafiulla, ar2576, Nov 30,2022
    if requestArgs.get('column') and requestArgs.get('order') and (requestArgs.get('column') in allowed_columns):
        query+=" ORDER BY "+requestArgs.get('column') +" "+requestArgs.get('order')
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    # Added code to append limit (default 10) or limit greater than 1 and less than or equal to 100
    # and print an proper error message if limit isn't a number or if it's out of bounds - Aaqib Rafiulla, ar2576, Nov 30,2022
    
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
            print('The result of Company search:',rows)
    except Exception as e:
        # TODO search-9 make message user friendly
        # Added code to make message user friendly - Aaqib Rafiulla, ar2576, Nov 30,2022
        print('Error while fetching data:',e)
        flash('There was an error fetching the required data', "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_companies.html", rows=rows, allowed_list=allowed_list)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
         # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
         # Added code to retrieve form data - Aaqib Rafiulla, ar2576, Dec 1,2022
        requestArgs = request.form.to_dict()
        print('The request agrs for Add company:',requestArgs)
        # TODO add-2 name is required (flash proper error message)
        # Added code to get name and print flash error message - Aaqib Rafiulla, ar2576, Dec 1,2022
        if(not requestArgs.get('name')):
            flash('Name is required!','danger')
            has_error=True
        # TODO add-3 address is required (flash proper error message)
        # Added code to get address and print flash error message - Aaqib Rafiulla, ar2576, Dec 1,2022
        if(not requestArgs.get('address')):
            flash('Address is required!','danger')
            has_error=True
        # TODO add-4 city is required (flash proper error message)
        # Added code to get city and print flash error message - Aaqib Rafiulla, ar2576, Dec 1,2022
        if(not requestArgs.get('city')):
            flash('City is required!','danger')
            has_error=True
        # TODO add-5 state is required (flash proper error message)
        # Added code to get city and print flash error message - Aaqib Rafiulla, ar2576, Dec 1,2022
        if(not requestArgs.get('state')):
            flash('City is required!','danger')
            has_error=True
        # TODO add-6 country is required (flash proper error message)
        # Added code to get country and print flash error message - Aaqib Rafiulla, ar2576, Dec 1,2022
        if(not requestArgs.get('country')):
            flash('Country is required!','danger')
            has_error=True
        # TODO add-7 website is not required

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP2_Companies (name, address, city, zip, country, state, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(zip)s ,%(country)s, %(state)s, %(website)s)
                """, requestArgs) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                # Added code to print a flash message to look like user friendly - Aaqib Rafiulla, ar2576, Dec 1,2022
                print('An error occurred while adding an employee',e)
                flash('An error occurred while adding an employee', "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    has_error = False
    row=[]
    company_id = request.args.get('id')
    if company_id: # TODO update this for TODO edit-1
        if request.method == "POST":
            # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
            # Added code to retrieve form data for name, address .... - Aaqib Rafiulla, ar2576, Dec 2,2022
            formData = request.form.to_dict()
            # TODO edit-3 name is required (flash proper error message)
            # Added code to get name and print flash error message - Aaqib Rafiulla, ar2576, Dec 2,2022
            if not formData.get('name'):
                flash('Name is required!','danger')
                has_error=True
            # TODO edit-4 address is required (flash proper error message)
            # Added code to get address and print flash error message - Aaqib Rafiulla, ar2576, Dec 2,2022
            if not formData.get('address'):
                flash('Address is required!','danger')
                has_error=True
            # TODO edit-5 city is required (flash proper error message)
            # Added code to get city and print flash error message - Aaqib Rafiulla, ar2576, Dec 2,2022
            if not formData.get('city'):
                flash('City is required!','danger')
                has_error=True
            # TODO edit-6 state is required (flash proper error message)
            # Added code to get state and print flash error message - Aaqib Rafiulla, ar2576, Dec 2,2022
            if not formData.get('state'):
                flash('State is required!','danger')
                has_error=True
            # TODO edit-7 country is required (flash proper error message)
            # Added code to get country and print flash error message - Aaqib Rafiulla, ar2576, Dec 2,2022
            if not formData.get('country'):
                flash('Country is required!','danger')
                has_error=True
            # TODO edit-8 website is not required
            # 
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            data = [formData.get('name',''), formData.get('address',''), formData.get('city',''),\
                 formData.get('state',''), formData.get('country',''), formData.get('zip',''), formData.get('website','')]
            data.append(company_id)
            try:
                # TODO edit-9 fill in proper update query
                # Added an SQL query to update the records to employee - Aaqib Rafiulla, ar2576, Dec 2,2022
                result = DB.update("""
                UPDATE IS601_MP2_Companies SET name=%s, address=%s, city=%s, state=%s,
                country=%s, zip=%s, website=%s WHERE id=%s
                """, *data)
                if result.status:
                    flash("Updated record", "success")
            except Exception as e:
                # TODO edit-10 make this user-friendly
                # Added code to print a flash message like user friendly - Aaqib Rafiulla, ar2576, Dec 2, 2022
                print('An error occurred during updation of company',e)
                flash('An error occurred during updation of company', "danger")
        try:
            # TODO edit-11 fetch the updated data
            # Added query to fetch updated data from company - Aaqib Rafiulla, ar2576, Dec 2,2022
            result = DB.selectOne("SELECT name, address, city, state, country, zip, website FROM IS601_MP2_Companies WHERE id=%s", company_id)
            if result.status:
                row = result.row
                print('The company data read:',row)
        except Exception as e:
            # TODO edit-12 make this user-friendly
            # Added code  to print flash error message as user friendly - Aaqib Rafiulla, ar2576, Dec 3,2022
            print('An error occurred while fetching company data',e)
            flash('An error occurred while fetching company data', "danger")
    # TODO edit-13 pass the company data to the render template
    # Added code to pass the company data to render template - Aaqib Rafiulla, ar2576, Dec 3,2022
    return render_template("edit_company.html", row=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees)
    # Added code to delete company by uid - Aaqib Rafiulla, ar2576, Dec 3,2022
    company_id = request.args.get('id')
    has_error = False
    if company_id:
        try:
            result = DB.selectAll('SELECT id FROM IS601_MP2_Companies WHERE name=%s','N/A')
            if not result.rows:
                result = DB.insertOne("""INSERT INTO IS601_MP2_Companies (name, address, city, country, state, website)
                        VALUES ('N/A','N/A','N/A','N/A','N/A','N/A')""")
            result = DB.selectAll('SELECT id FROM IS601_MP2_Companies WHERE name=%s','N/A')
            DB.update("""UPDATE IS601_MP2_Employees SET company_id=%s WHERE company_id=%s""",*[result.rows[0]['id'],company_id])
            delete_ = DB.delete("DELETE FROM IS601_MP2_Companies where id=%s", company_id)
        except Exception as e:
            print('An error occurred while deleting the company',e)
            flash('An error occurred while deleting the company','danger')
            has_error=True
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # Added code to todo items for delete-2,3,4 - Aaqib Rafiulla, ar2576, Dec 3,2022
    if not has_error:
        flash('Successfully deleted the company','success')
    return redirect('/company/search')
   