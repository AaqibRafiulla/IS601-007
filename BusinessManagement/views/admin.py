import io
from flask import Blueprint, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
from sql.db import DB
import re
import csv
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        # Added code to check if it's a .csv file or not- Aaqib Rafiulla, ar2576, Nov 28,2022
        if not re.search(r'.\.csv',file.filename):
            flash('Invalid file selected. Only CSV allowed','warning')
            return redirect(request.url)
        if file and secure_filename(file.filename):
            companies = []
            employees = []
            company_query = """
            INSERT INTO IS601_MP2_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE address = %(address)s, city = %(city)s, country=%(country)s, state=%(state)s, zip=%(zip)s, website=%(website)s 
            """
            employee_query = """
             INSERT INTO IS601_MP2_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = (SELECT id FROM IS601_MP2_Companies WHERE name = %(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)
            # TODO importcsv-2 read the csv file stream as a dict
            # Reading the csv file as dict- Aaqib Rafiulla,ar2576, Nov28,2022
            data_dict = csv.DictReader(stream,delimiter=',')
            for data in data_dict:
                # print(row) #example
                # TODO importcsv-3 extract company data and append to company list as a dict only with company data
                # Added the data of company to the company list- Aaqib Rafiulla,ar2576, Nov 28,2022
                if data["company_name"] and data["address"] and data["city"] and data["state"] and data["zip"] and data["web"]:
                    companies.append({'name': data['company_name'],'address':data['address'],'city':data['city'],\
                        'country':data['country'],'state':data['state'],'zip':data['zip'],'website':data['web']})

                # TODO importcsv-4 extract employee data and append to employee list as a dict only with employee data
                # Added the data of employee to the employee list- Aaqib Rafiulla,ar2576, Nov 28,2022
                if data["first_name"] and data["last_name"] and data["email"] and data["company_name"]:
                    employees.append({'first_name':data['first_name'],'last_name':data['last_name'],'email':data['email'],'company_name':data['company_name']})
                  
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    # Added flash message to display the number of companies inserted- Aaqib Rafiulla,ar2576, Nov 28,2022
                    flash('{} companies successfully inserted'.format(len(companies)), 'info')
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                # Added a flash message to display the number of companies loaded to the database- Aaqib Rafiulla,ar2576, Nov 28,2022
                #pass
                flash('There is no company data in the uploaded file','info')

            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    # Added a flash message to display the number of employees loaded to the database- Aaqib Rafiulla,ar2576, Nov28, 2022
                    flash('{} employees successfully inserted'.format(len(employees)), 'info')
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                 # TODO importcsv-8 display flash message (info) that no companies were loaded
                 #pass
                 # Added a flash message to display the number of employees loaded to the database- Aaqib Rafiulla,ar2576, Nov28, 2022
                 flash('There is no employee data in the uploaded file','info')
    return render_template("upload.html")
