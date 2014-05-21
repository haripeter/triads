filename='C:/Users/Peti/Desktop/Network Lab/Triadok/E.txt'


f=open(filename, 'r')
line=f.readlines()
header=[]
adat=[]
adat2=[]
adat3=[]
adat4=[]
lista=[]
#levágja a headert és megtisztítja
for i in line:
    lista.append(i.split('\t'))
for i in lista[0]:
    if len(i)>0:
        header.append(i)
header=[i.strip('\n') for i in header]
#print(header)
#levágja az első oszlopot:
for i in lista:
    adat=lista[1:]
#print(adat)
#levágja az első sort:
for i in adat:
    adat2.append(i[1:])
#kivágja az utolsó oszlopot:
for i in adat2:
   adat3.append(i[-1])
#kivágja a newline chart az utolsó oszlopból:
for i in adat3:
    if len(i) > 1:
        adat4.append(i[:-1])
    else:
        adat4.append(i)
#maaagic: a letisztított utolsó oszlopot bevágja az newlinecharos utolsó oszlop helyére:
g=0
for i in adat2:
    i[-1]=adat4[g]
    g=g+1
#making int in list of lists instead of str; adat5=a végleges, letisztított adatmátrix fuckyeah
adat2=[[int(g) for g in x] for x in adat2]
original_matrix=adat2

data2=[[i if i == 0 else 1 for i in x] for x in original_matrix]

#*******************
#hibakezelés
for m in range(len(data2)):
    if data2[m][m] != 0:
        print("hibás adatfájl, error, failure in file")

#********************
kl=0
for x in range(len(data2)):
    for y in range(len(data2)):
        for z in range(len(data2)):
            if (data2[x][y] == data2[z][y] and data2[x][y] == data2[x][z]) or (data2[x][y] == data2[y][z] and data2[x][z] == data2[x][y]):
                if data2[x][y]>0:
                    kl=kl+1

#print(kl)
nof_nodes=len(data2)
#print(len(data2))
freq_of_triads=(kl/2)/((nof_nodes*(nof_nodes-1)*(nof_nodes-2))/6)
print("Frequency of triads: ", freq_of_triads)
