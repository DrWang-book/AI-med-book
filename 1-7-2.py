import codecs
fi = codecs.open('/Users/dawanga/Documents/lx/python/yfjju8.txt', encoding='UTF-8')
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

for i in dic:
    print(i,  dic[i])