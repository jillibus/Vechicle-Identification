
# Vehicle Identification
![logo](images/BMW2_edited.png)

# Overview

#### Welcome to the <img src='images/CTRL-ALT-DEFEAT-SMALL_edited.png' width=12% height=10% />     GitHub Machine Learning project page. 

##### This is our final team project for the <a href="https://bootcamp.unc.edu/data/">**UNC Chapel Hill Data Analytics Course**</a> 

## GitHub Application
<a href="https://jillibus.github.io/Vehicle-Identification">Vehicle Identification</a>
test## General Information

**Team Name:** 

*CTRL ALT DEFEAT*

**Team Logo:**

<img src='images/CTRL-ALT-DEFEAT-SMALL_edited.png' width=14% height=12% />

**Team Members:**  

> <a href="https://github.com/hsp910"> Harsh Patel </a>  
> <a href="https://github.com/jillibus"> Jill Hughes </a>  
> <a href="https://github.com/ltmurphy"> Logan Murphy	</a>  
> <a href="https://github.com/CrossCreed"> Mihai Anghel	</a>  

# Selected Project Topic

> The following link will take you to our draft presentation created in Google Slides. The file was saved and uploaded to GitHub as a PDF to allow easier access for viewers. 

#### <a href="https://github.com/jillibus/Vehicle-Identification/blob/main/Vehicle Identification Final - v2 - Deliverable 2.pdf"> Vehicle Image Recognition </a>

#### Tableau Presentation

The project outline can also be viewed in Tableau via this <a href="https://public.tableau.com/app/profile/logan.murphy/viz/Vehicle_Identification_Presentation_D3/VehicleIdentificationStory?publish=yes"> hyperlink </a> *(Version for Deliverable 3)*

### Business Applications for Vehicle Image Recognition

> The project topic was selected for its potential use in smart transportation applications that focus on the monitoring of traffic flow, automated parking systems, and security enforcement.  Adding physical characteristics, with existing systems that track traffic patterns that include type, velocity, direction and position, (Vehicular Ad Hoc Networks - VANETs), would advance the information provided for use in additional applications.

### Source Data Chosen

> The Cars dataset contains *16,185* images of *196* classes of cars. The data is split into *8,144* training images and *8,041* testing images, where each class has been split roughly in a 50-50 split. Classes are typically at the level of Make, Model, Year, e.g. **__2012 Tesla Model S__** or **__2012 BMW M3 coupe__**.

> Dataset Source: <a href='https://ai.stanford.edu/~jkrause/cars/car_dataset.html'> https://ai.stanford.edu/~jkrause/cars/car_dataset.html </a>  
> Number of Images: 16,185

> 3D Object Representations for Fine-Grained Categorization  
  Jonathan Krause, Michael Stark, Jia Deng, Li Fei-Fei    
  4th IEEE Workshop on 3D Representation and Recognition, at ICCV 2013 (3dRR-13). Sydney, Australia. Dec. 8, 2013.   
  
### Project Goal

> Our Project Goal is to create an _Image Recognition Model_, with the simplest form of the Model recognizing whether or not a vehicle is present in a photo from our data set. 

### Future Goals
_After Course Completion_
> Our next goal we will build on the Model so that it can determine whether or not the vehicle in the image is a BMW or another brand of vehicle.

> Additional Goals for this project, with added complexity and continued development, are to determine the make and model of targeted vehicles. 

> The final iteration will have a multidude of potential real world uses. Law enforcement and amber alert application integration are just two of the myriad of examples. 

### **Questions the team hopes to answer with the data:**
1. Can we take a dataset containing thousands of images and create a model using machine learning in order to identify whether or not a vehicle is present in an image?

2. Can our prototype machine learning model identify the make, model and year of a targeted vehicle in an image?

---
# GOAL:   
> Create a Image Recognition Model, using the simplest form of the Model, that will recognize whether or not a vehicle is present in a photo from our data set. 

### Description of the data exploration analysis phase of the project:

> The data exploration phase of this project was a challenge for our team. The raw data from Stanford University came in MatLab format, which had to be processed for analysis in a Pandas DataFrame. We will be evaluating the images to determine what features we want to capture for the dataset and then store into database tables.  

> The following outlines the steps that were taken to get things crackalakin'

> Due to the metadata being written in *Matlab*, which is not a familiar format for the team like csv, it was converted into a DataFrame and then loaded into our AWS Database. 

**A)** In order to be able to load and read the metadata files, we found an example of how to extract the data from MatLab and convert it into Python DataFrames. Then we used SQLAlchemy to upload the DataFrames into the PostgreSQL database. :arrow_right:  <a href="https://github.com/jillibus/Vehicle-Identification/blob/manghel/stanford_readdata.ipynb"> stanford_readdata.ipynb </a>

* The images were divided into two (2) sets, a training set and a testing set. Each of the images were numbered and named the same. 
* The metadata  was split into three (3) different pieces,  one each for the labels, training and testing set. These were created into separate DataFrames as can be seen below:

* Created DataFrame **labels** for definition of types of cars in the dataset.
<img src='images/df_labels2.png' width=40% height=5%/>

* Created DataFrame **train** for definition of types of cars in training dataset. 
<img src='images/df_train2.png' width=40% height=35%/>

* *Merging labels*
<img src='images/df_train3.png' width=40% height=35%/>

* Created DataFrame **test** for definition of types of cars in testing dataset. 
<img src='images/df_test2.png' width=40% height=35%/>

**B)** Create AWS Buckets to hold images from both the cars-train and cars-test datasets  
_Note_: Uploaded the images to each AWS Bucket using AWS's upload tool.
    
<img src='images/Buckets2.png' width=70% height=35%/>   

**C)** Creation of AWS PostgreSQL Database 
    
<img src='images/Database2.png' width=70% height=35%/>
 
* The process to move the contents of the Pandas DataFrames into the PostgreSQL database was using the following:
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
* Creation of tables - lables & images in cars database for dataset
* Population of tables - from DataFrames, labels, df_train, df_test

<img src='images/class_count_train.png' width="722" height="460"/>
	
<img src='images/Training-Dataset-Loaded.png' width="722" height="460"/>
	
<img src='images/Image-Table.png' width="722" height="460"/>

**D)** Running Train/Test Machine Model on Data Set

1) In a new Python file, we start with the DataFrames, populated from the Cars Database.
2) We send in the DataFrame, and loop through the Training data, pulling the image from the location in the Dataframe.
3) Send it through our Model, and Train our Model.
4) Once the Model is trained, we repeat the steps with our Testing data and determine our accuracy.

**Our Model** uses multiple layers to make the Model rescale the images and be able to identify them. 
![vehicle/nonvehicle model](https://i.imgur.com/Cjxfk8V.png)
  * First the *images are rescaled* from 1 to 255 to 0 to 1 using a rescaling layer. This will allow the Model to run faster by using smaller numbers instead of large numbers.   
  * The *Conv2D layer* creates a convolution kernel each time with the a size of the images being converted included in each layer.   
  * The *MaxPooling2D layer* that follows every Conv2D layer is primarily to down sample the detection of features in feature maps. This means that even if colors of pixels are slightly different they should be pooled together into the same groups for images such as car tail lights.   
  * The *Dropout layer* is to help data from overfitting by dropping out roughly 20% of all output units from the layer.    
  * The *Flatten layer* is added to make certain that the tensor is reshaped to have a shape that is equal to the number of elements contained in tensor not including the batch dimension.   
  * Finally the *Dense layer* is a fully connected layer that is made to connect the Model and use the 'relu' activation function.   
  * This Model isn't tuned for high accuracy but is instead a general Model made for image recognition and categorization. 

### Decision-making process and explanation of model choice
> Neural Networks vs. Random Forest Classifier

* Neural Networks are generally more popular in usage for image processing in machine learning models (MLM). The two major packages considered for this project were **TensorFlow** and **Pytorch**. Both packages are very succesful at running models on image classification. However, the final decision was to go with <a href="https://www.tensorflow.org/"> TensorFlow </a>. 

* Apart from being more familiar with TensorFlow from previous experience, this model has a few other features which influenced our decision over Pytorch:
  * Built-in API allowing developers to directly link a model to an already deployed website without outsourcing programs.
  * Clear visualization for training data with Tensorboard.
  * No need for third party programs for visualization. 

* It is important to keep in mind that like any model, TensorFlow also has weaknesses which our team had to take into consideration:
  * Not a very efficient debugging method available.
  * More difficult to make quick changes to the model as it requires recreation from the beginning and retraining using any newly changed data. 
  
* Generally, Tensorflow allows developers to create and implement a neural network easier, primarily due to its slightly more mature product than Pytorch. There are more visualization options with Tensorboard which allow developers to recognize issues with models faster. The built-in API is a huge advantage for client presentation, allowing direct deployment of TensorFlow models to client websites and applications with little interference to the actual website.  

### Database

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

### Dashboard
> We will present our project in Tableau Dashboard for our final deliverable.   
> We will present our application prototype that we plan on completing in a future release.  
> We will also integrate D3.js for a fully functioning and interactive dashboard.    

## Results
___
![ModelTestResults](https://user-images.githubusercontent.com/89947873/153783845-e61721b8-968a-49fa-a62f-b05af7f1659c.png)

The results list the Make,Model, and Year of the vehicle and how many times it was identified. 

![image](https://user-images.githubusercontent.com/89947873/153802758-dafa300f-59a3-429c-95a5-5174b1389b40.png)

The overall accuracy is low but the Model is functioning. Accuracy improvements in future iterations will be a definitive objective.

## Summary
> Recommendation for future analysis:      
Increased timeframe for working with the data in order to train and test the Model.  

> Anything the team would have done differently:      
Understood the complexity of the dataset we chose, in order to read the data from a file system and then present it to the Model.  

Thank you for your time and reading our project details. Please let us know if you need any additional information.    
Harsh Patel, Jill Hughes, Logan Murphy, Mihai Anghel
