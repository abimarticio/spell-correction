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

Or simply use python command
```
python api.py
```

And head over to 
```
http//127.0.0.1:5000/spell-correction?text=raning
```

We can also test out our API using curl command in the following manner
```
$ curl http//127.0.0.1:5000/spell-correction?text=raning
```

## License

```
Spell Correction Flask app
Copyright (C) 2021  Abigail A. Marticio

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```