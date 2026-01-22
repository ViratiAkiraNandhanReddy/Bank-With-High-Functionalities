import os
import json
import logging

try:

    with open(

        fr'{ os.environ.get('LOCALAPPDATA') }\Bank-With-High-Functionalities\database\json\administrative files\config.json'
        
        ) as config: CONFIGURATION_JSON: dict = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}

# ---  --- #

match CONFIGURATION_JSON.get('DATABASE TYPE'):

    case 'JSON': from .JSON import SERVER
    case 'MySQL': from .MySQL import SERVER
    case 'SQLite3': from .SQLite3 import SERVER

__all__ = ['SERVER']
