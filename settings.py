import os
import json
from datetime import datetime
import pandas
import talib as ta
import numpy as np
from googlefinance import getQuotes
from dotenv import load_dotenv
load_dotenv()