import requests
import string

version = '1.20.1'
categories = 'forge'
project_type ='mod'
limit = 20
offset = 0
index = 'relevance'

response = requests.get(f'''https://api.modrinth.com/v2/search?
facets=[["categories:{categories}"], 
["project_type:{project_type}"], 
["version={version}"]]&
index={index}&
offset={offset}&
limit={limit}
''')

if response.status_code == 200:
    data = response.json()

    for i in range(len(data['hits'])):
        versions = data['hits'][i]['versions']
        versions_list = [i for i in versions if i.replace('.', '').isdigit()]
        with open(file='mods.txt', mode='a', encoding='utf-8') as file:
            print(f'''
Название - {data['hits'][i]['title']}
Описание - {data['hits'][i]['description']}
Категории - {data['hits'][i]['categories']}
Версии - {versions_list}
Кол-во загрузок - {data['hits'][i]['downloads']}
Подписчиков - {data['hits'][i]['follows']}
Последние обновление - {data['hits'][i]['date_modified']}\n
''')
