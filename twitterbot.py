# Import required libraries

import tweepy
import urllib3
import xmltodict

# Set keys for access
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Make client as object
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Access website and pull data
http = urllib3.PoolManager()
r = http.request('GET', 'http://hamqsl.com/solarxml.php')


# Make sense of data
doc = xmltodict.parse(r.data)

updated = doc['solar']['solardata']['updated']
solarIndex = doc['solar']['solardata']['solarflux']
topband = doc['solar']['solardata']['calculatedconditions']['band'][0]['#text']
thirty = doc['solar']['solardata']['calculatedconditions']['band'][1]['#text']
seventeen = doc['solar']['solardata']['calculatedconditions']['band'][2]['#text']
twelve = doc['solar']['solardata']['calculatedconditions']['band'][3]['#text']
topbandn = doc['solar']['solardata']['calculatedconditions']['band'][4]['#text']
thirtyn = doc['solar']['solardata']['calculatedconditions']['band'][5]['#text']
seventeenn = doc['solar']['solardata']['calculatedconditions']['band'][6]['#text']
twelven = doc['solar']['solardata']['calculatedconditions']['band'][7]['#text']


# Build string
messText = """HF Propagation Report
Updated at {}

SFI: {}

Band            Day        Night
80m-40m   {}     {}
30m-20m   {}     {}
17m-15m     {}     {}
12m-10m     {}     {}

Data from hamqsl.com
#testing #HFProp"""

#Check it works!
#print(messText.format(updated, solarIndex, topband, topbandn, thirty, thirtyn,seventeen, seventeenn, twelve, twelven))


# Send tweet
response = client.create_tweet(
    text=messText.format(updated, solarIndex, topband, topbandn, thirty, thirtyn,seventeen, seventeenn, twelve, twelven)
)
