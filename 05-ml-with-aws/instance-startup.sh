#!/bin/bash

## This script installs the nessesary libraries and opens up ssh to password only.
## Use this script at creation time of the instance on the AWS Console.

# Install The CLI
yes | snap install aws-cli --classic

# Install the python libraries
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
pip install pandas boto3 scikit-learn
pip3 install pandas boto3 scikit-learn
python3 -m pip install pandas boto3 scikit-learn

# Create a user so we don't need to distribute PEM files
apt install openssl
useradd -m -p $(openssl passwd -crypt <PASSWORD_HERE>) <USERNAME_HERE>

# Allow password authentication
sed -i 's/.*PasswordAuthentication no.*/PasswordAuthentication yes/'  /etc/ssh/sshd_config

# Probably only one of these is actually required...
service sshd reload
service ssh reload
service sshd restart
service ssh restart