import urllib2
import csv

# If you are using Python 3+, import urllib instead of urllib2

import json


#inFile = open('test.csv', "rb")
#reader = csv.reader(inFile)

#documents = []
#for i, row in enumerate(reader):
#    text = row[1]
#    record = {"id": i, "text": text}
#    documents.append(record)

data = {
  "Inputs": {
    "input1": {
      "ColumnNames": [
        "id",
        "text"
      ],
      "Values": [
        [
          "1",
          "FAIRFAX VIRGINIAAugust 15 2015 The American Society of Cataract and Refractive Surgery ASCRS has released an official position statement opposing directives that restrict two wellestablished presurgical ophthalmic practices the use of diluted povidoneiodine solution for topical infection prophylaxis and the use of multidose topical eye drops on multiple patients The position statement developed by the ASCRS Cataract Clinical Committee comes in the wake of some surgery centers being compelled to cease certain long accepted topical treatments for preoperative patients"
        ],
        [
          "2",
          "The surgical management of cataract in the small eye presents the ophthalmic surgeon with numerous challenges An understanding of the anatomic classification in addition to a thorough preoperative assessment will help individualize each case and enable the surgeon to better prepare for the obstacles that might be encountered during surgery Small eyes are especially challenging in terms of intraocular lens IOL calculations and possible current limitations of available IOL powers which could necessitate alternative means of achieving emmetropia Surgical strategies for minimizing complications and maximizing good outcomes can be developed from knowledge of the anatomic differences between various smalleye conditions and the pathologies that may be associated with each A thorough understanding of the challenges inherent in these cases and the management of intraoperative and postoperative complications will ensure that surgeons approaching the correction of these eyes will achieve the best possible surgical results"
        ]
      ]
    }
  },
  "GlobalParameters": {}
}

json_data = json.dumps(data)

body = json_data

url = 'https://ussouthcentral.services.azureml.net/workspaces/5322e506c95346678ad7e813c222e096/services/05244412d61d45c3bc2c5947cdafd096/execute?api-version=2.0&details=true'
api_key = 'apikey' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers)

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers)
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))