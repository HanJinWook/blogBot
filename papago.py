import urllib.request
import json


client_key = [
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
    {'client_id': 'YOUR_CLIENT_ID_1', 'client_secret': 'YOUR_CLIENT_SECRET_1'},
]


def run_translate(client_id: str, client_secret: str, english_text: str) -> str:  # 입력값 : CLIENT_ID, CLIENT_SECRET, 영어글
    print("영어글자수 : ", len(english_text))

    text = urllib.parse.quote(english_text)
    data = "source=en&target=ko&text=" + text  # 영어를 한글로 번역
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)

    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if rescode == 200:
        response_body = response.read()
        response_decode = response_body.decode('utf-8')
        response_json = json.loads(response_decode)
        result = response_json['message']['result']['translatedText']
        print(result)
        return result
    else:
        print("Error Code : " + rescode)

# Test Code - 영어 문장을 한글로 번역
# source = "I go school."
# print(run_translate(client_key[0]['client_id'], client_key[0]['client_secret'], source))
