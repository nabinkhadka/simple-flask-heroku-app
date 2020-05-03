# simple-flask-heroku-app
In a couple of minutes, deploy the simplest flask app that can be run on heroku server.

# Two important things to notice
1. Here `app:app` is something similar to `from app import app`
First `app` is written because of filename and second `app` is written because of the variable in the file which is our app to run by gunicorn
2. `requirements.txt` file is absolutely necessary for heroku to understand that this is python project


## Tips and tricks for heroku
1. `heroku logs -t -a <app_name>` to view server logs continuously
2. `heroku ps` to see running thread/service
3. `https://devcenter.heroku.com/articles/getting-started-with-python#introduction` for more
