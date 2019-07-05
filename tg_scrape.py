from telethon.sync import TelegramClient
import csv

api_hash = "" #API Hash
api_id = "" # API ID

today = ["2019-06-29", "2019-07-01"] #Fill in depending on the day (format yyyy-mm-dd)
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
