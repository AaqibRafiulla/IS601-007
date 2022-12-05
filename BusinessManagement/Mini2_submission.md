<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Aaqib Rafiulla (ar2576)</td></tr>
<tr><td> <em>Generated: </em> 12/4/2022 7:38:02 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ar2576" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205509381-c0a4b066-be23-4b41-a31b-a6bc3b2c8f57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing DIAR-mt85 updated to DIAR-ar2576 and also added relevant href links<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205509605-4c9d1d64-b616-41c2-8d6c-f40353b79b70.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing app deployed from heroku dev and with the url<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205509701-b33f1a01-1c37-43a2-9e37-971c76010e74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing changes made to index.html file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205509857-a55e744d-b31d-452d-9f39-529e809b5a2d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>website having my ucid and brought to you by message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205510053-1baba71e-4916-4721-8710-0745eab968e1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing IS601_MP2_Companies table with records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205510108-c58b41d4-5c0a-4846-a092-048cb99b71cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing IS601_MP2_Employees table with records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205510219-b4d4ad1c-c383-4fc0-83ba-3d319afe8327.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing My ucid ar2576 or the DB name <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205510932-a204fbdd-3de5-42c2-bb62-e5fafd0e781c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing to check if it is csv file or not and return<br>a flash error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205510997-0a8266e6-00a3-43cc-bf40-7b0da30378e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing csv file should be read from the provided stream as dict,<br>extracted employee and company data appended to employee and company list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205511096-8a187c08-af57-45af-aa2c-1514f391fcf6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing flash message generated noting no of records processsed and also if<br>a list wasn&#39;t loaded or was empty<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205523934-abb83d72-a81f-46b8-aff8-d7d4dda8562a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the error message when it is not a .csv file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205511408-2cd33acc-c746-454f-88dc-b998c355e7d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing employee data having records uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205511457-1ea2b7e8-4519-4bc4-aad2-f65543ae5e1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing company data having records uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205511929-49d3827c-0da5-4c12-89ae-8c8e5ff82f29.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing /add route for employee having queries, last_name, email and with all<br>the flash messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512019-71f72759-c9db-4389-a1f5-0ff7f59edb91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing a user friendly message flashed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512473-4c0a0ff3-cb62-41f3-a365-ba3bc6e559fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing url visible from heroku dev and adding a new employee Mohan Kumar<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512568-1632eb0f-cff0-4c74-84a2-e1bd9fb74ce1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing employee Mohan kumar added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512712-cae8a064-9316-4346-b1b9-ef6a7b57e9ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing last name required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512843-d269a9aa-23ce-406a-876e-60e8af230803.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing first name required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512914-7c922187-19c9-47e8-9d1f-8c1e1d5e4e0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing email is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205512970-f21225d2-e57d-427e-ac77-ae8e93b3ffd8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing @ is required in email address<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205513134-b404bb31-f18d-4b27-b58b-3809b31ead12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the employees mohan_kumar , mike_tyson added to employee table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515246-ea2407dc-227b-4a64-8b70-1d969c42086c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the employee DB record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515287-c0172238-5edf-4ea1-98dc-a0718367caf9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the employee Mohan kumar added to employee DB record<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515400-c2ac3df6-92ed-485a-a176-9070cfccd884.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing the todo items from 1 to 7 i.e., till sorting if<br>column and order are provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515515-493ba59a-f468-4ee4-8096-4703becb8297.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for appending limit or limit greater than 10 and also to print<br>a flash user friendly message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515696-70c6dc69-d56a-477e-b7cc-cfa2e294d7aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515756-1411f63a-bfb6-4864-ba4e-22cd0359fa6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205515921-604b5d4b-d08f-42f0-847e-4242c8b62ca0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with email filter ending with .au<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205516035-3e7031e8-41fc-4d0b-b509-a10e70d57b3a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with company filter named Franklin, peter L Esq<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205519826-8135da23-a832-4a46-85f8-6a035dada7e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing ASC filter applied for column first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205519959-fde01432-6911-41e9-afbb-61bf191f1fa1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing DESC filter applied for column company name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205516825-3cc92617-885e-4596-be68-1f2cb2e656eb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing from requesting args id to email is required with a flash<br>error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205516905-e0e52502-bea8-4061-99f0-f03ccc2931dd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code showing SQL update query to passing the employee data to render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517025-dab03c4f-2c29-40a7-9518-e929eba9d885.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of employee data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517065-06ff4555-6cff-4061-bfa4-47905e1d6f79.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Made an edit to last name of first employee Amira<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517099-bc0ededa-0b42-46e1-b9da-5fcd43dba937.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the updated last name of employee Amira to khan<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205513134-b404bb31-f18d-4b27-b58b-3809b31ead12.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing DB before edit of employee Amira&#39;s Last name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517199-2c5153eb-6234-4064-96d0-cc82fbd84ba9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing DB after edit of employee Amira&#39;s last name to khan<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517490-0c36d0ac-ed7c-4818-94ba-80eb23087b08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for /add route of company from retrieving form data to flash error<br>message saying country is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517577-7dde2e28-8ca7-4986-b68b-b161c69e5fe9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code from website not required to printing a flash user friendly message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205517865-3d87fa41-9874-4680-9b27-a8f2fe1c11f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the companies in company directory<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518019-e79caec7-71fd-41e4-8787-856001f23fad.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding a company named Ravi to directory<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518099-ae1553cb-7ec5-420d-af92-4b57804c6d64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Adding without name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518141-b5c6a531-f644-46ba-a83c-74c86b6ad08c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing error for not adding name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518228-30cb4ee4-ee2f-4862-a305-52c76b6516b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing error for not adding address<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518298-b83b1fd9-5e8d-407d-82fe-0476367ea1e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing error for not adding city<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518403-ee2b72a7-1239-49e6-95ec-644bfb312f0c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error for not selecting country<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518557-8d00975c-6b1d-4ff1-a8fb-e74a2a3ce435.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error for not selecting state<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518628-412f05c6-6834-4fff-a4b6-a5108766a9d6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>url from heroku dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518705-d7fa3c33-0e70-44b2-bf3a-0284528f4cb1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the new company Ravi in the company DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205518774-db149747-d998-4f94-be67-5abdff3f979e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the new company Ravi in the website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205519287-bfe1eaad-3107-40e7-9769-9b9cd024dfa3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for /search route for company from using select query to retrieve company<br>data to sorting if column and order are provided<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205519416-415e6598-9cd6-42e6-996a-953d3641685d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code from todo 7 to todo 9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205520226-c8565304-1511-46b3-89ec-4c3e339d7462.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205520322-c2153d16-f443-4cc0-b1b2-843f3d72d497.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results for country &quot;United states&quot; after applying country filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205520414-956b4bda-49d1-4310-8c6d-1a5cd6173df5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results for state &quot;New York&quot; after applying state filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205520533-d7db1ae7-b61d-4348-97b4-6994ea36ce20.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results showing ASC filter applied for column &quot;name&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205520626-f8659b36-0f35-439a-8859-ca8b4f90a1b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results showing DESC filter applied for column &quot;State&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521144-d977d780-7b3c-42fa-bbba-e32e9af8fef5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code from retrieving form data of company to printing a flash message <br>&quot;country is required&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521278-025c764a-c2b0-4fd7-b6df-01a6ae7a5b27.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code from sql update query to passing company data to render template<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521585-6f5a7f51-a331-493e-abc0-5dcd5a9b3dd5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot before an edit in company directory<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521697-6d4c27ce-2eea-43b1-b115-34074f58baac.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Editing the address to &quot;477 liberty ave&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521868-5079dcf3-860b-48f6-986b-32f3ec516d3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the address updated in the company directory to &quot;477 liberty ave&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521638-2915da97-3f44-40fd-8051-dda3ab525452.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing company data in DB before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205521947-e68ee5a2-da91-496a-a7f2-0d8627c93f6d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing company data in DB after editing address to &quot;477 liberty ave&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522233-8ebd2f49-cbe3-4a79-81fd-00402c228e94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for delete route in employee DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522332-7970a26b-baa0-45c1-8f7b-92a2cc93927a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee Directory before deleting an employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522457-90964ae1-f8e5-47ae-a78d-899cea1cd427.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing employee Marica Tarbor deleted from employee directory<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522538-4be4160b-90a0-40fa-9410-4e569e12a108.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee directory after deleting employee named &quot;Marica Tarbor&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522637-db370575-4251-4237-9d04-5e2ca34c18b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code implemented for delete route of company according to todo list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522828-14e82f43-08e2-400a-9846-ec51e3d530d3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company Directory before deleting a company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205522920-d45f3974-c0a6-401e-8ca7-a7d3ddecc39f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>message showing Farmers insurance group deleted from company directory<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205523006-05edf41d-8676-4f67-8473-c18866d77e6c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company directory after deleting a company named &quot;Farmers Insurance Group&quot;<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205524597-dfa05fae-8598-476e-9c23-40c08f255f22.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases showing passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205524864-e4672c8c-3aa1-4583-a6ef-017292b54143.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Individual test cases showing passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205524916-d652de0c-12a6-4a6d-a11f-2b8e17947785.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Individual test cases showing passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/205525068-ffc68414-a53d-491f-8992-04fb926aebdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Individual test cases showing passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>The project was really interesting, as I got to learn a lot including<br>flask, html and few relevant technologies. I faced issues with some test cases<br>where adding a company was causing a problem then I tried to analyze<br>and made changes with my company.py file and finally could run all the<br>test cases. I also faced some minor issues with the database connection and<br>this project indeed helped me to learn a lot and get used with<br>the test cases files and also fixing the issues related to it. All<br>in all, it was a good experience with the project as I got<br>to learn how to connect flask to an sql database and also learnt<br>deploying the app to heroku.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-2-business-management/grade/ar2576" target="_blank">Grading</a></td></tr></table>