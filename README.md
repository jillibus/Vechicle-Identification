
# Vehicle Identification
![logo](images/BMW2.png)

# Overview

Welcome to  <img src='images/CTRL-ALT-DEFEAT-SMALL.png' width=10% height=10% />     GitHub Machine Learning project page. 

This is our final team project for the <a href="https://bootcamp.unc.edu/data/">**UNC Chapel Hill Data Analytics Course**</a> 

## GitHub Application
<a href="https://jillibus.github.io/Vehicle-Identification">Vehicle Identification</a>

## Communication Protocols

**Team Name:** <img src='images/CTRL-ALT-DEFEAT-SMALL.png' width=10% height=10% />  

**Team Members:**  

> <a href="https://github.com/hsp910"> Harsh Patel </a>  
> <a href="https://github.com/jillibus"> Jill Hughes </a>  
> <a href="https://github.com/ltmurphy"> Logan Murphy	</a>  
> <a href="https://github.com/CrossCreed"> Mihai Anghel	</a>  

> The team will regularly use **Slack** for communicating updates and sharing of links/files.   
> The team will meet twice a week, after class, and once more during the weekend for final updates.   
> Any project emergency communication will be via phone.   

## Selected Project Topic

**Vehicle Image Recognition**

## Business Applications for Vehicle Image Recognition

> The topic at hand was selected for its potential use in intelligent transportation applications that focus on monitoring of traffic flow, automated parking systems, and security enforcement.  Adding physical characteristics, with existing systems that track traffic patterns that include type, velocity, direction and position, (Vehicular Ad Hoc Networks - VANETs), would advance the information provided for use in additional applications.

> Our first project Goal is to create a Image Recognition Model, using the simplest form of the model, that will recognize whether or not a vehicle is present in a photo from our data set. 

> Once we achieve our first Goal, we will add to this model, and determine whether or not the vehicle in the image is a BMW or another brand of vehicle.

> Future Goals of this project, with added complexity and continued development, is to determine the make and model of targeted vehicles. 

> The final iteration will have a multidude of potential real world uses such as amber alert and law enforcement application integration. 

## Source Data Chosen

> The Cars dataset contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. 2012 Tesla Model S or 2012 BMW M3 coupe.

> Dataset Source: <a href='https://ai.stanford.edu/~jkrause/cars/car_dataset.html'> https://ai.stanford.edu/~jkrause/cars/car_dataset.html </a>  
> Number of Images: 16,185

> 3D Object Representations for Fine-Grained Categorization  
  Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei    
  4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.    

## **Questions the team hopes to answer with the data:**

Goal 1:  
> Can the model correctly predict if there is a vehicle in the image?

---
## GOAL 1:   
> Create a Image Recognition Model, using the simplest form of the model, that will recognize whether or not a vehicle is present in a photo from our data set. 

### Description of the data exploration phase of the project:


### Description of the analysis phase of the project:

### Technologies, languages, tools, and algorithms used throughout the project:
#### Data Cleaning and Analysis
> Pandas will be used to clean the data and perform an exploratory analysis. 
> Further analysis will be completed using Python.

#### Database Storage
**Note: You will not beable to reach these links without proper authorization**
> Postgresql is the database we intend to use hosted on Amazon Web Services, AWS.    
  *  _DB Name:_ cars  
  *  _Database Instance ID:_ cars 
  *  _Database Link:_ <a href='http://cars.ckxsklg24qnv.us-east-2.rds.amazonaws.com/'> Cars DB </a>  
  *  _Database Port:_ 5432  
> We will be using AWS R3 storge for the images.   
  * _Storage Bucket:_ <a href='http://cars-vehicles.s3-website.us-east-2.amazonaws.com'> Training Set </a>  
  * _Storage Bucket:_ <a href='http://non-vehicles.s3-website.us-east-2.amazonaws.com'> Testing Set </a>  
> We will integrate Flask to display the data.  

#### Machine Learning
> SciKitLearn is the ML library we'll be using to create a classifier to determine if an image has a vehicle or not, or what type of vehicle it has.  
> TensorFlow will be the application and library where we will be using and testing the Neural Networks Models.    
> The original training set is a 50-50 split of data, we will be adjusting this as future models are introduced.    

### Dashboard
> In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard.   
> We will also look at Tableau Dashboard to determine if that will work with our application.  
> It will be hosted on Amazon Web Services, AWS.  

## Results

## Summary
> Recommendation for future analysis:

> Anything the team would have done differently:


Thank you for your time for reading our project details, please let us know if you need any additional information.  
Harsh Patel, Jill Hughes, Logan Murphy, Mihai Anghel
