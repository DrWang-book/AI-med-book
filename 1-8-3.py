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

def jac_sim(a,b):
    inter=0
    for i in a:
        if i in b:
            inter+=1
    return(round((inter/(len(a)+len(b)-inter)),2))

bzyxw=['柏子仁','党参','炙黄芪','川芎','当归','茯苓','制远志','酸枣仁','肉桂','醋五味子','半夏曲','炙甘草','朱砂']
sim_dic={}
for i in dic:
    sim_dic[i]=jac_sim(bzyxw, dic[i][1])

sorted_dict = {}
sorted_keys = sorted(sim_dic, key=sim_dic.get, reverse=True) 
for i in sorted_keys:
    sorted_dict[i] = sim_dic[i]
for i in sorted_dict:
    print(i, sorted_dict[i],dic[i])

