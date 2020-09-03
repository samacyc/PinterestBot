import json


with open('backup.json' ,'rb') as f : 
    data = json.load(f)

page = []
for info in data['Pages']: 
    page.append(info['page'])

print(page)

print(json.dumps({
    "Page" : page
}))