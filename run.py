import os
from taskmanager import app


#Tell the application how and where to run the application
if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP"),
        port= os.environ.get("PORT"),
        debug=os.environ.get("DEBUG")
    )

#We need to render some front-end templates where flask looks for any html templates and name it base.html