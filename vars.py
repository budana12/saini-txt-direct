#AMIT
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "10768857"))
API_HASH = environ.get("API_HASH", "81b5d675d410f16ceb39df10db9cdb54")
BOT_TOKEN = environ.get("BOT_TOKEN", "8122988957:AAERn_Imc3FoLmCox3GgziJNxju-rIbnCW8")
OWNER = int(environ.get("OWNER", "6520378417"))
CREDIT = "AMIT"
AUTH_USER = os.environ.get('AUTH_USERS', '6520378417').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
