import requests
CONTENT_WIKI_URL = 'https://pymotw.com/3/math/index.html'
re = requests.get(CONTENT_WIKI_URL)
print(re.text)
print(re.content)
print(re.headers)
print(re.encoding)
print(re.url)
print(re.elapsed)
print(re.is_permanent_redirect)