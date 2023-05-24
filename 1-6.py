from yfjj import dic
def stemmer(s):
    for i in ['胶囊','颗粒','口服液','合剂','滴丸','片','丸','散','水','膏','饮','浆']:
        if i in s:
            b=s.find(i)
            return(s[:b])
            break
    return(s)
ywlist=['天王补心丸','柏子养心丸','枣仁安神颗粒']
for i in ywlist:
    med_name=stemmer(i)
    for j in dic:
        if med_name in j:
            print(i, j, dic[j])
