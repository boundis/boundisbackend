boundisbackend
==============

Welcome to the boundis backend.

****To install all the required packages run pip install -r requirements.txt ****

This readme contains instruction on how you can clone the current working backend of boundis. This has been prepared to prevent changes inadvertently being made to the working repository. This assumes you are running Mac OS X. All steps are undertaken from within Terminal.

Step 1. Install virtualenv. Search the web and find a method you like to install (from terminal).

Step 2. Create a virtual environment. Navigate to you project folder (i.e. $ cd Projects/(project name)). In the terminal
          $ virtualenv (name)
        At (name) enter the name you would like to give the environemnt, choose any name.
        
Step 3. Activate the environment.
          $ source (name)/bin/activate. 
        Deactivate by typing 'deactivate'.
       
Step 4. Ensure you have activated your virtual environment (i.e.  $ source (name)/bin/activate.). Now install django by typing ' $ pip install django'

Step 5. Install git (if not already installed). Google this one.

Step 6. Create a directory in your project folder (i.e. $ mkdir (name eg. boundisbackend).

Step 7. Navigate to the new folder (i.e. $ cd boundisbackend). We will call this the boundis project folder.

Step 8. Create a git repository in this directory $ git init

Step 9. Copy the git repo to your local drive so you can run the backend. $ git clone https://github.com/boundis/boundisbackend.git. By cloning the repo in this way it ensures you cannot accidently make any changes. You can do what ever you want to the files and it wont effect the version on github.

Step 10. While inside the boundis project  folder within the termine type $ python manage runserver.

Step 11. In your web browser type 'http://localhost:8000/locations/all_venues'. 
