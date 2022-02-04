## Why Choose Tensorflow For Image Processing

### Neural Networks vs Random Forest Classifier

Neural Networks are generally more popular in usage for image processing in machine learning model. The two major packages considered for this project were TensorFlow and Pytorch. Both packages are very succesful at running models on image classification. However, we chose TensorFlow due to our familiarity with the package from previous experience. We also should note that neural networks are much more consistent when it comes to image classification over other machine learning models such as a Random Forest Classifier. Neural Networks have much more flexibility for feature processing compared to Random Forest Classifiers. 


### TensorFlow vs Pytorch: A List

#### TensorFlow

- Has a built-in API that allows developers to directly link a machine learning model using TensorFlow to an already deployed website without usage of outside programs.

- Easy visuzliation of training data with Tensorboard

- Not a very good debugging method available.

- Hard to make quick changes to the model. Requires recreating the model from the beginning and training it again using any newly changed data.


#### Pytorch

- Very similar coding style to Python.

- Dynamic Graphs included

- Easy and quick editing.

- Third party needed for viusalization 

- API server needed for pushing model to production/website.

Generally Tensorflow has an easier time for the developer to both create and implement a new neural network model, this is primarily due to TensorFlow being a slightly more mature product than Pytorch. First there is more visualization options with Tensoboard that allows developers to more quickly recognize any issues within new models. The bigger gain is for both developers and for clients. The built-in API that TensorFlow comes with allows developers to directly deploy TensorFlow models directly to client websites and applications with little interference to the actual website. TensorFlow is also more mature with being developed and working for mobile devices via the TensorFlow Lite application being developed alongside TensorFlow. 


#### Model Information

