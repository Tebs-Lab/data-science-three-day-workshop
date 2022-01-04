import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import boto3
import io

# Connect and fetch the saved model.
s3_client = boto3.client('s3')
response = s3_client.get_object(Bucket="mock-ml-models", Key="RF-Fish-Weight")

# This data is a "streaming" type, so it must be read explicitly.
persisted_model_data = response['Body'].read()

# Load the model with pickle.
model = pickle.loads(persisted_model_data)

# Load the dataset (just to test that the model is in fact trained)
response = s3_client.get_object(Bucket='mock-ml-datasets', Key='datasets/fish/Fish.csv')
fish_dataset = pd.read_csv(io.BytesIO(response['Body'].read()))

# Split the data into input and labels — we're trying to predict fish weight based on 
# its size and species
labels = fish_dataset['Weight']
input_data = fish_dataset.drop(columns=['Weight'])

# We have one categorical parameter, so lets tell pandas to one-hot encode this value.
features = pd.get_dummies(input_data, columns=['Species'])

# It should score GREAT since we're scoring it on training data... 
scores = model.score(features, labels)

print(scores)