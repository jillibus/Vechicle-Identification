import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
app = flask.Flask(__name__, template_folder='templates')
@app.route('/')
def main():
    return(flask.render_template('main.html'))
if __name__ == '__main__':
    app.run()



import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
#with open(f'model/car_model.pkl', 'rb') as f:
#    model = pickle.load(f)

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/')
#@app.route('/', methods=['GET', 'POST'])
def main():
#    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
#    if flask.request.method == 'POST':
#        # Extract the result of image 
#        input_image = flask.request.form['test_image']
#
#        # Make DataFrame for model
#        input_variables = pd.DataFrame([image],
#                                       columns=['test_image'],
#                                       dtype=object,
#                                       index=['input'])
#
#        # Get the model's prediction
#        prediction = model.predict(input_variables)[0]
#    
#        # Render the form again, but add in the prediction and remind user
#        # of the values they input before
#        return flask.render_template('main.html',
#                                     original_input={'Test Image':test_image}
#                                     # result?      'Class':humidity
#                                     result=prediction,
#                                     )

if __name__ == '__main__':
    app.run()
