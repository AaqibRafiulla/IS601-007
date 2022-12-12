<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Aaqib Rafiulla (ar2576)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2022 10:04:05 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ar2576" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206928874-09a0381c-50ab-4dbe-95be-0fd3994c9078.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing invalid email address<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206928961-3a057bad-2b0f-48e7-ab35-621e6b08163d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206929081-c8fe0c02-54cd-4004-9be3-67cef13eda94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206929219-3ad6eb09-058e-40ce-b0f7-092960e91ec9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing email not available or already been used<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206929366-5a3b3d2b-6adf-4512-a9bf-fd178d8e6b43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206929449-d2cbfdc9-b5bf-4fb5-9e7b-0c776e9cb586.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the form filled with all the required details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206929548-8c44d36b-3e47-43b7-80b2-68ae99487253.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the users table with data from task 1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In this basically we are using flask&#39;s library and wtf forms which helps<br>in creation of forms with validation and rendering of forms. The wtf forms<br>is combined with bootstrap which has a presentable and responsive display of the<br>form fields which we have defined. Before submitting the forms , the data<br>is validated to ensure it matches all the required fields and if not<br>an error is thrown at the respective field. Wtf forms verifies the user<br>input in the front end using the validators such as input type, length<br>of characters and if the input matches , the data is submitted to<br>the backend and it further evaluates to check whether the username and and<br>email have previously been registered or not.<div>The user enters the password and then<br>it verifies if it matches with the confirm password, after which the data<br>is submitted to the backend and then it validates.</div><div>The database contains user&#39;s records<br>or data which can be retrieved when required and the same data can<br>either be deleted or updated, and each user is assigned with a unique<br>id.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206931509-594eba3b-c9e2-40a5-8b96-c9db93e09878.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing password mismatch while logging in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206931573-5be314e8-8572-4d53-ac14-f0f96630bd5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing successful login of user ac2345<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>In this basically we are using flask&#39;s library and wtf forms which helps<br>in creation of forms with validation and rendering of forms. The wtf forms<br>is combined with bootstrap which has a presentable and responsive display of the<br>form fields which we have defined. Before submitting the forms , the data<br>is validated to ensure it matches all the required fields and if not<br>an error is thrown at the respective field. Wtf forms verifies the user<br>input in the front end using the validators such as input type, length<br>of characters and if the input matches , the data is submitted to<br>the backend and it further evaluates to check whether the username and and<br>email have previously been registered or not.<div>The user enters the password and then<br>it verifies if it matches with the confirm password, after which the data<br>is submitted to the backend and then it validates.</div><div>The database contains user&#39;s records<br>or data which can be retrieved when required and the same data can<br>either be deleted or updated, and each user is assigned with a unique<br>id.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206931879-60e7bee2-b056-410e-8598-08bee4edba5b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing logout successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206932293-966c39b5-a743-461d-9601-3c8e04922437.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User denied from logging in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Firstly, we check if the user is logged in or not, if the<br>session does not have any user data it means the user is not<br>logged in and he cannot perform any further actions and displays that the<br>permission is denied to login for that user. If he is able to<br>login then it displays a flash message showing successfully registered.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206932293-966c39b5-a743-461d-9601-3c8e04922437.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing user denied from logging in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206932636-bafcd2b7-602e-4b56-a7ae-32a93983fae4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user cannot access the role page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206934461-01021aaf-43c2-476d-a0aa-5bccfb6a329e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with records<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206934549-0497ef60-0499-41f0-893d-b1e1a5aaac98.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UserRoles table with data and the admin user is the one having user_id<br>1<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>Firstly, we check if the user is logged in or not, if the<br>session does not have any user data it means the user is not<br>logged in and he cannot perform any further actions and displays that the<br>permission is denied to login for that user. If he is able to<br>login then it displays a flash message showing successfully registered.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>For the role-protected pages, the application works in a such a way that<br>only the user defined as admin is able to add, list and assign<br>roles and a regular user will not able to see the roles tab<br>in the application. For the add function, a new role is directly added<br>directly into the database as an SQL query .<div>Similarly, for the edit function<br>the user that is predefined as an admin who wants to edit a<br>role , the form.validate_on_submit() checks if that user is an admin.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935533-c5261c7d-2e80-4c82-841a-729e498d70b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Home page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935585-0f8cf498-99d9-4043-8e33-48616805110f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935630-f29fd849-400f-4f5b-a8ba-917bc5ed955e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add sample page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935757-b345f6d5-a600-4407-a10a-ea36b2b8e7e6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>list sample page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935815-d94c8f23-bbd6-4c67-99a5-ffb6454db680.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add roles page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935859-4de41154-64e1-40fc-9146-66f2cdf75cc9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>list roles page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206935927-cb8c29b9-1df2-487c-a89f-068ca49cf13b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>assign roles page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206936118-f6d24236-cc7f-4675-bda9-dae29ffe1ea4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful logout of user admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>In this generally we are using bootstrap for styling of the website, and<br>CSS is used to set the color of the nav bar and also<br>set the size and spacing of the elements.<div>The nav background and the text<br>color is set to white. The form input fields are designed with a<br>border and the corners have a radius.</div><div>The class attributes are used to assign<br>specific styling to elements.<br><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206932636-bafcd2b7-602e-4b56-a7ae-32a93983fae4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing access denied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206931509-594eba3b-c9e2-40a5-8b96-c9db93e09878.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206929219-3ad6eb09-058e-40ce-b0f7-092960e91ec9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User name not available error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>The messages are highlighted with a color reflecting the type of the error,<br>like the green color shows that login or logout is successful. The messages<br>are basically formatted in a friendly manner in the backend before sending it<br>to the frontend. The messages shown are short and concise for the user<br>to easily understand.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206936853-6d4ed5fa-d06f-4d14-a231-6ae28bfa1580.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the user profile page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>The user&#39;s profile is retrieved from the DB by matching the user id,<br>if the same matching user id is found in the DB the information<br>is prefilled in the profile form.<div>The form is then sent to the template<br>for displaying the username and email filled in.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206938262-42c12314-da1b-49c3-a7e7-2bc377b8990e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile updated successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206938361-3107165b-1452-4229-bd9f-23688d2068a6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206938521-8f0dc700-156e-487a-8cfa-5813859d7550.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username required message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206938663-36c28121-8463-41f1-b47c-ee9f15aa5dbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206939042-0ce29d88-3773-4968-88e6-a9cce8db9ba9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing invalid email format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206939190-0ce5e740-59fb-4967-9dc1-3c2ee88a7fbe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing username not available or already in use<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206939281-7449a879-2c1d-4414-b204-980cbd3aeafb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing email not available or already in use<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206944694-7a54982b-f813-49fc-ac8e-cbf5d12cdfca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile before updating for user aaqib_1&#39;s email<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206944870-459927e2-0531-4eb6-9d51-28e4df75b082.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile before updating for user aaqib_1&#39;s email in DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206945293-4e33f84c-01e6-446c-b1c3-dcd3c7be7efc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile after updating email to <a href="mailto:&#x61;&#97;&#113;&#105;&#x62;&#x5f;&#49;&#64;&#x67;&#x6d;&#x61;&#x69;&#x6c;&#x2e;&#x63;&#111;&#x6d;">&#x61;&#97;&#113;&#105;&#x62;&#x5f;&#49;&#64;&#x67;&#x6d;&#x61;&#x69;&#x6c;&#x2e;&#x63;&#111;&#x6d;</a><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/206945415-6b7941b9-09bf-491e-ac82-fd5644eb78d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile after updating email to <a href="mailto:&#97;&#97;&#x71;&#105;&#x62;&#x5f;&#49;&#x40;&#x67;&#x6d;&#97;&#x69;&#x6c;&#46;&#99;&#111;&#109;">&#97;&#97;&#x71;&#105;&#x62;&#x5f;&#49;&#x40;&#x67;&#x6d;&#97;&#x69;&#x6c;&#46;&#99;&#111;&#109;</a> in DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/22">https://github.com/AaqibRafiulla/IS601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>The user can update both username and email accordingly and the password update<br>is mandatory. So, in order to update the password you have to fill<br>the entries i.e., current password, new password and confirm password as shown in<br>the screenshots. Before the password is updated , we need to make sure<br>both the email and username is not duplicated and also if current password<br>is valid , the new password and confirm new password is verified to<br>ensure they match and are of the same or required length.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>I had issues while deploying my application to heroku, and it showed an<br>application error and I went through the logs to verify the error then<br>I got to know that my project folder has subfolders inside it and<br>this is causing the application to not deploy in heroku. Then I made<br>the required changes and finally the application got deployed to heroku. I learnt<br>the working of the wtf forms and using flask&#39;s libraries which makes the<br>forms flexible and also how bootstrap gives a presentable and responsive display of<br>the form.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms1.herokuapp.com/login">https://is601-ar2576-prod-ms1.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone1-deliverable/grade/ar2576" target="_blank">Grading</a></td></tr></table>