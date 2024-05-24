# Testing for *Your Shopping List*

This is the testing for the site *Your Shopping List*.

Link to live site.
Find the README [here](README.md).
## User Story testing

|User Story|Outcome|
|-|-|
|As a user I can create an account so that I can sign in to the application.|A non logged in user can click the Sign Up link in the navbar and create an account|
|As a user I can log in to my account so that I can see, edit and delete my lists|A non logged in user with an account can log in to the account using the Login link in the navbar|
|As a user I can log out of my account so that me or someone else can log in to another account on the same device|A logged in user can logout using the logout link. The user or someone else can then log in to another account on that device|
|As a user I can create a shopping list so that I have a place to write what groceries to buy.|A logged in user can create a list by clicking the Create New List button displayed on the list menu page|
|As a user I can edit a list I created before so that I can reuse older lists or change a list I intended to use.|A logged in user with a created list can edit the list by navigating to the list and adding, editing and deleting items in the list. They can also edit the list name|
|As a user I can delete a list so that I don’t have to see it in my list menu|A logged in user with a created list can delete the list by first clicking the Delete List button and then confirm the deletion in the modal that pops up.|
|As a user I can share a list so that other people can shop from a list I have created.|A logged in user with a created list can email the list to whomever they like by first clicking the Share List button, filling in the form in the modal that pops up and then click the Send List button|
|As an admin I can delete users so that inactive users don’t take up space in the database|A Superuser can go to the admin page, log in and edit and delete users|

## Automated Testing
### W3C HTML
All of this sites html pages have been validated through W3C validator. It came back with one warning: it suggests the logo in the navbar should not be an h1 element. As a minor warning I have chosen to disregard it.

![Image of the W3C html validator varning](static/images/documentation/home-page-warning.jpg)

### W3C CSS
This project has one CSS file. It went through the W3C CSS validator and came back with no warnings or errors.
### JSHint
This project has on javascript file. It went through JSHint and came back with some warnings.
- It warns that the bootstrap variable is undefined
- It warns that the emailjs variable is undefined
- It warns that the sendMail variable is unused

The bootstrap and emailjs variable are important to the functionality of the site and exist due to instructions from bootstrap respective emailjs. I will disregard these warnings due to eventual errors to functionality.

sendMail is a function written properly, why this is caught by JSHint I do not know. I will disregard this warning.
### CI Python Linter
Code Instittue has a easy to use Python Linter. You can find it [here](https://pep8ci.herokuapp.com/).

All of the python files were run through the CI Python Linter. It came back with no errors.

### Lighthouse
Lighthouse is a devtools tool to measure performance, accessibility, best practices and SEO of a site. It rates between 0 and 100. These are the results of this site:

**Mobile, home page**

![Image of the Lighthouse score for mobile on the home page](static/images/documentation/LH-mobile-home.jpg)

**Mobile, list menu page**

![Image of the Lighthouse score for mobile on the list menu page](static/images/documentation/LH-mobile-list-menu.jpg)

**Mobile, list page**

![Image of the Lighthouse score for mobile on the list page](static/images/documentation/LH-mobile-list.jpg)

**Desktop, home page**

![Image of the Lighthouse score for desktop on the home page](static/images/documentation/LH-desktop-home.jpg)

**Desktop, list menu page**

![Image of the Lighthouse score for desktop on the list menu page](static/images/documentation/LH-desktop-list-menu.jpg)

**Desktop, list page**

![Image of the Lighthouse score for desktop on the list page](static/images/documentation/LH-desktop-list.jpg)

With a few 100s in the top and a few 87 as a lowest, the average value is 94.5. I deem it acceptable with some work to be done with the accessibility of the site.

## Manual Testing
## Bugs
