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
- [Authors](#authors)




## Project Brief

A more enviromentally friendly way to keep track of how your awauriums are doing in a store, home, professional enviroment

### Resources

- View my full risk assessment document [here.][1]
- View my project presentation [here.][2]
- View my JIRA Project [here.][3]

### Requirements

## Project Approach

## Project Architecture

### Database Structure

### CI Pipeline

### Front End Development

## Testing

### Unit Testing

### Functional Testing

### Issues with Flask-Testing.

_This section of the documentation covers my experience with the Flask-Testing module, why I ultimately chose to scrap the LiveServerTestCase class, and how I designed my own multi-threaded test framework._

Test_client() is a _lightweight browser emulation_ that comes prebuilt into flask. This makes it easier for developers to test their programs without having to write their own.
However, this client cannot _fully_ emulate the environment of an application running within a browser.

There are a number of things that it will **not** do. The test_client() browser cannot execute JavaScript code, which makes it impossible to fully test an interactive UI. 
Any code that is included within a http response will be returned without having been executed.

For this project, I wanted to ensure that my functional tests were running in a ‘true-to-life' production environment.

This is why I chose to run my functional tests on a use a real web browser, hat is connected to our application, running on a real web server. 

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

