import re
lines = []
n = int(input("enter n: "))
f = open("data.txt", "r")
for x in f:
    num = re.findall('[0-9]+', x)[-1]
    lines.append(f"{x[:-(len(num)+1)]}{int(num)+n}\n")
f.close()
result = open("result.txt", "w")
for x in lines:
    result.write(x)
result.close()
