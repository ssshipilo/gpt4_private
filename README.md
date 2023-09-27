
<h1 align="center">GPT 4 Private (GPT Private)</h1>

![GPT 4 Private](https://github.com/ssshipilo/gpt4_private/blob/main/git/welcome.png)

<div align="center">
  <a href="https://github.com/ssshipilo/microsoft_account/pull">
    <img src="https://img.shields.io/github/issues-pr/cdnjs/cdnjs.svg" alt="GitHub pull requests" />
  </a>
</div>

<br />

___

<div align="center">
    Using the GPT4Private model, with output to json as returned by OpenAI. The model itself cannot compete with GPT4 Open AI, but for small tasks, for process automation, it can be very useful.
</div>

## Features

- Receive answers, as text
- Process files, the file must contain a request and the text to the request
- There is an API endpoint to run the program on the server, for your programs
- Optimized code, with increased performance
- Receive the response as JSON

## Example of code operation
![GPT 4 Private](https://github.com/ssshipilo/gpt4_private/blob/main/git/example.png)

## Steps

### Download model
[Download model ggml-gpt4all-j-v1.3-groovy.bin](https://huggingface.co/qm9/ggml-gpt4all-j-v1.3-groovy.bin) 

create a `models` folder in the project root, and place the downloaded model in this folder

### Copy repository
    git clone https://github.com/ssshipilo/gpt4_private

### Dependency installation
    pip install -r requirements.txt

___

## Starting a text PrivateGPT

#### Run Windows
    python privateGPT.py

#### Run Windows
    python3 privateGPT.py

## Starting Flask server

#### Run Windows
    python main.py

#### Run Windows
    python3 main.py

## Server Usage
On the port you're running on for example as set to `localhost:56663`.
You need to make a request of the form, in case you want to give a text request to

```python
import requests

url = "http://localhost:56663/gpt"
data = {"text": "Hi, I am example code"}
response = requests.post(url, json=data)

print(response.text)
```

in the case of fileos it's the same, only you need to use the file key, example :

```python
import requests

url = "http://localhost:56663/gpt"
data = {"file": your file in bytes}
response = requests.post(url, json=data)

print(response.text)
```

I assume that you are a developer and understand why in bytes, but if not, I will explain, after the file is sent to the server in bytes it is saved in a file, then the content of this file is read by readers to get the text, and it is already passed to the GPT 4 Private bot, and then the file is deleted.


## Warning and Legal
THIS CODE IS PROVIDED IN THE FORM IN WHICH IT IS PROVIDED, AND IS PROVIDED FOR EVALUATION PURPOSES. THIS IS AN INDEPENDENT AND UNOFFICIAL PROJECT ONLY FOR EDUCATIONAL USE. TO CONVEY TO THE DEVELOPER HOW PROCESS AUTOMATION IS CREATED IN GENERAL.
