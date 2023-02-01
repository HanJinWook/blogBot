import openai


openai.api_key = "YOUR_OPENAI_KEY"


def make_subject(keyword, cnt):
  question = "I will make blog articles about '" + keyword + "'. Please make " + str(cnt) + " topics without numbering. And separate it with commas with no new line."
  # question = keyword + " Tell me " + str(cnt) + " of the most popular TED Talk titles and speakers' names in 2020. give me the list without numbering. and give it in the form of 'Title' by 'Name'. And separate it with commas with no new line."
  print(question)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  print(response)
  li = response['choices'][0]['text'].strip()
  subject_trim = li.replace(", ", ",")
  subject_list = list(subject_trim.split(","))
  return subject_list

# Test Code
# subject_result = make_subject('Music', 3)
# print(subject_result)


def make_article(subject, words=2000):
  question = "Write a long blog article about '" + subject + "' around " + str(words) + " words in markdown format. And include subtitles and detail description. In writing that seems to have a high exposure to Google search."
  # question = "Write a blog article about TED talk named '" + subject + "' around " + str(words) + " words in markdown format. And include youtube link, ted.com link, subtitles and detail description. In writing that seems to have a high exposure to Google search."
  print(question)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  print(response)
  article = response['choices'][0]['text']
  return article

# Test Code
# article_result = make_article('Famous Singer in Korea', 200)
# print(article_result)


def make_tag(text, cnt=5):
  question = "I'm writing a blog article. And article's title is '" + str(text) + "'. Please make " + str(cnt) + " tags that goes well with this article in Korean. And separate it with comma. And leave out # symbol."
  print(question)
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question,
    temperature=0.7,
    max_tokens=4000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  print(response)
  tag = response['choices'][0]['text']
  return tag

# Test Code
# text = "Famous Singer in Korea"
# tag_result = make_tag(text, 5)
# print(tag_result)
