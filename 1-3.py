import codecs
fi = codecs.open('yfjju8.txt', encoding='UTF-8')
lines = fi.readlines()
print(len(lines))
i=0
while i<len(lines):
    line = lines[i]
    if '方  名' in line:
        b1 = line.find('：')
        b2 = line.find('（')
        b3 = line.find('）')
        fangming = line[b1+1:b2]
        leibie = line[b2+1:b3]
        print(fangming, leibie)
    i+=1

