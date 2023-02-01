import requests


# https://www.tistory.com/guide/api/manage/register
key = [
    {'blogName': 'nothinkblarblar', 'app_id': 'YOUR_APP_ID', 'secret_key': 'YOUR_SECRET_KEY'},
    {'blogName': 'peachblarblar', 'app_id': 'YOUR_APP_ID', 'secret_key': 'YOUR_SECRET_KEY'},
    {'blogName': 'lifeisblarblar', 'app_id': 'YOUR_APP_ID', 'secret_key': 'YOUR_SECRET_KEY'},
]


def blog_name(user: str):
    if user == "jino":
        return key[0]['blogName']
    elif user == "charlie":
        return key[1]['blogName']
    elif user == "joe":
        return key[2]['blogName']


def token(user: str):
    if user == "jino":
        return 'YOUR_TISTORY_TOKEN'
    elif user == "charlie":
        return 'YOUR_TISTORY_TOKEN'
    elif user == "joe":
        return 'YOUR_TISTORY_TOKEN'


def get_auth_code(app_id, blog_name):
    response_type = "code"
    state = "anything"
    client_id = app_id
    redirect_uri = 'https://' + blog_name + '.tistory.com'
    url = "https://www.tistory.com/oauth/authorize?" + \
          "client_id=" + client_id + "&" + \
          "redirect_uri=" + redirect_uri + "&" + \
          "response_type=" + response_type + "&" + \
          "state=" + state
    print(url)
    return url


# 1. 토큰을 받기 위한 code 알아내기
# get_auth_code(key[0]['app_id'], key[0]['blogName'])


def get_access_token(app_id, secret_key, blog_name, code):  # code 값은 '허가하기' 클릭 이후에 나오는 값
    client_id = app_id
    client_secret = secret_key
    redirect_uri = 'https://' + blog_name + '.tistory.com'
    url = "https://www.tistory.com/oauth/access_token?" + \
          "client_id=" + client_id + "&" + \
          "client_secret=" + client_secret + "&" + \
          "redirect_uri=" + redirect_uri + "&" + \
          "code=" + code + "&" + \
          "grant_type=authorization_code"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        print("토큰 받기 성공")
        print(response.status_code)
        print(response.text)
        return response
    else:
        print("토큰 받기 실패")
        print(response.status_code)
        print(response.text)


# 2. 1번에서 알아낸 code 로 access token 받기
# code = 'GET_CODE_BY_AUTH'
# get_access_token(key[0]['app_id'], key[0]['secret_key'], key[0]['blogName'], code)


def post_blog(title, content, tag, expose, blog_name, token):
    url = 'https://www.tistory.com/apis/post/write?'
    access_token = token
    parameters = {
        'access_token': access_token,
        'output': '{output-type}',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'tag': tag,
        'visibility': expose  # (0:비공개, 3:공개)
    }
    response = requests.post(url, params=parameters, verify=False)

    if response.status_code == 200:
        print("글작성 성공")
        print(response.status_code)
        print(response.text)
    else:
        print("글작성 실패")
        print(response.status_code)
        print(response.text)


# 3. access token 으로 블로그 글쓰기
# token = 'YOUR_TISTORY_TOKEN'
# post_blog("제목", "내용", "태그", '0', key[0]['blogName'], token)


def get_list(page_num, blog_name, token):
    url = 'https://www.tistory.com/apis/post/list?'
    access_token = token
    parameters = {
        'access_token': access_token,
        'output': '{output-type}',
        'blogName': blog_name,
        'page': page_num
    }
    response = requests.get(url, params=parameters, verify=False)

    if response.status_code == 200:
        print("불러오기 성공")
        print(response.status_code)
        print(response.text)
    else:
        print("불러오기 실패")
        print(response.status_code)
        print(response.text)

# Test Code
# token = 'YOUR_TISTORY_TOKEN'
# get_list('1', key[0]['blogName'], token)


def modify_blog(post_id, title, content, tag, expose, blog_name, token):
    url = 'https://www.tistory.com/apis/post/modify?'
    access_token = token
    parameters = {
        'postId': post_id,
        'access_token': access_token,
        'output': '{output-type}',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'tag': tag,
        'visibility': expose  # (0:비공개, 3:공개)
    }
    response = requests.post(url, params=parameters, verify=False)

    if response.status_code == 200:
        print("글수정 성공")
        print(response.status_code)
        print(response.text)
    else:
        print("글수정 실패")
        print(response.status_code)
        print(response.text)

# Test Code
# token = 'YOUR_TISTORY_TOKEN'
# modify_blog('105', "제목수정", "본문수정", "", '0', key[0]['blogName'], token)
