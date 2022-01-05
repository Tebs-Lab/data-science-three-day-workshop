from io import BytesIO

from flask import Flask, render_template, request, jsonify
from PIL import Image, ImageOps

from mnist_model import MnistPredictor
from fish_model import FishPredictor
 
app = Flask(__name__)

# Initialize the models, each of which will be used in their particular route.
# In a larger app, these routes might be spread across a few files, and initializing
# our model wrappers would preferably be done in each relevant route.
mnist_predictor = MnistPredictor('../save_files/mnist-model.h5')
fish_predictor = FishPredictor('../save_files/rf_model.pickle')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mnist', methods=["GET", "POST"])
def mnist():
    if request.method == 'GET':
        return render_template('mnist_input.html')

    # Fetch, resize, and grayscale-ify the data.
    user_drawing = Image.open(BytesIO(request.data))
    user_drawing = user_drawing.resize((28,28))
    user_drawing = ImageOps.grayscale(user_drawing)

    # Major Note: The frontend drawing API encodes the data differently than
    # the training data. Specifically the data is inverted: 255 means "black"
    # in the training data but 255 means "white" in the web interface. So, we
    # have to invert the image for our predictor to work.
    user_drawing = ImageOps.invert(user_drawing)

    # Make the prediction using our simple API
    digit, conf = mnist_predictor.predict(user_drawing)

    # Return the predictions as JSON
    return jsonify({
        'digit_prediction': digit,
        'confidence': float(conf) 
    })

# In class exercise: finish this route such that:
# 1. There is a landing page for the fish model.
# 2. Users can submit the requisite fish weights using an html form via POST.
# 3. The web server renders a page predicting  the fish's weights given the provided measurements.
#    (this will require you to import sklearn and restore the model!)
@app.route('/fish', methods=["POST", "GET"])
def fish():
    if request.method == "GET":
        return render_template("fish_input.html")

    weight = fish_predictor.predict(
        request.form['length1'],
        request.form['length2'],
        request.form['length3'],
        request.form['height'],
        request.form['width']
    )

    return jsonify({"weight": weight})

