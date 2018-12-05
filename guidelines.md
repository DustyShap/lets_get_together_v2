Guidelines
You should use the programming language you are most comfortable with to complete this exercise.
Please include a README file that includes the version of your language and any required dependencies.
Example: “This program was written with Ruby 2.2.3.”
Please include instructions on how to execute your program.
Example: “To execute this program, run ruby my_cool_program.rb”
If your program has a graphical interface (web app or any other UI) please include instructions on how to bring up the UI to run the program.
Please include some way to test your program. “Test” in this case means “execute the program against a specific set of inputs to make sure that it returns a particular output.” These tests can be manually executed or automated, either is fine.
Example : “To test this program, run ruby my_cool_program.rb, enter “Scott” for your name, and verify the output is Hello Scott.”
Please package all files you have written for this exercise in a single archive. Virtually any format is fine, but a single .zip file is probably the most straightforward way.
Be prepared to extend this problem during the pairing portion of your interview.
These submissions will be graded anonymously. Please refrain from adding any self-identifying information in the assignment.
This bit is important: please work on this independently. Feel free to search the internet for help, but otherwise you should write this code yourself without asking questions about the exercise to anyone except via email to apprenticeship@.
Overview
As someone who has been at Braintree for over a year, you must have heard about the ‘Let’s Get Together’ initiative. This initiative is a way for people across the organization to meet folks whom they may not have met before. How it works - interested people sign up and a program randomizes them into groups of a given size. All the people assigned to a group then figure out when they can have a get-together to meet each other. For this coding challenge, we would like you to build a similar tool.

Specifications
Your program will take as input a list of people and a number which represents the size of the group. It will randomly assign people to groups of the specified size and then output the groups, listing the people in each group. For example, if 22 people sign up and we would like them to meet in groups of 5, then the tool should generate 4 groups of 5 random people and 1 group of 2 people. A request to regenerate the groups, will randomize the input again and generate a different assignment of people to the groups. If the list of names contains duplicates, it will be considered as a single entry. The user will decide how many names to input in the list - your program should not limit how many can be accepted.

Assumptions
The list will contain at least one person on it
The size of the group will always be positive 1 or more
Considerations
You are free to choose how the user enters input. An HTML form is just as good as a command line prompt. The same goes for how you display output.
You are free to choose how you store or do not store this data in your program. A database is just as good as storing transactions in a file or in memory.
Graphic design is not the focus here so please do not spend too much time on aesthetics - the important ask is that the solution meets the requirements.
Example input 1
List of people:

Big Bird

Elmo

Kermit The Frog

Miss Piggy

Cookie Monster

Elmo



Group size: 3

Output 1a
Group 1

Kermit The Frog

Miss Piggy

Elmo



Group 2

Cookie Monster

Big Bird



If asked to regenerate,

Output 1b
Group 1

Big Bird

Elmo

Kermit The Frog



Group 2

Miss Piggy

Cookie Monster

Example input 2
Consider the same list of people as above, but if the group size is 4

Output 2
Group1

Kermit The Frog

Miss Piggy

Elmo

Big Bird



Group 2

Cookie Monster



Deadline
You will be required to submit your solution to this challenge by 11:59PM Central on Monday, July 2nd. Your manager has confirmed that you will have two hours of time during your work week to work on this challenge - discuss the details with that person. You are welcome to take additional time outside of work should you need it—submitting your challenge tomorrow is just as great as submitting it at 11:58PM on the 2nd.
