import os
import json

APP_HOME = os.getenv("APP_HOME", os.path.dirname(__file__))
print(APP_HOME)
configs = json.load(open(os.path.join(APP_HOME, 'config.json')))
