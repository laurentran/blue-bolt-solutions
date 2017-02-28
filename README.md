## Topic Detection to Define Search Facets

This project uses the Microsoft Cognitive Services Topic Detection API, within the Text Analytics API suite, to detect topics across a corpus of text documents.  The most common topics detected are defined as search facets for indexing the documents in the corpus.

In [request.py](https://github.com/laurentran/blue-bolt-solutions/blob/master/request.py), we format the data and make the API call to Cognitive Services. The results from the API call are shown in [response.json](https://github.com/laurentran/topic-detection/blob/master/response.json).  

## Azure Function and Keyphrase Extraction to Assign Search Facets

Once the search facets are defined using topic detection, they are stored in an Azure Table.  When a new text document is added to Blob storage, an Azure Function, called `assignTopic`, is triggered to call the Cognitive Services Keyphrase Extraction API.  The keyphrases returned are matched against the list of defined search facets in order to assign facets to the new document.  The function writes the matching topics to DocumentDB.

The function code is found in [assignTopic](https://github.com/laurentran/blue-bolt-solutions/blob/master/assignTopic/)

# License

Licensed using the MIT License (MIT); Copyright (c) Microsoft Corporation. For more information, please see [LICENSE](https://github.com/laurentran/blue-bolt-solutions/blob/master/LICENSE)
