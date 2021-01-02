# Spell Correction Flask

## Overview

A Flask application for spell correction that uses dictionary substitution method. The dictionary we use in this repository is from [Peter Norvig]
(https://norvig.com/ngrams/spell-errors.txt).

## Usage

In this repository, Python 3.8.2 was used and it is recommended to create a virtual environment to isolate the dependencies used by this module.
```
$ virtualenv spell-correction-env
$ source ./spell-correction-env/Scripts/activate
$ pip install -r requirements.txt
```

We implement the spell correction that uses dictionary substitution method. To use this, we have the `/spell-correction` view function. The request parameter for this function is `text`.

To run this app, we can use flask command
```
$ export FLASK_APP=api.py
$ flask run
```

We can also use python -m flask
```
export FLASK_APP=api.py
python -m flask run
```

And head over to 
```
http//127.0.0.1:5000/spell-correction?text=raning
```
