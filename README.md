# Open Road
---

## Table of Contents
---
- [User Experience (UX)](#user-experience-ux)
    * [Strategy](#strategy)
    * [User Stories](#user-stories)
    * [Scope](#scope)
    * [Structure](#structure)
- [Features](#features)
    * [Home Page](#home-page)
    * [Road Trips](#road-trips)
    * [Contact Form](#contact-form)
    * [Footer](#footer)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
    * [Code Validation](#code-validation)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Bugs and Fixes](#bugs-and-fixes)
- [Deployment](#deployment)
    * []()
    * []()
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## User Experience (UX)
---
### Strategy

With the core UX Principles in mind, I began brain storming and deciding who my target audience for my road trip website and the features I can intergrate that can benefit users. 

The target audience for Open Road are:
- 21-35 year olds
- People who seek adventure and not afraid to go on the off beaten track
- People that have potentially less responsibilities and are able to take a road trip
- People who enjoy getting inspiration from others experiences and sharing their own

Following the pandemic, there are circa three years worth of missed years people were unable to travel and explore. We are seeing more [young people](https://www.travelmarketreport.com/RetailStrategies/articles/Younger-Travelers-Plan-to-Travel-More-Spend-More-Post-Pandemic) wanting to travel and have new experiences to make up for lost time. 

As the site is specifically road trip orientated travel, younger people often go on holiday with friends and have potentially less responsibilities such as children/mortgage. A road trip can be as short or as long as you want it to be, providing flexibility.

The users will be looking for:
- The ability to navigate the site with ease.
- Read concise information about road trips the user is interested in. 
- The user is able to create a user account. Which links to the following point below:
- The ability to share their own experiences via writing their own blog or commenting on another post. 

Due to the site being able towards a younger audience who often browse on mobile devices; I will use bootstrap elements to customise and create a responsive site. Often young people are looking for a memory building experience with friends/ loved ones or finding themselves in a solo experience; which road trips can offer. 

### User Stories

Please find all my user stories & acceptance criteria in greater detail [here]()

- USER STORY: Manage posts.
- USER STORY: Manage/create Categories.
- USER STORY: Site Pagination.
- USER STORY: Open a post.
- USER STORY: Basic website layout with Navbar/footer.
- USER STORY: User can clear view Logged in status.
- USER STORY: Like a post.
- USER STORY: View road trip posts list
- USER STORY: Remind user to register for an account if they do not have one. 
- USER STORY: Scroll to the Top Button on home page.
- USER STORY: Comment on a post. 
- USER STORY: Intuitive sit navigation.
- USER STORY: All road trips must have a description, suggested travel length.
- USER STORY: Accout Registration.
- USER STORY: Informative landing page.

### Scope

To achieve both user and business goals, I will include the following features:

- A responsive navbar that allows users to navigate through various pages on the site.
- A Landing page providing a brief summary about Open Road and links to trips posts and login/ registration options.
- Road Trip Post page, with Card displaying the different posts from users shared.
- Add Road Trip page, allowing logged in users to share their experience.
- Post detail page, users can click on a post from road trip page that they are interested in and read the full post. 
- Edit Post page: If a user is logged in, there shows an Edit Button on both the road trip page and post detail page. This will take them to the edit page where they can make alterations to their post. 
- Delete Post Page: If a user is logged in, there shows a Delete Button on both the road trip page and post detail page. This will take them to the delete page where they can make alterations to their post.
- Register/ login and sign out feature using Django allauth.

### Structure

The design of website is made to be clean cut and simple. This is to offer key information quick and locate what is desired rather than reading unessary information.

The website is made of two apps:
- Website: offers core functionality
- roadtrip: display posts and blog post data

App structure:

#### Skeleton

Please note, the website differs slightly from the original wireframes.

The theme is supposed to be clean cut and simple, offering the simplicity that is a humbling road trip journey. I have used bootstrap to create styling and design to my website. 

[Wireframes can be viewed here](https://share.balsamiq.com/c/jFLAg5a7apUrV86ucTo7tU.png)

I chose a dark green colour to offer a nature theme to the site as road trips around the USA are heavily influence by the immersive experience in the great unknown. 
---
## Features
### Home Page

Navigation Bar: The nav bar has links to all the active pages. This allows the user to clearly identify each option and navigate to where they want. 

The Nav bar is fully responsive and collapses on mobile devices to a hamburger icon. This allows the user to easily access the navigation links without the hassle of pressing back buttons on the browser. Or struggling to read small text along the bar. 

Links to road trips - This offers a second option to the user in case they are scrolling on the home page initially and decide they want to view posts. 

About information - this opens into a modal and offers the user a brief summary of the site on the home page. 

### Road trips

Site users are able to view blog posts from people's road trips around the USA.

If the user is logged in, they are able to view `Edit` and `Delete` buttons for posts they have published. Otherwise they are not able to do so with others posts.

### Post Detail

Here the user is able to view the blog post in full detail and comment if they wish to share an opinion or feeback. 

If the user is logged in, they are able to view `Edit` and `Delete` buttons for posts they have published. Otherwise they are not able to do so with others posts.

### Add Road trips

Once logged in, users with log ins are able to add their own blog experiences. 

### Edit Road trips

Once logged in, users with log ins are able to add their own blog experiences. 

### Delete Road trips

Once logged in, users with log ins are able to add their own blog experiences. 

### Comment on posts

Once logged in, users with log ins are able to leave comments on travel posts.

### Like a post

Once logged in, users with log ins are able to like posts.

### Footer
---
## Technologies Used
### Languages 
- HTML
- CSS
- JavaScript
- [Python](https://www.python.org/)
    - Python used to write all of the code in this application that makes it fully functional.
- [Django](https://www.djangoproject.com/)
    - Django is the framework that has been used to build the overall project and all its apps.

### Tools 

- [Image Color Picker](https://imagecolorpicker.com/color-code/20442c)
- [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjw8-OhBhB5EiwADyoY1eL0Yyb7LjlqjLVuM9xfXLRdmzK9m1CxpreaZIzIzxFIs8Oms8CNSBoCPagQAvD_BwE)
- [Font Awesome](https://fontawesome.com/)
    - Used for the icons in the website.
- [GitHub](https://github.com/)
    - Used to store code for the project once pushed.
- [Pep8](http://pep8online.com/)
    - Used to test code for any issues/errors.
 [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code written and used for this webpage.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code written and used for this webpage.
- [JSHint](https://jshint.com/)
    - Used to validate JS code.
- [PostgresSQL/ElephantSQL](https://www.elephantsql.com/)
    - I have used ElephantSQL a PostgreSQL relational database in deployment to store the data for my models.
- []()

## Testing
### Code Validation
### Automated Testing

I have used the Coverage library to carry out my Automated Testing. 

To generate your own coverage report from the command line:
1. Install the package using the command `pip3 install coverage`.
2. Run coverage run manage.py test.
3. Run `coverage html` to generate the report.
4. To access the report via the browser, use the command `python3 -m http.server` and open `index.html` file from inside `htmlcov` folder, that will appear. 

### Manual Testing
### Bugs and Fixes
--- 
## Deployment 
The main branch of my repository open_road, has been used for the deployment of this application.

### Github and Gitpod

In order to deploy my Django application, I used the Code Institute Python Essentials Template.

Instructions: 
- Click on `Use This Template` button.
- Then create a repository name and a concise description.
- Click on `Create Repository from Template`. This will then create your repository and open up into its repository page.
- Then create a Gitpod Workspace. Click on `Gitpod`. Expect a few minutes of loading while it sets up.
- Rule of thumb should be to return to the Gitpod Workspace when you want to continue working on the project rather than clicking on `Gitpod` in your repository; as this will create a new workspace rather than continue on the one you are currently working on. 
- (Optional: but it is good to pin your workspace so that it isn't deleted).
- It is important to commit your work carried out often with clear messages. The following commands are used:
3 Step Commit Process:
    - `git add .`: adds **ALL** modified files to staging area
    - `git commit -m "A message explaining what you are committing"`: commits changes to a local repository.
    - `git push`: pushes all committed changes to the subject Github repository.

### Heroku

To deploy my project, I followed the steps offered by the Code Institute tutorial and the [Django Blog Cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf).

- In the Gitpod CLI use `pip3 freeze --local requirements.txt` to create the relevant files needed for Heroku to succesfully install your project dependencies. 
- **Important**: `requirements.txt` and `env.py` should be in the `.gitignore` file to prevent the files from being committed. The env.py holds the secret key and important links that should not be compromised.
- In addition, you need a `Procfile` as this will specify the commands that are carried out by the app on startup.

Instructions: 
1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in. You cannot do the following steps without an account. 
2. Click `New` and select `Create New App`.
3. Give your project a unique name. You will be prompted to change it if it is not.
4. Select the region you are in (e.g. mine is EU).

In the Heroku settings:
You need to set your Environment Variable to essure your application deploys successfully.
- Click `Revel Config Vars` and enter:
 - SECRET_KEY - to be set to your chosen key
- CLOUDINARY_URL - to be set to your Cloudinary API environment variable
- PORT = 8000

Heroku Deployment:
- Click Deploy tab
- Click `Github-connect` to connect your Github account.
- Search for your repository name.
- Select the correct repository name and click `connect`.
- You can either manually or automatically deploy your application. 
- Select your deployment method and click `Deploy Branch`.
- Once ready, you will be able to click `View`. 
--- 
## Credits
--- 
Please see the following links I have used to fix bugs, learn from or tackle problems:


## Acknowledgments

I would like to thank my course mentor Akshat Garg for his guidance and support in our sessions. 
