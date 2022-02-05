
# Vehicle Identification
![logo](images/BMW2_edited.png)

# Overview

#### Welcome to the <img src='images/CTRL-ALT-DEFEAT-SMALL_edited.png' width=12% height=10% />     GitHub Machine Learning project page. 

##### This is our final team project for the <a href="https://bootcamp.unc.edu/data/">**UNC Chapel Hill Data Analytics Course**</a> 

## GitHub Application
<a href="https://jillibus.github.io/Vehicle-Identification">Vehicle Identification</a>

## General Information

**Team Name:** 

*CTRL ALT DEFEAT*

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

### Selected Project Topic

## <a href="https://github.com/jillibus/Vehicle-Identification/blob/main/Vehicle Identification Final - v2 - Deliverable 2.pdf"> Vehicle Image Recognition </a>

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
### GOAL:   
> Create a Image Recognition Model, using the simplest form of the model, that will recognize whether or not a vehicle is present in a photo from our data set. 

### Description of the data exploration analysis phase of the project:

> The data exploration phase of this project was a challenge for our team. The raw data from Stanford University came in MatLab format, which had to be processed for analysis in Pandas DataFrame. We will be evaluating the images to determine what features we want to capture for the dataset and then store into database tables.  

> The following outlines the steps that were taken to get things crackalakin'

### Loading in the dataset

> Due to the metadata being written in *Matlab*, not a familiar format that we've worked with before, such as a CSV, it was converted into a DataFrame and then loaded into our AWS Database. 

**1)** In order to be able to load and read the metadata files, we found an example of how to extract the data into from MatLab and convert it into Python DataFrames then we used sqlalchemy to upload the DataFrames into the PostgreSQL database. :arrow_right:  <a href="https://github.com/jillibus/Vehicle-Identification/blob/manghel/stanford_readdata.ipynb"> stanford_readdata.ipynb </a>

* The images were divided into two (2) sets, a training and testing one. Each of the images were numbered and named the same. 
* The metadata  was split into three (3) different pieces, each for the lables, training and testing set. These were created into separate DataFrames as can be seen below:

* Created DataFrame **labels** for definition of types of cars in the dataset.
<img src='images/df_labels.png' width=50% height=35%/>

* Created DataFrame **train** for definition of types of cars in training dataset. 
<img src='images/df_train.png' width=50% height=35%/>

* *Merging labels*
<img src='images/df_train_w_labels.png' width=50% height=35%/>

* Created DataFrame **test** for definition of types of cars in testing dataset. 
<img src='images/df_test.png' width=50% height=35%/>

* Uploaded the DataFrames into the *Cars* Database  
   _Note_: This part had to wait until the Database was created and the DataFrames were known.
  * Part 2 The process to move the contents of the Pandas DataFrames into the PostgreSQL database was using the following:
    * Using sqlalchemy's create_engine library
    ```
    # Load labels DataFrame into lables table
    import psycopg2
    from sqlalchemy import create_engine
    db_string = f"postgresql://postgres:{db_password}@cars.{aws_url}:5432/cars"
    engine = create_engine(db_string)
    ```
    * For each of the DataFrames we created in _stanford_readdata.ipynb_, we took the DataFrame and used the to_sql function.
    ```
    labels.to_sql(name='labels', con=engine, if_exists='append',index=True)
    df_train.to_sql(name='images', con=engine, if_exists='append',index=True)
    df_test.to_sql(name='images', con=engine, if_exists='append',index=False)
    ```

**2)** Create AWS Buckets to hold images from both the cars-train and cars-test datasets
_Note_: Uploaded the images to each AWS Bucket using AWS's upload tool.
    
<img src='images/Buckets.png' />   

**C)** Creation of AWS PostgreSQL Database 
    
<img src='images/Database.png'/>	

**Note: You will not be able to reach these links without proper authorization**
> <a href="https://www.postgresql.org/"> PostgreSQL </a> is the database we intend to use hosted on <a href="https://aws.amazon.com/"> Amazon Web Services, AWS </a>.    
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
<img src='images/Label_count.png' width=40% height=30% />
<img src='images/Image_count.png' width=40% height=30% />  

 * _Sample Data_: Located at **DBTableExamples.txt**
---
> Database Example:
<img src='images/DBTableExamples.png' width=45% height=30% />

### Running Train/Test Machine Model on Data Set

#### Decision-making process and explanation of model choice
> Neural Networks vs. Random Forest Classifier

* Neural Networks are generally more popular in usage for image processing in machine learning model (MLM). The two major packages considered for this project were **TensorFlow** and **Pytorch**. Both packages are very succesful at running models on image classification. However, our decision to chose was to go with <a href="https://www.tensorflow.org/"> TensorFlow </a>. 

* Apart from being more familiar with TensorFlow from previous experience, this model has a few other features which influenced our decision over Pytorch:
  * Built-in API allowing developers to directly link a model to an already deployed website without outsourcing programs.
  * Clear visualization for training data with Tensorboard.
  * No need for third party programs for visualization. 

* It is important to keep in mind that like any model, TensorFlow also has weaknesses which our team had to take into consideration:
  * Not a very efficient debugging method available.
  * More difficult to make quick changes to the model as it requires recreation from the beginning and retraining using any newly changed data. 
  
* Generally, Tensorflow allows developers to create and implement a neural network easier, primarily due to its slightly more mature product than Pytorch. There are more visualization options with Tensorboard which allow developers to recognize issues with models faster. The built-in API is a huge advantage for client presentation, allowing direct deployment of TensorFlow models to client websites and applications with little interference to the actual website.  

#### Machine Learning Models
> This model uses multiple layers to make the model rescale the images and be able to identify them. 
  * First the *images are rescaled* from 1 to 255 to 0 to 1 using a rescaling layer. This is to help speedup the model from using smaller numbers instead of larger numbers.   
  * The *Conv2D layer* creates a convolution kernel each time with the a size of the images being converted included in each layer.   
  * The *MaxPooling2D layer* that follows every Conv2D layer is primarily to down sample the detection of features in feature maps. This means that even if colors of pixels are slightly different they should be pooled togehter into the same groups for images such as car tail lights.   
  * The *Dropout layer* is to help data from overfitting by dropping out roughly 20% of all output units from the layer.    
  * The *Flatten layer* is added to make certain that the tensor is reshaped to have a shape that is equal to the number of elements contained in tensor not including the batch dimension.   
  * Finally the *Dense layer* is a fully connected layer that is made to connect the model and use the 'relu' activation function.   
  * This entire model isn't tuned for high accuracy and is more of a general model made for image recognition and categorization.  

### Dashboard
> We will present our project in Tableau Dashboard for our final deliverable. 
> We will create an application of our Vehicle Recognition Model
  * Our application will allow a user to upload an image and choose a button to run the application
  * The application will return if the image uploaded has a vehicle in the image or not.
  * Our application will be hosted on Amazon Web Services, AWS.  
  * We will be using Flask and Pickle to integrate the model into the application.
> In addition to using a Flask template, we will also integrate D3.js for a fully functioning and interactive dashboard.  

## Results

## Summary
> Recommendation for future analysis:
Increased timeframe for working with the data and building and training the model.


> Anything the team would have done differently:
TBD

Thank you for your time for reading our project details, please let us know if you need any additional information.  
Harsh Patel, Jill Hughes, Logan Murphy, Mihai Anghel
