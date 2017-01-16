import json
import csv
import requests

inFile = open('test.csv', "rb")
reader = csv.reader(inFile)

documents = []
for i, row in enumerate(reader):
    text = row[1]
    record = {"id": i, "text": text}
    documents.append(record)

data = {}
data['documents'] = documents
data['stopWords'] = []
data['stopPhrases'] = []

json_data = json.dumps(data)

headers = {'Ocp-Apim-Subscription-Key': 'API-KEY', 'Content-Type': 'application/json', 'Accept': 'application/json'}

r = requests.post('https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/topics', headers=headers, data=json_data)
print r.content
print r.headers['operation-location']
