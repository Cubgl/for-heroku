from pprint import pprint

from requests import get, post, delete

# pprint(get('http://localhost:8080/api/v2/news/2').json())

pprint(get('http://localhost:8080/api/v2/news').json())

# pprint(post('http://localhost:8080/api/v2/news',
#            json={'title': 'Заголовок'}).json())

# pprint(post('http://localhost:8080/api/v2/news',
#            json={'title': 'Добрый вечер!',
#                  'content': 'А Вы знакомы с "Людмилой - Добрый вечер"?',
#                  'user_id': 1,
#                  'is_published': False,
#                  'is_private': False}).json())

# pprint(delete('http://localhost:8080/api/v2/news/2').json())