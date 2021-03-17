# Provisioning a Server

So called "severless" deployments are popular for inference — at least inference of fairly simple models. However, due to the (generally) significant computational costs of training a model, and the limitations of AWS Lambda (for example, a 3GB memory maximum) training a model using AWS Lambda is not especially popular.

Instead, it's more common to use Sagemaker or EC2 to provision a server and use it to train the model. Once the model is trained, we'll typically persist it and any other relevant artifacts (usually to S3), but it could also be saved directly on the server and retrieved via SSH for example. 

We then use that server that trained model and any other relevant outputs (often to S3) 

We are essentially following this tutorial: [https://aws.amazon.com/getting-started/hands-on/train-deep-learning-model-aws-ec2-containers/](https://aws.amazon.com/getting-started/hands-on/train-deep-learning-model-aws-ec2-containers/)

## Step 0 — Configure a User To Access Elastic Container Service

* If you haven't already, you need to configure and IAM user and give that user The ECS Full Access Policy.
* ECS, the Elastic Container Service, is the service that manages the virtual machines that you can use to deploy EC2 Instances. 
* Your IAM user needs ECS_FullAccess permissions
    * You can find these in the "attach existing policies" tab of the "add permissions" menu.
    * Additionally, we need to add this "inline policy" json:

    ```
    {
       "Version": "2012-10-17",
       "Statement": [
              {
                     "Action": "ecr:*",
                     "Effect": "Allow",
                     "Resource": "*"
              }
       ]
    }
    ```

## Step 1 — Spin Up A Server

* Go to the EC2 console.
* Click Launch Instance
* We're using the Deep Learning AMI Ubuntu template, it has a GPU!
    * But regardless of what server type you spin up, accessing it and executing commands on it works very similarly. 
    * Although, different OSes obviously have different terminal interfaces.

* Select review and launch.
* Download the security key-pair .
* Click "view instances" to see your server

## Step 2 — A Lot Of Configuration...

* Go to your instances menu.
* Find the instance you just created
* Copy it's public DNS.

Now, navigate to the .pem file you saved and execute the following:

```
cd /Users/<your_username>/Downloads/

chmod 0400 <your .pem filename>

ssh -i <your .pem filename> ubuntu@<your instance DNS>
```

* From inside the EC2 instance, you need to configure AWS access.
* Install cli with `sudo snap install aws-cli`
* `aws configure`
* You'll need your secret key... hope you wrote it down?
    * Or just make a new one.

* Install the dependencies:

```
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip install pandas boto3 scikit-learn
pip3 install pandas boto3 scikit-learn
python3 -m pip install pandas boto3 scikit-learn
```

## Step 3 — Upload and Execute The Training Code

The easiest way to transfer files to your AWS instance is SCP.

```
scp <path/to/train_model.py> <user>@<ec2-public-dns>:<~/path/on/EC2_instance>
```

You can also download with SCP

```
scp <user>@<ec2-public-dns>:<~/path/on/EC2_instance> <path/to/save_file> 
```

Install the dependencies (this is a quick dirty way, your infrastructure team probably uses a Docker container or something else.) We have done this for the students!

```
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip install pandas boto3 scikit-learn
pip3 install pandas boto3 scikit-learn
python3 -m pip install pandas boto3 scikit-learn
```
## Step 4 — Download the Saved Model and Perform Inference

* Go to `restore_model.py` for an example. 
    * This code will work anywhere that has the proper libraries and AWS configuration setup!

* For example:
    * As part of your webserver startup code.
    * In AWS Lambda
    * On your local machine...