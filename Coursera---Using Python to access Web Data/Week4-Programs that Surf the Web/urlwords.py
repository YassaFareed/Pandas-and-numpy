import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # very helpul and acts as a socket 

counts = dict()
for line in fhand:
    words = line.decode().split()  # we need to decode it from utf-8 bytes to string 
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
