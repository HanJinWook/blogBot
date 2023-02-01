import requests
import json


# https://unsplash.com/oauth/applications
def access_key(user: str):
    if user == "jino":
        return 'YOUR_ACCESS_KEY'
    elif user == "charlie":
        return 'YOUR_ACCESS_KEY'
    elif user == "joe":
        return 'YOUR_ACCESS_KEY'


def get_image(key):
    # https://unsplash.com/oauth/applications 에서 보이는 Access Key
    url = "https://api.unsplash.com/photos/?" + "client_id=" + key
    response = requests.get(url, verify=False)
    print(response.status_code)
    print(response.text)
    return response

# Test Code
# get_image(access_key("jino"))


def random_image(query, cnt, key):
    # https://unsplash.com/oauth/applications 에서 보이는 Access Key
    url = "https://api.unsplash.com/photos/random?" + "client_id=" + key
    parameters = {
        # 'collections': '',
        # 'topics': '',
        # 'username': '',
        'query': query,
        # 'orientation': '',
        # 'content_filter': '',
        'count': str(cnt)
    }
    response = requests.get(url, params=parameters, verify=False)
    print(response.status_code)
    print(response.text)
    json_object = json.loads(response.text)
    html_url = ""
    for i in range(int(cnt)):
        html_url += "<img src=" + json_object[i]['urls']['small'] + " />\n"
    print(html_url)
    return html_url

# Test Code
# random_image('computer', 3, access_key("jino"))
