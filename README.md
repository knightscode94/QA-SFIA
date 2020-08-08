[//]: # (Implicit Links Within Project)

[1]: https://docs.google.com/spreadsheets/d/1C1NilfOavO-xX1UOnmB7djAXTZ_X5EZ-cNiQfMzb8rI/edit?usp=sharing   "Risk Assessment"
[2]: https://docs.google.com/presentation/d/1BL5r35I7me4MSkJispzxlc57zhBZT7YtfSIj4wbV7tA/edit?usp=sharing   "Presentation"
[3]: https://team-1579095236068.atlassian.net/jira/your-work   "JIRA Project"
[4]: https://www.bma.org.uk/advice-and-support/nhs-delivery-and-workforce/workforce/mental-health-workforce-report   "mental health workforce report"


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
- [Project Management](#project-management)
- [Project Review](#project-review)
  - [Risk Assessment](#risk-assessment)
  - [Known Issues](#known-issues)
  - [Future Optimisation](#future-optimisation)
- [Author](#author)




## Project Brief

A more enviromentally friendly way to keep track of how your awauriums are doing in a store, home, professional enviroment

### Resources

- View my full risk assessment document [here.][1]
- View my project presentation [here.][2]
- View my JIRA Project [here.][3]

### Requirements

For my project to be successful I need to create a CRUD able project this means it needs a CREATE READ UPDATE and DELETE. I met this by CREATING users and tanks with tests, READING the results from the tank tests on the home page, UPDATING and Reading the users information in account and finally DELETING the user and all the tests they carried out.

## Project Approach
my project went under a redesign last minute as I wanted a working app over having something fancy. initially i was going to use three tables but had issues joining the tests to the tanks so went to having the tests connected to the tanks in one table, it isnt the most efficient but can be imporved in later stages and can be developed.

I started by creating the back end to include everything I needed then worked on the users, tanks with testing then submitting to home page.

## Project Architecture

### Database Structure

### CI Pipeline

### Front End Development

## Testing
here is my cov report of my app

----------- coverage: platform linux, python 3.6.9-final-0 -----------
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
application/__init__.py      12      0   100%
application/forms.py         35      5    86%   33, 91-94
application/models.py        22      0   100%
application/routes.py        74     17    77%   41, 49, 53, 64-68, 70-72, 94, 102-103, 115-117
-------------------------------------------------------
TOTAL                       143     22    85%

### To get 100%
## forms.py:
test email already in use functionality

## routes.py:
login - redirect if user already logged in, if user is not registered go to register
update account - check user data is pulled from DB
logout - check works
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

Selenium is a web browser automation tool that supports the most popular web browsers, across Windows, MacOS and Linux.

>> Permission to name this testing framework the “Mi-Guel” test framework.
>> I found my solution after reading Miguel Grinberg’s Flask Web Development (2nd edition). 

Selenium requires a 'web driver' to run tests within a web browser.

>> Additional credit goes to the ‘GOAT’: TDD with Python (2nd edition), written by Harry J.W. Percival.


## Project Management

## Project Review

## Risk Assessment

### Known Issues

## Author

**Tobias Jackson**

