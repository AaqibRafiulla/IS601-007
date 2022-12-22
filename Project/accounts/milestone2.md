<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Aaqib Rafiulla (ar2576)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 6:09:41 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ar2576" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208772087-d7080dd3-bd9a-49ea-a312-e0954a413857.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of admin create item page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208772857-532c683a-293e-4daf-9138-6f78118e7caa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing item created with details filled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208773538-7a72ee5b-faff-4bca-bc6c-c21efba4e952.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>New item created showing up in item list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208775536-84f5db2b-db44-45ca-b18d-df088c057ba5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the products details with columns in the DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208775993-6175f87b-6322-4cbe-a424-6b01d82f045d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the product details with columns in the app<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>For adding products from UI to the database, a Flask form is created<br>which has details like item_id which is a hidden field , name, stock,<br>description, cost, image. A route also is added to navigate to the product<br>page&nbsp; and also a function named item was created which collects the data<br>submitted to the form. The validate_on submit() function is used to record the<br>values submitted by the user and these values are used in the sql<br>update query which then updates the product details to the backend. For the<br>layout of product page, bootstrap is used which is also added to the<br>HTML page of nav bar.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208777733-de29ccc3-5ba8-4fb9-b7df-907af5718d38.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the products on the shop page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208779154-42905c10-9ac3-498a-99a1-357b619bc0b4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing login successful<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208780055-fbb33178-8acf-4fe1-976b-5366dc3a2f54.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item increase quantity filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208780316-7dc85663-1fc4-42d3-82ba-8dc3218eb48e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item decrease quantity filter<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>If a user wants to view the items in the shop, a shop_list<br>function is created where the selectAll query is used to select all the<br>items that are in the items table added by the user. An empty<br>list named rows is first initialized and the selectAll query is written in<br>try-except block. So, if the query executes successfully , the result gets appended<br>to the rows list. If there is an error in selecting items a<br>flash message is used to alert the user that &quot;There was an error<br>in fetching the items&quot;. A route is added to access the shop items<br>and also a login is required was added before the function so that<br>only logged-in users can access the list of items from the shop. The<br>user can also increase or decrease the quantity before adding the items to<br>the cart.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208784467-355681c3-33fb-492b-8560-9a5e0ee4e949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged in as admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208784805-32713baf-12f1-4362-8e14-3e0c83f05080.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item list page having admin in the url<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208785028-e8477b6f-4306-412a-8b64-17ac2e1deadf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Items list page with view, edit and delete filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208785417-b23b5da3-8770-4616-85ce-c1ce6d760524.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Stock updated to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208785523-a5876435-01e6-45ce-92b2-f3c3ff6a38e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>iPhone 14 pro max not visible in the shop page after setting it<br>to 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208785670-8c3e0215-9b44-407a-8cf5-3142707ba154.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>iPhone 14 pro max visible in the item list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>For the admin to view, create, delete and edit items from the items<br>page, a function item is created which references to the item form which<br>is created in forms.py. A route is added to navigate to the shop<br>or item page using GET and POST methods. The admin logic is added<br>by using the @admin_permission .require(http_exception=403). With this if the admin is not logged<br>in and the user tries to navigate to the products page, the application<br>will display the 403 page. The form.validate_on_submit() function is used to collect data<br>from the admin or user when the form is submitted. To update the<br>products that already exists, an update query was used to update the items<br>in the database and to delete the items, delete was created that had<br>the route with GET and POST methods. The function request.args.get(&quot;id) was used to<br>collect the item id from the user.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208786100-0c58216e-898b-493a-aaf1-547dbcddee4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the edit button in the admin item list page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208786582-f3989cd2-0ac8-4415-9127-912623310291.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Item list page from admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208787119-5e138f39-ee52-476e-884c-ce7e64f533a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit item page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208787741-f9ebe720-ebb0-4597-8b7d-66b2a66bee91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing the cost of oven to 150<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208788001-c7ffa1c4-e439-4868-9324-aeefec835f66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated the price of oven to 150<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208788092-0ed91147-310b-41b2-a28a-d1d20f2b6869.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the updated cost of oven in item list page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>To edit the items from the products page for the admin, the flask<br>form itemform was created and this function uses GET and POST methods in<br>the route. The form.validate_on_submit() function is used to validate the data submitted which<br>is submitted by user/admin. To make edits to the item page, the DB.update<br>function is used to update the query. The query uses the user inputs<br>from the form to update the products table, and so if the update<br>is successful it displays a flash message saying update items in cart, if<br>there is an error it displays a danger flash message.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>(missing)</p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208789623-b7a0c53b-e0b0-4e1f-b848-cb7238585503.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message showing belt added to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208789875-c828316a-2fa1-487f-8bf6-247ba4932c6b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message showing while adding item to the cart when not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208790115-5abd64d5-52c8-45cf-b1ad-99a3539e7c3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing cart table with all the items added<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208790239-4f4ff22d-f844-4b37-9d8b-aca349d4bb7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing cart table with all the items added from DB<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>A route with GET and POST methods is used to navigate the cart<br>tab in the application, user login is validated by adding @login_required. So, if<br>a user is not logged in will not be able to access the<br>cart. The request.form.get() function was used to collect information about the products from<br>the user such as quantity and item id of the product. For the<br>front-end , a cart.html file is created which has the table heading tags<br>of product, quantity, subtotal and actions.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>In this, the user_id of the logged in user is collected with the<br>current_user.get_id() function. if the quantity selected is greater than 0, the cost and<br>name of the product is selected from the database with the SELECT query.<br>The items in the cart are updated with update query which has the<br>id, quantity, and cost from from the result of previous select query. If<br>the update query executes successfully then a flash message is displayed else if<br>not it will throw an error and the user cannot update the cart.<br>If an item is not added to the cart, then an INSERT query<br>is used on the cart table to insert the values such as id,<br>quantity, cost which is retrieved from the previous query.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208790925-ba54f6fa-775c-411b-8950-f2dfe2e5a8a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing new item added in the cart with total based on the quantity<br>and price<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208792268-8ade057d-eda6-4aa6-a487-3a52b861b859.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208792669-ed6003a4-66a5-4c47-8302-b6484f84b8b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing more items added to cart with updated total cost<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>The cart function has the login required which says that only logged-in users<br>can access the cart. A select query is used to get the cart_id,<br>item_id, name , quantity, stock, cost and (quantity*cost) is used in the query<br>to get the subtotal cost of the items. The cart table is joined<br>with the items table using the JOIN condition cart.itemid = item.itemid. The result.rows<br>method is used to display each cart item with the subtotals as rows.<br>The totall variable is the total cost of the cart for each subitem.<br>If there are no errors and exceptions in the query, then the logged<br>in user will be able to view the subtotal for each item and<br>total cost for each item.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208801883-b2b35fec-651b-4218-8f54-4335c94dbb3f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart quantity added by a user before update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208802084-30b6cd6f-6a95-4389-991b-7c82d6a9e17b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updating the quantity of winter jacket to 4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208802450-978fcec0-7cf0-44d9-9a2e-c8e8ebc7d4a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated quantity of shoes from 1 to 5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208803947-fd60599e-2387-4ae4-904d-bd1c41b6c896.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the quantity of Nike Air jordan shoes before 0<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208805110-5a8fdfbc-3bca-4429-aca6-d0e13b0dbe28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after setting the quantity and updating to 0, the item gets deleted from<br>the cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208805349-be8fa70a-ccd3-4fe2-af4d-a57dff5c3f84.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before setting the quantity of TV to -1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208805531-31806ba1-b3c8-4823-b988-fa3228768a32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>after setting quantity to -1, the item gets deleted from cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>If the quantity selected is greater than 0, the cost and name of<br>the product is selected from the database with the SELECT query. The items<br>in the cart are updated with update query which has the id, quantity,<br>and cost from from the result of previous select query. Similarly if the<br>quantity selected is less than 0 or negative, a delete query is used<br>to delete the item selected from the cart. So, if the delete query<br>executes, then it displays a flash message saying item is deleted from the<br>cart.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208806805-9ac4dfce-11cc-4b1f-bf86-bf37749a95d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deleting item dell laptop from cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208806932-048f3b95-3435-47ef-a488-63b1b028d25d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After deleting laptop from cart and the cart value or the total cost<br>gets updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208807647-e1b3bd6d-a95e-411c-a1a4-9a625171a611.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart page before clearing the cart item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/208807942-7dafd1d5-1920-41db-8186-6603db54c938.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the cart page after clearing all the items and the balance gets<br>updated to 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>If the quantity selected is less than 0 or negative, a delete query<br>is used to delete the item selected from the cart. So, if the<br>delete query executes, then it displays a flash message saying item is deleted<br>from the cart. The item is deleted based on the item id and<br>user id. If there is an error or exception, then it displays a<br>warning flash message to the user.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/24">https://github.com/AaqibRafiulla/IS601-007/pull/24</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Initially I had issues with my requirements file not installing, so I had<br>to upgrade it and also there was issue with deploying the application to<br>heroku, and I found that there were sub-folders inside my project folder which<br>was causing my app to not deploy and then it got deployed to<br>heroku. There was also an issue with my database tables as it was<br>not updating the records. I learnt how the queries were used to handle<br>the database and perform the operations such as delete, update and also learnt<br>how the functions were used to record the values of the user and<br>these values were then used in the SQL queries or statements which directly<br>updates the details in the database after the query executes successfully. I also<br>learnt on how the permissions for the admin and user was validated using<br>the functions.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-ar2576-prod-ms2.herokuapp.com/login">https://is601-ar2576-prod-ms2.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-milestone-2-shop-project/grade/ar2576" target="_blank">Grading</a></td></tr></table>