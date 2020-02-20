# Ideal Status

Ideal Status is a platform to manage your websites status.


## Installation

After all, you need to create your environment and config your configuration file:

```bash
pip install virtualenv
virtualenv env
source env/bin/activate

pip install -r requirements.txt
```

```bash
cp config.default.py config.py
nano config.py
```
Set your secret key

```python
SECRET_KEY = ''
```

Now you need to create the database using sqlite3, run the following commands:
```bash
python
```

```python
from app import db, app

db.create_all(app=app)

exit()
```

To deactivate your enviroment run the following command:
```bash
deactivate
```

## License
[MIT](https://mit-license.org/)
