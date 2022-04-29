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
