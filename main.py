import markdown
import tistory
import chat_gpt
import unsplash


user = "jino"


def post_blog_using_keyword(input_keyword: str, input_cnt: int, input_expose: str):

    blog_name = tistory.blog_name(user)
    token = tistory.token(user)
    access_key = unsplash.access_key(user)

    # 키워드 기반으로 주제 n개 뽑기
    subject_keyword = input_keyword  # 키워드
    subject_number = input_cnt  # 뽑을 주제 개수
    subject_result = chat_gpt.make_subject(subject_keyword, subject_number)
    print("*****subject_result : ", subject_result)

    # 주제에 어울리는 글 작성
    article_en_list = []
    article_words = 2000  # 블로그 글 words 숫자

    for item in subject_result:
        article_result = chat_gpt.make_article(item, article_words)
        article_en_list.append(article_result)
    print("*****article_en_list : ", article_en_list)

    for i in range(len(article_en_list)):
        title_en = subject_result[i]
        article_en = article_en_list[i]

        img = unsplash.random_image(title_en, 5, access_key)

        blog_sum = img + article_en

        html = markdown.markdown(blog_sum)  # 마크다운 -> HTML

        # tag_y = chat_gpt.make_tag(title_en, 4)
        tag_n = ""

        tistory.post_blog(title_en, html, tag_n, input_expose, blog_name, token)


if __name__ == '__main__':
    post_blog_using_keyword('Successful investment method', 3, '3')
