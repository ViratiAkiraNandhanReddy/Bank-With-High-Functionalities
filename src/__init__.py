import os
import json
import logging
from . import __mail__
import customtkinter
from typing import Any
from .__server__ import SERVER

CONSTANTS: dict[str, dict[str, Any]] = {
    
    'WEBSITES' : {

        'GITHUB_REPOSITORY' : 'https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities',
        'PROJECT_WEBSITE' : 'https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/',

    },

    'SOCIALS' : {

        'GITHUB' : 'https://github.com/ViratiAkiraNandhanReddy',
        'INSTAGRAM' : 'https://www.instagram.com/viratiakiranandhanreddy',
        'TWITTER' : 'https://twitter.com/akiranandhan_',
        'LINKEDIN' : 'https://www.linkedin.com/in/viratiakiranandhanreddy',
        'YOUTUBE' : 'https://www.youtube.com/@ViratiAkiraNandhanReddy',
        
    },

    
}

DIR_PATH = str(os.environ.get('LOCALAPPDATA')) + r'\Bank-With-High-Functionalities'

try:

    with open(fr'{DIR_PATH}\database\json\administrative files\config.json','r') as config:
        CONFIGURATION_JSON: dict[str, Any] = json.load(config)

except FileNotFoundError, json.JSONDecodeError:

    CONFIGURATION_JSON = {}