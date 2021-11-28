# Project 2, Car Rental Database application
Benjamin Knight, Christopher Smith, Luciano Marconi.  
This is a Flask web application built alongside the official [flask tutorial here](https://flask.palletsprojects.com/en/2.0.x/tutorial/index.html)

# How To Run
These steps are assuming you can already run a python program. Because we are using a virtual environment no additonal libraries should be needed to run  
1. After cloning the repository change directories to the project2 directory `cd .\project2\`
2. Now activate the virtual environment with  `.\env\Scripts\activate`
3. Set these two environment variables
    - `$env:FLASK_APP = "flaskr"`  
    - `$env:FLASK_ENV = "development"` 
4. If this is your first time running the program, initalize the database `flask init-db`
5. Finally run `flask run`

You should now be able to navigate to the website by going to `http://127.0.0.1:5000/` in your internet browser. From here I recommend going to `http://127.0.0.1:5000/assignment` since that is where most of the actual development will take place.

## Helpful Stuff
- I made a [basic youtube video](https://www.youtube.com/watch?v=nwafy_JwdNU) that walks through the website (as of 11/27/21) and goes over the entire sequence from a user pressing a button to when the data is displayed to the page. If you don't care about the details and just want to recreate it, skip to [13:05](https://youtu.be/nwafy_JwdNU?t=785)
