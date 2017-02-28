request = require('request')

module.exports = function (context, myBlob) {

    // get topics from Azure table
    data = context.bindings.inputTable;

    // get keyphrases from cognitive services
    var keyPhrases = [];

    requestBody = JSON.stringify({
        "documents": [
            {
            "language": "en",
            "id": context.bindingData.blobname,
            "text": myBlob
            }
        ]
    })

    // ping keyPhrase extraction API
    request.post({
        headers: {'content-type' : 'application/json', 'Ocp-Apim-Subscription-Key' : process.env.API_KEY},
        url: 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/keyPhrases',
        body: requestBody,
    }, function(error, response, body){
        if(error) {
            context.log(error);
        } else {
            keyPhrases = JSON.parse(body).documents[0].keyPhrases;

            // find matching topics
            var topics = [];
            for (var i = 0; i < data.length; i++) {
                topic = data[i].Topic;
                for(var j = 0; j < keyPhrases.length; j++) {
                    if (topic === keyPhrases[j]) {
                        topics.push(topic)
                    }
                }
            }

            // save topic assignments to DocumentDB
            context.bindings.outputDocument = {
                Topics : topics,
                DocumentName: context.bindingData.blobname,
            } 

            // end function
            context.done();
        }
    });
};