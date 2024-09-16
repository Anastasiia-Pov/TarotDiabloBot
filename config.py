from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ.get('TOKEN')
admin_id = os.environ.get("ADMIN_ID")
tg_url = os.environ.get("TG_URL")
git_url = os.environ.get("GIT_URL")
support = os.environ.get("SUPPORT")
