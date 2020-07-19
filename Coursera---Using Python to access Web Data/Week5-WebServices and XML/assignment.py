import xml.etree.ElementTree as ET
import urllib.request

url = "http://py4e-data.dr-chuck.net/comments_405295.xml"
xml = urllib.request.urlopen(url).read()

stuff = ET.fromstring(xml)
lst = stuff.findall('comments/comment')
print('User count:', len(lst))

x=[]
for item in lst:
    x.append(int(item.find('count').text))
    
print(sum(x))