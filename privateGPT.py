#!/usr/bin/env python3
import json
import os
import argparse
from ingest import load_single_document
from langchain.llms import GPT4All, LlamaCpp
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.embeddings import HuggingFaceEmbeddings

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
model_n_batch = int(os.environ.get('MODEL_N_BATCH', 8))

def parse_arguments():
    parser = argparse.ArgumentParser(description='privateGPT: Ask questions to your documents without an internet connection, '
                                                 'using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')

    parser.add_argument("--mute-stream", "-M",
                        action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')

    return parser.parse_args()

def extract_text_from_answer(answer):
    if "texts" in answer:
        return "\n".join(answer["texts"])
    return ""

def generate_text_with_llm(llm, query):
    answer = llm.generate([query])
    return extract_text_from_answer(answer)

def privateGPT(input_data, type="text"):
    try:
        # Parse the command line arguments
        args = parse_arguments()
        embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
        
        # activate/deactivate the streaming StdOut callback for LLMs
        callbacks = [] if args.mute_stream else [StreamingStdOutCallbackHandler()]
        
        # Prepare the LLM
        llm = None
        if model_type == "GPT4All":
            llm = GPT4All(model=model_path, max_tokens=model_n_ctx, backend='gptj', n_batch=model_n_batch, callbacks=callbacks, verbose=False)
        else:
            return json.dumps({ "response": f"Model type {model_type} is not supported. Please choose GPT4All.", "status": "error" }) 
        
        query = ""
        if type == "text":
            query = input_data
        elif type == "file":
            query = load_single_document(input_data)

        response = llm.generate([query])
        response = response.json()
        json_str = json.loads(response)['generations'][0][0]['text']

        return json.dumps({"response": json_str, "type": "text", "status": "ok"})
    except Exception as e:
        return json.dumps({ "response": str(e), "status": "error" }) 

if __name__ == "__main__":
    input = input("Enter your request ...")
    print(privateGPT(input))