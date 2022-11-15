import pickle
import numpy as np


class FishPredictor:
    def __init__(self, saved_model_path):
        # Load the model
        with open(saved_model_path, 'rb') as load_file:
            self.model = pickle.load(load_file)


    def predict(self, length1, length2, length3, height, width):
        fish_datapoint = np.array([length1, length2, length3, height, width])
        fish_datapoint = np.expand_dims(fish_datapoint, axis=0)
        weights = self.model.predict(fish_datapoint)
        
        return weights[0] # sklearn expects multiple samples at once, we only gave one.