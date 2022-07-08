# dailyTweetDate
tweets daily about date information on GMT time  

## Usage

run  
`pip install -r requirements.txt`  

on twitter developer dashboard activate `OAuth 1.0a`  

create `.env` file and put your twitter token  
`API_KEY = "Your-Api-Key"  
API_KEY_SECRET = "Your-Secret-Api-KEY"  
BEARER_TOKEN = "Yout-Bearer-token"  
ACCSESS_TOKEN = "Your-Acsess-Token"  
ACCSESS_TOKEN_SECRET = "Your-Secret-Acsess-Token"`  

if you run on a server, run  
`python scheduler.py` or use DockerFile  

if you run locally and just see if it works, run  
`python main.py`  