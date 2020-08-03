lines = []
while True:
    s = input("write sth : ")
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)