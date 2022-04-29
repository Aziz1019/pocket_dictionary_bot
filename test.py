# import wikipedia
#
# wikipedia.set_lang("uz")
# print(wikipedia.search("Tashkent"))
#
# print(wikipedia.summary("Toshkent"))
# import json
# import requests
#
# options = ['bla', 'bla2', 'bla3']
# token = "5219586926:AAHZdk7HgBHGKIILCqtqJAUFbociulB4nyQ"
# chat_id = 393340108
# question = 'What is your name?'
# uri = f'https://api.telegram.org/bot{token}/sendPoll?chat_id={chat_id}&' \
#       f'question={question}&options={json.dumps(options)}'
#
# r = requests.get(uri)
# print(r.status_code)
# res = r.json()
# print(res)

# EXCHANGE RATE API

# import requests
#
# # Where USD is the base currency you want to use
# url = 'https://v6.exchangerate-api.com/v6/bab2fce81b9cfbfcfb06c591/pair/USD/UZS'
#
# # Making our request
# response = requests.get(url)
# data = response.json()
#
# # Your JSON object
# # print(data)
#
# currency = data['conversion_rate']
#
# print(f"Today: 1 dollar is {currency} sums")


import requests
#
# tafsir = "uzb-muhammadsodikmu"
# sura = 1
# oyat = 1
# url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/{sura}/{oyat}.json"
#
# response = requests.get(url)
#
# print(response.status_code)
#
# data = response.json()
#
# text = data['text']
#
# print(text)

# city='namangan'
#
# url = f"https://api.pray.zone/v2/times/today.json?city={city}&school=5"
# r = requests.get(url)
# print(r.status_code)
#
# res = r.json()
# print(res['results']['datetime'][0]['times'])
#
# print(f"Shom namozi vaqti: {res['results']['datetime'][0]['times']['Maghrib']}")


# Using Dictionary API via Python code
# from pprint import pprint as print
app_id = "8a0159b2"
app_key = "3ccee657c84498785dac6063f84f49d4"
language = "en-gb"

word_id = "orange"
url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
print(r.status_code)

res = r.json()

print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
print(res['results'][1]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
print(res['results'][2]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])

print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])
