<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Aaqib Rafiulla (ar2576)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2022 11:18:17 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/ar2576" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197426911-9fa40b88-21d5-4a96-a846-849ccf9f0175.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the calculate cost function with the output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197427339-6b8ca3a4-64d4-42f7-8a47-614747d7eed3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the calculate_cost function with output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197427524-9cadef12-bd13-4a79-b85f-1bb45f8d89cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Displaying the run function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197428529-b0e1abb8-6c6f-4ec2-9395-2feb9c6d126d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Displaying the output if the user needs only the container<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>Firstly in the calculate_cost function we are passing three arguments i.e., container, flavour<br>and toppings, and then we declare cost as global variable and initialise with<br>0. The working of the code clearly states that a user can only<br>have a single container i.e., either a waffle cone, sugar cone or a<br>cup, so after the user selects a container it outputs the cost of<br>the container and to select the flavors we use range and suppose the<br>user selects 2 then it checks the array length and goes inside the<br>loop and updates count, initially the flavor count is 0 which indicates vanilla<br>so it checks if the user input matches with the file in the<br>directory, if it matches then it computes the flavor cost and the loop<br>runs again until the user gets a flavour or if it matches according<br>to user input. For the topping ,suppose the user selects done or doesn&#39;t<br>needs any toppings it breaks and comes outside the loop and outputs the<br>total cost and if the user selects 2 toppings and if the array<br>length is two, the loop runs two times and in the first time<br>it checks if the topping or array matches with the user input, if<br>matches it computes the cost of toppings and finally it returns the cost.<br>And the code also runs even if the user requires no flavor or<br>toppings and it outputs the cost of the container alone.<div>In the run function<br>we declare container, flavor and toppings as global variable and since both flavor<br>and toppings is an array the user gives input and we append until<br>user selects next or done.<br><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197430284-4716a935-c6cc-4dae-ae4a-0308750bd09d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing OutOfStockException with the output indicating unavailability of cup<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197430919-7250f339-f4a7-448a-bddd-4bc53aaa9537.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing InvalidPaymentException when user does not enters the exact amount as mentioned in<br>the bill<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197431372-f1a111ed-1b2f-4f46-a3a6-2fa9cd252a02.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing NeedscleaningException <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197431723-63ddf803-a1d1-4b5b-8bed-d30680c3308e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197431929-97a2a2c6-4950-4786-9f7b-289d344d5c3e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ShowingExceededRemainingChoicesException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197432115-64439503-443c-4fe8-9fd1-ef2d80d7f8c5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the exceptions file which has the message to be printed in the<br>output to handle the exceptions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <p>To handle the exceptions , I used try and except block by first<br>checking the condition if the quantity is less than zero if it is<br>then raise OutOfStockException and print the message saying the stock is unavailable if<br>the quantity is set to 1.<div>And then for NeedscleaningException printing the message and<br>then calling the function cleanmachine() and if reamining_uses = USES_UNTIL_CLEANING and raising the<br>exception if the machine needs to be cleaned by initialising uses_until_cleaning as 1.</div><div>Printing<br>the message when Invalidchoiceexception is raised in the function pick_container(), pick_flavor() and pick_topping()<br>if user selects invalid choice which is not there in the menu.</div><div><div>Printing the<br>message when ExceededRemainingChoicesexception is raised in the function pick_container(), pick_flavor() and pick_topping() if<br>user selects more than 3 flavors.</div><div><div>Printing the message when Invalidpaymentexception is raised in<br>the function handle_pay() if user does not pay the exact amount mentioned in<br>the bill.</div><div><br></div></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197432501-a1fd4173-558d-441e-93d3-73dee7397724.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the test cases 1,2,3,4&amp;6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197432611-e59fb409-978c-497d-b145-e1551f9aa32e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the test cases 7,8&amp;5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197432995-e25f579a-8a74-4e69-a9e8-cbddc4d22163.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the test cases passed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197433169-465a0536-bf8d-4e7e-aeca-14fc1c148572.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the test cases passed and giving invalid input by equating to assert<br>to check if the test cases really work<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197434122-404b006d-0126-4b95-97f6-20d14b0bec00.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the test case 7 and giving invalid input by equating to assert<br>to check if the test cases really work<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197434550-2835d620-fa00-4481-87f4-be5d9eaeaf23.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the test case 8 and indicating all the 8 test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test-1 says that the first selection must be a container, so for this<br>I defined a function test_case_one which has machine as argument and then using<br>if statement to check if it is not equal to the container by<br>first initially importing icecream from STAGE.<div>Test-2 says we can only add flavors if<br>they are in stock by checking if remaining_uses &lt;= 0</div><div>Test-3 says we can<br>only add toppings if they are in stock by checking if remaining_toppings &lt;=<br>0<br></div><div>Test-4 says we can add upto 3 flavors/scoops which means maximum scoops or<br>flavours should be less than or equal to 3 by using if remaining_scoops<br>&lt;= 0<br></div><div>Test-5 says we can add upto 3 toppings by checking if remaining_toppings<br>&lt;= 3 as maximum can be 3<br></div><div>Test-6 says cost must be calculated based<br>on user choice&nbsp; by passing claculate_cost function with parameters having user choice and<br>then asserting it to check if the cost computed is correct<br></div><div>Test-7 says to<br>calculate total sales by passing calculate_cost function with parameters having user inputs and<br>then passing the computed result to handle_pay function to find the total sales<br>of the icecream or the cost generated.<br></div><div>Test-8 computes total icecream sold by passing<br>calculate_cost function with user input and then passing the result to handle_pay function<br>and finally asserting total_icecreams to the no of icecreams sold, if correct the<br>test case is passed.</div><div><br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AaqibRafiulla/IS601-007/pull/10">https://github.com/AaqibRafiulla/IS601-007/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>The assignments and the tasks assigned was really good as it did help<br>me to learn a lot and I encountered difficulties while running the test<br>cases and also in handling the exception especially the outofstockexception. All in all<br>i got to know things which i had mere knowledge and I learned<br>how to handle exceptions, run test cases according to the condition given and<br>finally get the desired output.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197437451-84e6d8e3-caf8-4221-abe4-5d73cbc5e4c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output with 2 or 3 combination<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/113788539/197437981-bb4b9638-9d45-4793-9608-bffbba5039f7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output showing if the user wants to only have a container alone<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F22/is601-mini-project-1-icecream/grade/ar2576" target="_blank">Grading</a></td></tr></table>