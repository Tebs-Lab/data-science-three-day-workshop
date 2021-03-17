import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import boto3
import io

# Load the data from s3
s3_client = boto3.client('s3')
response = s3_client.get_object(Bucket='mock-ml-datasets', Key='datasets/fish/Fish.csv')

# The response body has the data, but it's a stream so it must be read
# And converted to a "bytes" object.
fish_dataset = pd.read_csv(io.BytesIO(response['Body'].read()))

# Split the data into input and labels — we're trying to predict fish weight based on 
# its size and species
labels = fish_dataset['Weight']
input_data = fish_dataset.drop(columns=['Weight'])

# We have one categorical parameter, so lets tell pandas to one-hot encode this value.
features = pd.get_dummies(input_data, columns=['Species'])

model = RandomForestRegressor()
model.fit(features, labels)

persist_model_data = pickle.dumps(model)

# Upload to S3
s3_client.put_object(Body=persist_model_data, Bucket="mock-ml-models", Key="RF-Fish-Weight")
