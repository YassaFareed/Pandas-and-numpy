import urllib.request 
import json

json_url = 'http://py4e-data.dr-chuck.net/comments_405296.json'

data = urllib.request.urlopen(json_url).read().decode()
js = json.loads(data)

s = 0
total_number = 0

for comment in js["comments"]:
    s = s + int(comment["count"])
    total_number += 1

print('Count:',total_number)
print('Sum:',s)