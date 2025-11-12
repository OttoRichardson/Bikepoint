
import os
import sys
from dotenv import load_dotenv
import boto3
import json
import time
from datetime import datetime
import requests

from extract import extract
from load import load
print('loading functions')


url = 'https://api.tfl.gov.uk/BikePoint/'


extract(url)

load()
