import tweepy
import secret
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCSESS_TOKEN"),
    access_token_secret=os.getenv("ACCSESS_TOKEN_SECRET")
)   

nextYear = 2023
now = datetime.datetime.now().date()
##- Counting Days
dayCount = datetime.date(nextYear, 1, 1) - datetime.date.today()
daysLeft = str(dayCount).replace(", 0:00:00","")

dayLeftYear = f"{daysLeft} days left to {nextYear}!"
if daysLeft == 0:
    daysLeftYear = "Happy New Year 🥳"
    nextYear += 1

response = client.create_tweet(text=f"Today Date Is {str(now)} (GMT), and {dayLeftYear}")

print(response)