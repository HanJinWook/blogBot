import requests
import json


# https://unsplash.com/oauth/applications 에서 확인
access_key = 'YOUR_ACCESS_KEY'


def get_image(key: str):  # 이미지 뽑기 연습
    url = 'https://api.unsplash.com/photos/?' + 'client_id=' + key
    response = requests.get(url, verify=False)
    print(response.status_code)
    print(response.text)
    return response

# Test Code
# get_image(access_key)


def random_image(query, count, key):  # 쿼리와 일치하는 랜덤 이미지 뽑기
    url = 'https://api.unsplash.com/photos/random?' + 'client_id=' + key
    parameters = {
        # 'collections': '',
        # 'topics': '',
        # 'username': '',
        'query': query,
        # 'orientation': '',
        # 'content_filter': '',
        'count': str(count)
    }
    response = requests.get(url, params=parameters, verify=False)
    print(response.status_code)
    print(response.text)
    json_object = json.loads(response.text)
    html_url = ''
    for i in range(int(count)):
        html_url += '<img src=' + json_object[i]['urls']['small'] + ' />\n'
    print(html_url)
    return html_url

# Test Code
# random_image('Computer', 3, access_key)
