import markdown
import tistory
import chat_gpt
import unsplash

# https://YOUR_BLOG_NAME.tistory.com
blog_name = 'YOUR_BLOG_NAME'  # 티스토리 블로그 이름


# 키워드 기반으로 자동 글쓰기
def post_blog_by_keyword(keyword: str, count: str, expose: str):  # 주제, 작성 개수, 게시글 노출 여부(0: 비공개, 3: 공개)

    token = tistory.token_value(blog_name)  # 티스토리 토큰
    access_key = unsplash.access_key(blog_name)  # Unsplash 액세스 키

    # 키워드 기반으로 주제 n개 뽑기
    subject_keyword = keyword  # 키워드
    subject_number = count  # 뽑을 주제 개수
    subject_result = chat_gpt.make_subject(subject_keyword, subject_number)  # 키워드와 연관된 주제 뽑기
    print("subject_result : ", subject_result)

    # 주제에 어울리는 글 작성
    article_en_list = []
    article_words = '2000'  # 블로그 글 words 숫자

    for item in subject_result:
        article_result = chat_gpt.make_article(item, article_words)  # 주제 기반으로 게시글 작성
        article_en_list.append(article_result)
    print("article_en_list : ", article_en_list)

    for i in range(len(article_en_list)):
        title_en = subject_result[i]
        article_en = article_en_list[i]

        img = unsplash.random_image(title_en, 5, access_key)  # 제목과 어울리는 이미지 찾기
        blog_sum = img + article_en  # 이미지와 게시글 내용을 합치기
        html = markdown.markdown(blog_sum)  # 마크다운 -> HTML
        tag = chat_gpt.make_tag(title_en, '4')  # 태그 4개 생성
        tistory.post_blog(title_en, html, tag, expose, blog_name)  # 티스토리 글쓰기


if __name__ == '__main__':
    post_blog_by_keyword('Successful investment method', '5', '3')  # 성공적인 투자 방법이라는 키워드로 공개글 5개 쓰기
