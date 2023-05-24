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
    
    if '组  成' in line:
        tmp=[]
        b4=line.index('：')
        newl=line[b4+1:]
        newl=newl.replace('、',' ')
        newl=newl.replace('﹑',' ')
        newl=newl.replace('。',' ')
        zucheng=newl.split()
        dic[fangming]=[leibie,zucheng] 
    i+=1

counter={}
for i in dic:
    for j in dic[i][1]:
        if j in counter:
            counter[j]+=1
        else:
            counter[j]=1

sorted_dict = {}
sorted_keys = sorted(counter, key=counter.get, reverse=True) 
for i in sorted_keys:
    sorted_dict[i] = counter[i]
for i in sorted_dict:
    print(i, sorted_dict[i])