# Facial Recognition Attendance

## Description
This application reflects my implementation of open source facial recognition software with real-world use cases. This is a project completed during my first semester of a two semester capstone project during my undergraduate education. Here, I build a full stack react/django app to allow for classroom management via automated facial recognition. 

The basic use case of this application is to allow for a professor or class leader to add in information about a particular class or section, along with student pictures, and each day the students would check in by having their face scanned at the computer. This helps ensure validity of attendance in that an individual cannot attend a class for someone else. Additionally, it eliminates the need for tedious time spent calling names or having students sign in through some other means.

## Installation

| Dependency | Version | Details |
| :--------: | :-----: | ------- |
| Python | 3.* | The build is based off of python 3. Specifically I used Python 3.7 but most versions of python 3 should still be compatible. |
| Django | 2.2.7 | The backend is completely django based and uses its version of SQL Lite for small database utilities. Installation can be handled through the pip package manager. |
| Django REST Framework | 3.10.3 | The backend also uses the Django REST framework to create REST-full API utilities for the front end application. |
| Face Recognition | 1.2.3 | Face recognition is an open source library available on GutHub that is one of the more accurate Python recognition systems available. This is used in part to handle attendance taking. |
| NPM | Non Specific | The Node Package Manager is used to handle all of the front end dependencies associated with the React app. |

## Usage

The application has two core components, front end and back end. Both are separate applications referencing one another through API calls. The directory structure has simply labeled these two entities.

<i>To start the front end...</i>


cd front_end

npm install

npm start


<i>To start the back end</i>


cd back_end

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8007

<b>NOTE: You may have to change some things in Settings.py as well as some of the URLS for the API's as they are platform specific to my server.</b>
