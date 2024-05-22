# #This will initialize our task manager application and use own import
# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# if os.path.exists("env.py"): #So as to use our hidden files, but wont de deployed to heroku and will throw an error
#     import env # noqua.....to stop warnings indicating that they are not availbale

# #Now we create an instance of the imported Flask() class, and store it in the app variable
# app = Flask(__name__)
# #setup configuration variables  from our enviroment variables
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
# app.config["SQLALCHEMY_ATABASE_URI"] = os.environ.get("DB_URL")

# #CREATE INSTANCE OF IMPORTED SQL CLASS

# db = SQLAlchemy(app)

# from taskmanager import routes #noqa...No quality Assurance

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from taskmanager import routes  # noqa

