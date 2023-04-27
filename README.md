# OpenRoad USA
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


### Scope

To achieve both user and business goals, I will include the following features:

### Structure
The design of website is made to be clean cut and simple. This is to offer key information quick and locate what is desired rather than reading unessary information. 

App structure:

#### Skeleton

[Wireframes can be viewed here](https://share.balsamiq.com/c/jFLAg5a7apUrV86ucTo7tU.png)
---
## Features
### Home Page
### Road trips
### pending
### Contact Form
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
- []()
- []()
- []()


## Testing
### Code Validation
### Automated Testing
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
## Acknowledgments
I would like to thank my course mentor Akshat Garg for his guidance and support in our sessions. 