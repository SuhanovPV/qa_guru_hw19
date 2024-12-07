import os

from dotenv import load_dotenv

load_dotenv()

bstack_username = os.getenv('name')
bstack_accesskey = os.getenv('access_key')
project = os.getenv('project_name')
timeout = os.getenv('timeout')
app = os.getenv('app')
