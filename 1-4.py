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
        if leibie not in dic:
            dic[leibie]=[fangming]
        else:
            dic[leibie].append(fangming)
    i+=1

for i in dic:
#print(i, len(dic[i]), dic[i])
    print(i,'\t', len(dic[i]))
