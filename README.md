# Your Shopping List
*Your Shopping List* is the place to go if you want a quick and easy way to create a shopping list while on the go! You can: edit it, delete it or share it with a friend!

This is a project created during the Code Institute flag, being the portfolio project 4. It is for learning purposes only.

Link to live site
Picture of responsiveness

## Contents

* [User Experience](#user-experience)
    * [Colour Scheme](#colour-scheme)
    * [Font](#Font)
* [Project Planning](#project-planning)
    * [Agile Methods](#agile-methods)
    * [MoSCoW method](moscow-method)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [ERDs](#erds)
* [Features](#features)
    * [CRUD functionality](#crud-functionality)
    * [Showcase](#showcase)
    * [Future Features](#future-features)
* [Technologies and Languages used](#technologies-and-languages-used)
    * [Languages](#Languages)
    * [Technologies](#technologies)
    * [Frameworks and libraries](#frameworks-and-languages)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Guthub](#github)
    * [Django](#Django)
    * [Heroku](#heroku)
    * [CI Database](#CI-database)
    * [Clone](#Clone)
    * [Fork](#fork)
* [Credits](#credits)
    * [Code](#code)
    * [Acknowledgements](#acknowledgements)

## User Experience
This application needs to be fast to use. It is competing with your phones notes app, a piece of paper and a pen and of course just your memory.

The USP of this site is to have a clean look which gives the user a clear oversite and easy to use features you can not find at it's competitors.
### Colour Scheme
The colours chosen for this site are contrasting eachother and each serves their own purpose.

- Off-white / #ECE5DC: used as a general background colour
- Ocean blue / #2DAFD6: used as the background colour of the navigation bar
- Notebook yellow / #EED878: used as the background of the lists and the landing page information. Chosen to imitate the colour of a notebook.
- Teal / #008080: used for the lines in the notebook imitation.

![Image of the colour pallette used](static/images/documentation/color-pallette-YSL.jpg)
### Font
The font used is *Roboto*. It is a clean, sans-serif font which fits perfect for a website with a simple design. The font is imported from Google Fonts.

## Project Planning
This project is intended to help with the everyday life mission to go to the grocery store. With a working shopping list system you can make your shopping more efficient and be sure to come back home with the items you needed. With a sharing feature a partner, friend or family member can do the shopping the site user planned and in that way be of service in sickness and in health.

**Site Goals**
* Provide a quick way to write and handle shopping lists
* Have a nice look with good responsiveness
* Have easy to use features, especially on mobile
* Have a quick and secure way of sharing lists

### Agile Methods
This project was planned with agile methods. As some features depended on others to be built, the obvious way was to start with the most fundamental features and user stories first and work upwards. Since one feature had the label "Could have" it was planned to be built last, after the site was fully functioning.

### MoSCoW Method
The issues created for this site were labeled with the use of the MoSCoW method. That divides the labels into:

* Must have - features that is a must for the site to be working as intended
* Should have - features that the site should have to be of use to the user
* Could have - features that could bring that little extra to the user
* Won't have - features that no longer fit the project or won't be included in this release

### User Stories
|User Story|Priority|
|-|-|
|As a user I can create an account so that I can sign in to the application.|MUST HAVE|
|As a user I can log in to my account so that I can see, edit and delete my lists|MUST HAVE|
|As a user I can log out of my account so that me or someone else can log in to another account on the same device|MUST HAVE|
|As a user I can create a shopping list so that I have a place to write what groceries to buy.|SHOULD HAVE|
|As a user I can edit a list I created before so that I can reuse older lists or change a list I intended to use.|SHOULD HAVE|
|As a user I can delete a list so that I don’t have to see it in my list menu|SHOULD HAVE|
|As a user I can share a list so that other people can shop from a list I have created.|COULD HAVE|
|As an admin I can delete users so that inactive users don’t take up space in the database|SHOULD HAVE|

### Wireframes
The site was developed mobile first. The desktop wireframes are therefor bigger versions of the mobile wireframes.

**Mobile**

![Wireframe for the start page on mobile](static/images/documentation/mobile_start_page.png)
![Wireframe for the sign up page on mobile](static/images/documentation/mobile_sign_up.png)
![Wireframe for the login page on mobile](static/images/documentation/mobile_login.png)
![Wireframe for the list menu on mobile](static/images/documentation/mobile_list_menu.png)
![Wireframe for the list on mobile](static/images/documentation/mobile_handle_list.png)
![Wireframe for the share list feature on mobile](static/images/documentation/mobile_share_list.png)

**Desktop**

![Wireframe for the start page on desktop](static/images/documentation/Desktop_start_page.png)
![Wireframe for the sign up page on desktop](static/images/documentation/Desktop_sign_up.png)
![Wireframe for the login page on desktop](static/images/documentation/Desktop_login.png)
![Wireframe for the list menu on desktop](static/images/documentation/Desktop_list_menu.png)
![Wireframe for the list on desktop](static/images/documentation/Desktop_handle_list.png)
![Wireframe for the share list feature on desktop](static/images/documentation/Desktop_share_list.png)

### ERDs
This site uses three models: Django's *User* model, a *list* model and a *list item* model. 

Below is the Entity Relationship Diagram:

![Image of the sites ERD](static/images/documentation/your-shopping-list-ERD.png)


**User**
Django's User model is a excellent way to create and handle users at your site. Combined with the AllAuth framework, a lot of the work to create a functioning site with user is already done. 

The default fields for the AllAuth sign up page is *username*, *email* and *password.* To differentiate between regular users and admin accounts the *Superuser* field was added to the ERD. These are not all of the Django User model fields, but those used in this site.

**List**
The List model is a custom model. It has a primary key of Djangos default id field, that increments automatically. That id is also what builds the detailed list views URL. The author field is a foreign key that connects with the user model. It is mostly used for authentification.

**List item**
The List item model is what creates what you actually see in the lists. It also has a primary key of the default id field. It also connects to the user model via the author field. The List model has a second foreign key connecting it to the List model. This is to make sure that the correct items are displayed when opening a list.

## Features
### CRUD functionality
This site contains three different kind of objects: User, List and List item.

As a logged in user you can handle List and List items. With simple buttons and forms you can create, read, update and delete your lists and list items.

As a not logged in user you are only allowed to create a user. Remaining handling features of the user object is limited to the superusers through the admin page. As of now there is no way for a regular user to update username, change password or delete account.

### Feature showcase
#### Navbar
The Navbar is simple. An only text logo and links to Sign Up, Login and (when logged in) Logout.

![Image of the sites navbar when not logged in](static/images/documentation/navbar-signup-login.jpg)

![Image of the sites navbar when logged in](static/images/documentation/navbar-logout.jpg)

#### Sign Up / Login / Logout
The Sign Up, Login and Logout pages all inherits the navbar from the rest of the site. Their own design comes mostly from the AllAuth framework.

![Image of the sites sign up page](static/images/documentation/sign-up-page.jpg)
![Image of the sites login page](static/images/documentation/login-page.jpg)
![Image of the sites logout page](static/images/documentation/logout-page.jpg)

#### List menu
The list menu displays the user's lists with a notebook like background. The name of the appears to be on one of the lines in the notebook. At the bottom of the menu the user finds the "Create New List"-button. That opens a modal in which the user can submit a name to the list.

![Image of the list menu](static/images/documentation/list-menu.jpg)
![Image of the new list modal](static/images/documentation/new-list-modal.jpg)

#### List
In the detailed list view is where the real work of the site takes place. This is where the user creates the content of the list. The page also allows the user to edit the list, delete the list and via email share the list.

The *EDIT* and *EDIT LIST* buttons allows the user to edit the list name respectively the list items.

To share and delete the list - modals pop up and the user can enter the information needed and/or confirm the action.

![Image of the sites list page](static/images/documentation/detailed-list.jpg)
![Image of the sites list page when edit buttons clicked](static/images/documentation/list-edits.jpg)
![Image of the share list modal](static/images/documentation/share-list-modal.jpg)
![Image of the delete list modal](static/images/documentation/delete-list-modal.jpg)
#### Error pages

### Future features








## Credits
The log in/log out/sign up code is from the CI Blog Walkthrough
The toast js is from Bootstrap
the notebook look is from https://www.codesdope.com/blog/article/getting-notebook-paper-effect-with-css/