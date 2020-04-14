
# Flask

Install Flask:
```
conda install flask
```

Make a new hello.py class:
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

Start up your flask server:
```
export FLASK_APP=hello.py
flask run
```

Running on http://127.0.0.1:5000/

## Resources:
- https://healeycodes.com/javascript/python/beginners/webdev/2019/04/11/talking-between-languages.html
- https://blog.sneawo.com/blog/2017/06/27/how-to-use-jupyter-notebooks-with-flask-app/
- https://www.techiediaries.com/flask-tutorial-templates/
