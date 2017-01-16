import requests
import json
import string
import csv

request_data = {}
request_data['size'] = 200

r = requests.post('http://{ELASTIC}/{INDEX}/_search', data=json.dumps(request_data))
data = json.loads(r.text)

with open('test.csv', 'wb') as csvfile:
    content_writer = csv.writer(csvfile)
    content_writer.writerow(['id', 'text'])
    for item in data['hits']['hits']:
        hit_id = item[u'_id']
        source = item[u'_source']
        body = None
        if source is not None and ('body' in source is not None):
            body = item[u'_source'][u'body'] #assumes _source is being saved and body exists on a document

        if hit_id is not None and body is not None:
            content_writer.writerow([hit_id, ''.join(filter(lambda x: x in string.letters + string.digits + ' <>/', body))])

