import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'GreyMatters_Bot'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://alphanakflix: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@github.com/alphanakflix/netflix_tvshowsbot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 main.py &")
