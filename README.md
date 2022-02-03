
# Vehicle Identification
![logo](images/BMW2_edited.png)

# Overview

#### Welcome to the <img src='images/CTRL-ALT-DEFEAT-SMALL_edited.png' width=12% height=10% />     GitHub Machine Learning project page. 

##### This is our final team project for the <a href="https://bootcamp.unc.edu/data/">**UNC Chapel Hill Data Analytics Course**</a> 

## GitHub Application
<a href="https://jillibus.github.io/Vehicle-Identification">Vehicle Identification</a>

## General Information

**Team Name:** 

CTRL ALT DEFEAT

**Team Logo:**

<img src='images/CTRL-ALT-DEFEAT-SMALL_edited.png' width=14% height=12% />

**Team Members:**  

> <a href="https://github.com/hsp910"> Harsh Patel </a>  
> <a href="https://github.com/jillibus"> Jill Hughes </a>  
> <a href="https://github.com/ltmurphy"> Logan Murphy	</a>  
> <a href="https://github.com/CrossCreed"> Mihai Anghel	</a>  

### Communication Protocols

* The team will regularly use <a href="https://slack.com/"> **Slack** </a> :speech_balloon: for communicating updates and sharing of links/files   
* The team will meet three (3) times a week to work on the project.
	* Two times during designated class time to work on the project. Teammates are welcome to remain in breakout rooms after class to continue working. 
	* A third final time to work on remaining tasks before submitting deliverables will be made during the weekend (Sat/Sun depending on schedules) each week.    
* Any project emergency communication will be via phone :thumbsup:  

# Selected Project Topic

#### <a href="https://github.com/jillibus/Vehicle-Identification/blob/main/Vehicle%20Identification%20Final%20-%20Deliverable%202.pdf"> Vehicle Image Recognition </a>

### Business Applications for Vehicle Image Recognition

> The topic at hand was selected for its potential use in intelligent transportation applications that focus on monitoring of traffic flow, automated parking systems, and security enforcement.  Adding physical characteristics, with existing systems that track traffic patterns that include type, velocity, direction and position, (Vehicular Ad Hoc Networks - VANETs), would advance the information provided for use in additional applications.

### Source Data Chosen

> The Cars dataset contains *16,185* images of *196* classes of cars. The data is split into *8,144* training images and *8,041* testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. **__2012 Tesla Model S__** or **__2012 BMW M3 coupe__**.

> Dataset Source: <a href='https://ai.stanford.edu/~jkrause/cars/car_dataset.html'> https://ai.stanford.edu/~jkrause/cars/car_dataset.html </a>  
> Number of Images: 16,185

> 3D Object Representations for Fine-Grained Categorization  
  Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei    
  4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.   
  
### Project Goal

> Our Project Goal is to create an _Image Recognition Model_, with the simplest form of the model recognizing whether or not a vehicle is present in a photo from our data set. 

### Future Goals
_After Course Completion_
> Our next goal we will build on the model so that it can determine whether or not the vehicle in the image is a BMW or another brand of vehicle.

> Further Goals for this project, with added complexity and continued development, are to determine the make and model of targeted vehicles. 

> The final iteration will have a multidude of potential real world uses such as amber alert and law enforcement application integration. 

### **Questions the team hopes to answer with the data:**
1. Can we take a dataset containing thousands of images and create a model using machine learning in order to identify whether or not a vehicle is present in an image?

2. Can our prototype machine learning model identify the make, model and year of a targeted vehicle in an image?

---
# GOAL:   
> Create a Image Recognition Model, using the simplest form of the model, that will recognize whether or not a vehicle is present in a photo from our data set. 

### Description of the data exploration phase of the project:

> The data exploration phase of this project was a challenge for our team. The raw data from Stanford University came in MatLab format, which had to be processed for analysis in Pandas Dataframe.
The following thought process outlines the steps that were taken to get things crackalakin'

  * In order to be able and load & read the dataset metadata file :arrow_right: created Python File - <a href="https://github.com/jillibus/Vehicle-Identification/blob/manghel/stanford_readdata.ipynb"> stanford_readdata.ipynb </a>
    * Created DataFrame - labels for definition of types of cars in the dataset.
    <img src=https://github.com/jillibus/Vehicle-Identification/blob/manghel/images/df_labels.png?raw=true />





  
  * The images were divided into 2 sets  
    * A training set and a testing set, **each of the images numbered and named the same.**
  * The metadata about the images were also in pieces, this time in 3 sets.  
    * A set holding the labels
    * A set holding the training metadata, in a specific order to line up with the image names of the training images
    * A set holding the testing metadata, in a specific order to line up with the image names of the testing images
  * The metadata is writting in an old programming language, _Matlab_
  * The matadata is not in a format such as a CSV file, a Panda's DataFrame, or any other format we were familiar with.
  * The capture of the metadata needed to be converted from MatLab to a DataFrame, then loaded into a Database.
> The process to perform this task was in 2 parts. 
  * Part 1 (This is shown in _stanford_readdata.ipynb_)
    * Conversion of the MatLab metadata files into Pandas DataFrames  
    * Conversion of the datatypes in the Dataframes to the correct datatypes  
  * Part 2 The process to move the contents of the Pandas DataFrames into the PostgreSQL database was using the following:
    * Using sqlalchemy's create_engine library
    ```
    # Load labels dataframe into lables table
    import psycopg2
    from sqlalchemy import create_engine
    db_string = f"postgresql://postgres:{db_password}@cars.{aws_url}:5432/cars"
    engine = create_engine(db_string)
    ```
    * For each of the DataFrames we created in _stanford_readdata.ipynb_, I took the dataframe and used the to_sql function.
    ```
    labels.to_sql(name='labels', con=engine, if_exists='append',index=True)
    df_train.to_sql(name='images', con=engine, if_exists='append',index=True)
    df_test.to_sql(name='images', con=engine, if_exists='append',index=False)
    ```

### Description of the analysis phase of the project:
> We will be evaluating the images to determine what features we want to capture for the dataset and then store into database tables.

### Technologies, languages, tools, and algorithms used throughout the project:
#### Data Cleaning and Analysis
> Pandas will be used to clean the data and perform an exploratory analysis. 
> Further analysis will be completed using Python.

#### Database 
**Note: You will not be able to reach these links without proper authorization**
> <a href="https://www.postgresql.org/"> Postgresql </a> is the database we intend to use hosted on <a href="https://aws.amazon.com/"> Amazon Web Services, AWS </a>.    
  *  _DB Name:_ cars  
  *  _Database Instance ID:_ cars 
  *  _Database Link:_ <a href='http://cars.ckxsklg24qnv.us-east-2.rds.amazonaws.com/'> Cars DB </a>  
  *  _Database Port:_ 5432  
> We will be using AWS R3 storage for the images.   
  * _Storage Bucket:_ <a href='http://cars-traindataset.s3-website.us-east-2.amazonaws.com'> Training Set </a>  
  * _Storage Bucket:_ <a href='http://cars-testdataset.s3-website.us-east-2.amazonaws.com'> Testing Set </a>  
> Database Schema
<img src='images/ERD_CarsDB.png' width=55% height=40% />

 * _Creation Scripts:_ Located in **DB Images/create_tables.sql**  
---  
> Database on AWS
<img src='images/Table-Constraint-Setup.png' width=40% height=30% /> 

---  
> Database population:
<img src='images/Label_count.png' width=50% height=30% />
<img src='images/Image_count.png' width=50% height=30% />  

 * _Sample Data_: Located at **DBTableExamples.txt**
---
> Database Example:
<img src='images/DBTableExamples.png' width=55% height=40% />

#### Machine Learning Models
> SciKitLearn is the ML library we'll be using to create a classifier. This will determine if an image contains a vehicle or not and what make the vehicle is.  
> TensorFlow will be the application and library where we will be using and testing the Neural Networks Models.
> The Model we will use is Sequential, adding hidden layers with activation set to _reLU_, using the optimizer _adam_ and _accuracy_ metrics.    
> The original data set is a 50-50 split of data, we will be adjusting this as future models are introduced.    

### Dashboard
> In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard.   
> We will present our project in Tableau Dashboard for our final deliverable. 
> Our application will be hosted on Amazon Web Services, AWS.  

## Results

## Summary
> Recommendation for future analysis:
Increased timeframe for working with the data and building and training the model.


> Anything the team would have done differently:
TBD

Thank you for your time for reading our project details, please let us know if you need any additional information.  
Harsh Patel, Jill Hughes, Logan Murphy, Mihai Anghel
