from telethon.sync import TelegramClient
import csv
import pandas as pd
import time

api_hash = "" #API Hash
api_id = "" # API ID

range_to_search = pd.date_range("2019-06-28", "2019-07-03").tolist() #Replace dates depending on the timespan
today = [str(i)[:10] for i in range_to_search]

destinations = {
'Name':'Link', 
} #Add desired name + link as required

word_to_search = "" #search query goes here

with open('chats.csv', 'w') as file:
	file = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	file.writerow(['date','count'])

	for i in today:
		msg_total = 0
		for destination, key in destinations.items():
			with TelegramClient("scrape", api_id, api_hash) as client:
				for k in client.get_messages(client.get_entity(key), 1000, search=word_to_search):
					if str(k.date)[:10] == i:
						print(f"{k.message}\n")
						msg_total += 1
		file.writerow([i, str(msg_total)])
		time.sleep(120)
