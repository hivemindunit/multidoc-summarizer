import json
from loguru import logger
import numpy as np
from nltk import sent_tokenize
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
nltk.data.path.append('./nltk_data')

def endpoint(event, context):
    try:
        request = json.loads(event["body"])
        input_documents = request.get("documents")
        assert input_documents, f"`documents` is required"
        logger.info('Request: ')
        logger.info(input_documents)

        documents_number = len(input_documents)
        documents = '\n\n'.join(input_documents)
        print(documents, flush=True)
        parser = PlaintextParser.from_string(documents, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences_number = int(documents_number * 0.42)
        logger.info(summary_sentences_number)
        summary = summarizer(parser.document, summary_sentences_number)
        processed_documents = []
        for index, doc in enumerate(input_documents):
            included_in_summary = False
            for sentence in summary:
                if str(sentence) in doc:
                    included_in_summary = True
#                     doc = str(sentence)
                    processed_documents.append(doc)
        response = processed_documents
        logger.info('Response: ')
        logger.info(response)

        # https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-integration-settings-integration-response.html
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps(response),
        }
    except Exception as e:
        logger.error(repr(e))

        # https://docs.aws.amazon.com/apigateway/latest/developerguide/handle-errors-in-lambda-integration.html
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
            },
            "body": json.dumps({"error": repr(e), "event": event, "context": context}),
        }

if __name__ == "__main__":
    print(endpoint({"body": json.dumps({"query": "vacation"})}, None)["body"])