import tweepy
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

nextYear = int(datetime.datetime.now().year) + 1
now = datetime.datetime.now().date()
##- Counting Days
dayCount = datetime.date(nextYear - 1, 12, 31) - datetime.date.today()
daysLeft = str(dayCount).replace(", 0:00:00","")

dayLeftYear = f"{daysLeft} days left to {nextYear}!"

if str(daysLeft) == '0:00:00':
    dayLeftYear = "Happy New Year 🥳"


response = client.create_tweet(text=f"Today Date Is {str(now)} (GMT), and {dayLeftYear}")

print(response)