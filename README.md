# simple-flask-heroku-app
The simplest flask app that can be run on heroku server.

# Only thing to understand here is Procfile
Here `app:app` is something similar to `from app import app`
First `app` is written because of filename and second `app` is written because of the variable in the file which is our app to run by gunicorn


## Tips and tricks for heroku
1. `heroku logs -t` to view server logs continuously
2. `heroku ps` to see running thread/service
3. `https://devcenter.heroku.com/articles/getting-started-with-python#introduction` for more
