from tensorflow.keras.models import load_model
import numpy as np


class MnistPredictor:
    def __init__(self, saved_model_path):
        self._model = load_model(saved_model_path)

    def predict(self, image_data):
        # 28x28 image -> 784x1 vector
        vectorized_data = np.array(image_data)
        vectorized_data = vectorized_data.reshape((784,))

        # Odd syntax note: tf expects to do predictions in batches, so we 
        # wrap our vector in a list, and also immediately select the 0th element
        # from the list of predictions. A bit ugly tbh.
        prediction = self._model.predict(np.array([vectorized_data]))[0]
        top_prediction_index = np.argmax(prediction)

        # These are in a special numpy format when returned above, so we cast them
        return int(top_prediction_index), float(prediction[top_prediction_index])