with open('zadania maturalne czerwiec 2021/napisy.txt', 'r') as f: txt = [x.rstrip() for x in f]

print('Zad 1',len([y for x in txt for y in x if y.isdigit()]))
print('Zad 2',''.join([txt[x][int(x/20)] for x in range(19, len(txt), 20)]))
# print('Zad 3',''.join([(x)[24]  for x in txt if x+x[0] == ''.join(list(reversed(x+x[0]))) or x[-1]+x == ''.join(list(reversed(x[-1]+x)))]))
print('Zad 3',''.join([x[25] if x+x[0] == ''.join(list(reversed(x+x[0]))) else x[24] if x[-1]+x == ''.join(list(reversed(x[-1]+x))) else '' for x in txt]))
vv = []
for x in txt:
    cc = [q for q in x if q.isdigit()]
    if len(cc)%2 != 0:
        cc.pop()
        vv += cc
    else:
        vv += cc
# odp = (''.join(list(map(lambda y: chr(int(y)), list(filter(lambda x: int(x) >= 65 and int(x) <= 90,[vv[x]+vv[x+1] for x in range(0,len(vv)-1,2)])))))).split('XXX')
print('Zad 4',(''.join(list(map(lambda y: chr(int(y)), list(filter(lambda x: int(x) >= 65 and int(x) <= 90,[vv[x]+vv[x+1] for x in range(0,len(vv)-1,2)])))))).split('XXX')[0]+'XXX')
