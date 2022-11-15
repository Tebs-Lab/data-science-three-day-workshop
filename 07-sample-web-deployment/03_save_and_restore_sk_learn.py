import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the data
fish_dataset = pd.read_csv('../datasets/fish/Fish.csv')

# Split the data into input and labels
labels = fish_dataset['Weight']
features = fish_dataset.drop(columns=['Weight', 'Species'])

# Train
model = RandomForestRegressor()
model.fit(features, labels)

# Save the model
with open('save_files/rf_model.pickle', 'wb') as save_file:
    pickle.dump(model, save_file)


# Load the model
with open('save_files/rf_model.pickle', 'rb') as load_file:
    loaded_model = pickle.load(load_file)

# It should score GREAT since we're scoring it on training data... 
# And they should be identical, since they are the same model.
print(model.score(features, labels))
print(loaded_model.score(features, labels))
