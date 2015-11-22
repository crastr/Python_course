__author__ = 'Alex'
with open("yazkora.txt", "r") as f:
    text = f.read()
sentences = text.replace('\n', ' ')
sentences = sentences.split('.')
answer = [' ']
for line in sentences:
    words = line.split(' ')
    for word in words:
        if word[-2::] == 'yo':
            answer.append(word)
    answer.append('\n')
with open("answer.txt", "w") as n:
    n.write(' '.join(answer))




