# program copied from pythonbook.pdf--book
# phil welsby 26 december 2018

name = input('Enter file name: ')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('Most common word =',bigword)
print('Number of occurances =',bigcount)

