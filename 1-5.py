import codecs
fi = codecs.open('yfjju8.txt', encoding='UTF-8')
lines = fi.readlines()
print( len(lines) )
dic={ }
i=0
while i<len(lines):
    line = lines[i]
    if '方  名' in line:
        b1 = line.index('：')
        b2 = line.index('（')
        b3 = line.index('）')
        fangming = line[b1+1:b2]
        leibie = line[b2+1:b3]
        if fangming not in dic:
            dic[fangming]=[leibie]
        else:
            dic[fangming].append(leibie)
    i+=1

for i in dic:
    if len(dic[i])>1:
        print(i, len(dic[i]), dic[i])