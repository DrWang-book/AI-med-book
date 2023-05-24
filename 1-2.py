import codecs
fi = codecs.open('yfjju8.txt', encoding='UTF-8')
lines = fi.readlines()
print(len(lines))
i=0
while i<len(lines):
    line = lines[i]
    if '方  名' in line:
         print(line[:-1])
    i+=1

