# ML In A Web Server Demo

This section contains:

1. Sample "train and persist" scripts for two models:
    1. A regression model based on the fish weight dataset.
    2. A classification model for the MNIST dataset.
2. A simple Flask web server which utilizes the saved models.

The purpose of this section is to demonstrate how a model can be built, persisted, imported into another software package where users can then interact with the model.

## Instructor Notes:

1. Demo the code that trains and saves the models first.
    * Students will also need to run the code to create the persistent models!
2. Demo the web app itself (not the code, the running instance) second.
    * Startup command from `flask-app` directory: `flask run`
        * `FLASK_ENV=development FLASK_ENV=development flask run`
        * (use export to turn on development mode for a whole shell session)
    * Reference for simple Flask startup: [https://flask.palletsprojects.com/en/2.0.x/quickstart/](https://flask.palletsprojects.com/en/2.0.x/quickstart/))
3. Demo a little of the Flask specific stuff, enough for students to complete the micro exercise meaning:
    * What a template is, how it works, and how to render one.
    * Fetching data from the request (specifically from a form POST)
    * How the basic app routing works.
