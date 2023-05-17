# **Readme file for L3T10**

***

## **Capstone Project 1**

### **Task**
In this task, the purpose was to consolidate what had been done. It involved taking the Capstone Project from an earlier level using Sphinx to automatically create documentation, and publishing it on Github and Docker.

#### **Previous Capstone**
In Level 2 the task was to use Django to create a small website for any purpose. *The fictional "Against littering" party was chosen. They were standing for local election.* On the website there had to be a database driven component as well as user login and authentication.
On the website created, the viewer could see images of the fictional candidate, as well as a embedded Youtube video about the subject. A viewer could then either register for a mailing list, where their details would be kept in a database; or could register as a user. If they registered as a user, they could log in and see the database of events that were forthcoming, as well as add their own events and see other user details.


### **Installation**
## From Dockerhub
The repository is available on my dockerhub page [here](https://hub.docker.com/repository/docker/martinchris30/l3t10).
If accessing on [Docker playground](https://labs.play-with-docker.com), then log in and start a new instance. Then use the following command to download and run the image 
```
docker run -d -p 8000:8000 martinchris30/l3t10
```
This should then download the image and allow the user to access the programme by clicking on the open port 8000 at the top of the screen, as shown in the image below.
![Screenshot from docker playground, showing open port 8000](.\readme_images\docker_playground.png)


## From Github
The repository is available on my Github [here](https://github.com/ChrisMartin30/l3t10).
After downloading from here, or from my dockerhub page mentioned above, to install on the user's local machine a virtual environment should be used.

<br />  

### Using a Virtual Environment
To create a virtual environment on a Windows device (*as that's all I have experience with*) open the command prompt from the start menu and if the user has not used virtual environments before then install by following the folloing steps. First install pip by typing
```
python -m pip install pip
```
Once pip has been installed, install the package enabling virtual environments by typing
```
pip install virtualenv
```
Then install a wrapper with
```
pip install virtualenvwrapper-win
```

Once the user has the relevant packages they can set up a virtual environment by typing
```
mkvirtualenv venv
```
Then install the needed files in that virtual environment by navigating to the project folder and typing
```
pip install -r requirements.txt
```
This will install django as well as other necessary packages.

<br/>

***

## Using the project

The project is simply a website which allows those interested in the fictional political party to either join a mailing list, or register as a user and be allowed to see and create events.

#### Joining the mailing list
If the user joins the mailing list they fill in their details in the form; the Sphinx documentation for the form can be seen [here](../project/docs/_build/html/party.html#party.forms.MailingForm).

#### Registering as a new user
If the user registers as a new user they fill in their details as shown in image below.
![Screenshot of register new user page](.\readme_images\register_new_user.png)


## Credits
This project has been done at the direction of HyperionDev University of Edinburgh Software Engineering Bootcamp, and their documentation has been used in the writing of this README file.


## Future Improvements
* The Sphinx documentation could be made more comprehensive, for both the party website app and the user authentication app.
* The party website could be expanded and have further information, attachements such as a manifesto etc.
