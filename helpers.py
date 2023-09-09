import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid

from flask import redirect, render_template, session
from functools import wraps

def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
