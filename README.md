[//]: # (Implicit Links Within Project)

[1]: https://docs.google.com/spreadsheets/d/1C1NilfOavO-xX1UOnmB7djAXTZ_X5EZ-cNiQfMzb8rI/edit?usp=sharing   "Risk Assessment"
[2]: https://knightscode94.atlassian.net/secure/RapidBoard.jspa?rapidView=4&projectKey=FP&selectedIssue=FP-8  "JIRA Project"


# Aquarium water test logger


## Contents

- [Project Brief](#project-brief)
  - [Resources](#resources)
  - [Requirements](#requirements)
- [Project Approach](#project-approach)
- [Project Architecture](#project-architecture)
  - [Database Structure](#database-structure)
  - [CI Pipeline](#ci-pipeline)
  - [Front End Development](#front-end-development)
- [Testing](#testing)
 - [Unit Testing](#unit-testing)
 - [Functional Testing](#functional-testing)
- [Project Review](#project-review)
  - [Risk Assessment](#risk-assessment)
  - [Known Issues](#known-issues)
- [Author](#author)




## Project Brief

A more enviromentally friendly way to keep track of how your awauriums are doing in a store, home, professional enviroment

### Resources

- [RISKS][1]
- [JIRA][2]

### Requirements

For my project to be successful I need to create a CRUD able project this means it needs a CREATE READ UPDATE and DELETE. I met this by CREATING users and tanks with tests, READING the results from the tank tests on the home page, UPDATING and Reading the users information in account and finally DELETING the user and all the tests they carried out.

## Project Approach
my project went under a redesign last minute as I wanted a working app over having something fancy. initially i was going to use three tables but had issues joining the tests to the tanks so went to having the tests connected to the tanks in one table, it isnt the most efficient but can be imporved in later stages and can be developed.

I started by creating the back end to include everything I needed then worked on the users, tanks with testing then submitting to home page.

## Project Architecture

### Database Structure
![alt text](https://github.com/knightscode94/QA-SFIA/blob/master/DB%20structure.png)
![alt text](https://github.com/knightscode94/QA-SFIA/blob/master/ERD.png)

### CI Pipeline

### Front End Development
my front end uses flask as my primary development implamentation due to its ease of use and the many external plugin libraries it offers, i havent added any css code yet that will be for future development but the front end is intuitive and easily readable and designed so even the least tech savy users can use it. Flask is a front end web development program designed to code in python. I could of used DJANGO which offers more support but is known to be more complex than flask especially for new users such as myself.

## Testing
Here is my cov report of my application

![alt text](https://github.com/knightscode94/QA-SFIA/blob/master/TESTS.png)

### To get 100%
forms.py:
test email already in use functionality

routes.py:
login - redirect if user already logged in, if user is not registered go to register
update account - check user data is pulled from DB
delete - check all data related is deleted

### Unit Testing
## Start of testing___
Application setup export keys
drop the tables and create the new tables
create users and save to users table

## During testing____
standard test from tutorial test home page is visable
test you can create a tank with test information
test a user can logout
delete a user and everything associated with user
create a user with non auto input
login using pre installed data

## End of testing___
Delete tables

### Functional Testing
test server is running
from tutorials create a user
test login redirects to register if user doesnt exist and log in user after registration

### UI Testing with Selenium.

Selenium is a web browser automation tool that supports the most web browsers, across Windows, MacOS and Linux.

Selenium requires a web driver such as chromedriver to run tests within a web browser for my tests i used chrome.

## Project Review
for the first version of my application I am happy weith how things have turned out, if i develop this further I will look into splitting my tables into 3, tanks users and tests, until then I will probable add a search feature so that you can reduce the home page data down to date, tank or who completed the test.

## Risk Assessment

### Known Issues
if nitrate, nitrite and ammonia are not filled in the app doesnt respond with an error, this is easily fixed by adding adding a validator into the forms, the app doesnt crash just does nothing. I had not fixed this yet due to the time it took to get the float system in place.

## Author

**Tobias Jackson**

