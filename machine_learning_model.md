## Why Choose Tensorflow For Image Processing

### Neural Networks vs Random Forest Classifier

Neural Networks are generally more popular in usage for image processing in machine learning model. The two major packages considered for this project were TensorFlow and Pytorch. Both packages are very succesful at running models on image classification. However, we chose TensorFlow due to our familiarity with the package from previous experience. We also should note that neural networks are much more consistent when it comes to image classification over other machine learning models such as a Random Forest Classifier. Neural Networks have much more flexibility for feature processing compared to Random Forest Classifiers. 


### TensorFlow vs Pytorch: A List

#### TensorFlow

- Has a built-in API that allows developers to directly link a machine learning model using TensorFlow to an already deployed website without usage of outside programs.

- Easy visualization of training data with Tensorboard

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

This model uses multiple layers to make the model boy rescale the images and be able to identify them. First the images are rescaled from 1 to 255 to 0 to 1 using a rescaling layer. This is to help speedup the model from using smaller numbers instead of larger numbers. The Conv2D layer creates a convolution kernel each time with the a size of the images being converted included in each layer. The MaxPooling2D layer that follows every Conv2D layer is primarily to down sample the detection of features in feature maps. This means that even if colors of pixels are slightly different they should be pooled togehter into the same groups for images such as car tail lights. The Dropout layer is to help data from overfitting by dropping out roughly 20% of all output units from the layer.  The Flatten layer is added to make certain that the tensor is reshaped to have a shape that is equal to the number of elements contained in tensor not including the batch dimension. Finally the Dense layer is a fully connected layer that is made to connect the model and use the 'relu' activation function. This entire model isn't tuned for high accuracy and is more of a general model made for image recognition and categorization.