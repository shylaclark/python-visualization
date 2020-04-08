
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
