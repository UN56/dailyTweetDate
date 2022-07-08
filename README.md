# dailyTweetDate
tweets daily about date information on GMT  

check the [demo](https://twitter.com/DailyDateBot)

## Usage

clone repo  
`git clone https://github.com/UN56/dailyTweetDate.git`

`cd dailyTweetDate`

run  
`pip install -r requirements.txt`  

on the Twitter developer dashboard activate `OAuth 1.0a`  

create `.env` file and put your twitter token  
`API_KEY = "Your-Api-Key"`  
`API_KEY_SECRET = "Your-Secret-Api-KEY"`  
`BEARER_TOKEN = "Your-Bearer-token"`  
`ACCSESS_TOKEN = "Your-Accsess-Token"`  
`ACCSESS_TOKEN_SECRET = "Your-Secret-Accsess-Token"`  

if you run on a server, run  
`python scheduler.py` or use DockerFile  

if you run locally and just see if it works, run  
`python main.py`  