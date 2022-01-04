# Exercise: Training and Restoring a Model Using AWS

Perform the following steps.

1. Login to an AWS instance via SSH.
    * The instructor will provide you with a URL you can use to access the server.
    * The instructor will provide you with a username and password as well.
2. Once you have connected to the remote server, use the AWS CLI to configure your AWS identity, this will allow you to access the `mock-ml-datasets` and `mock-ml-models` S3 buckets.
3. Read the `train_model.py` script.
    * What is it doing, and how does it work?
4. Modify the `train_model.py` script so that the key used to upload the dataset to the S3 bucket contains your name.
    * This is because everyone attempting this exercise will be using that S3 bucket, and you want your model to have a unique name!
5. Execute the `train_model.py` script on the AWS server. 
6. Log out of the AWS server.
7. On your OWN computer, run the AWS CLI configuration steps.
8. Read and modify the `restore_model.py` script such that you fetch your model. Do this by changing the key to match the key you used in step 4.
9. On your OWN computer, run the modified `restore_model.py` script. 

Viola! You have now used AWS to train a model using an AWS server, saved that model to an S3 bucket, and restored that model to your local device.

