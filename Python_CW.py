ss='abc' #1
print(ss[::-1])
ss2='Hel"lo Wor"ld!' #2
begin=0
end=0
flag=0
for i in range(0,len(ss2),1):
    if ss2[i]=='\"':
        if flag==0:
            begin=i
            flag=1
        else:
            end=i
print(ss2[begin+1:end])
s='9' #3
s=int(s)
s*=2
print(s)
ss4='15263654 365467474'  #4
space=ss4.find(" ")
ss4_mod=ss4[space+1:]+" "+ss4[:space]
print(ss4_mod)
ss5="nikita.garmashov@mail.ru" #5
sobaka=ss5.find("@")
print(ss5[:sobaka])
ss6="+7 (812) 134-12-324" #6
ss6_mod=''
for i in range(0,len(ss6),1):
    if ss6[i]!='-' and ss6[i]!=' ' and ss6[i]!='(' and ss6[i]!=')':
        ss6_mod+=ss6[i]
print(ss6_mod)
ss7="а роза упала на лапу Азора" #7
ss7_mod=''
for i in range(0,len(ss7),1):
    if ss7[i]!=' ':
        ss7_mod+=ss7[i]
ss7_mod=ss7_mod.lower()
if ss7_mod[::-1]==ss7_mod:
    print('Полином')
else:
    print('Не полином')


file = open("animals.txt")
Animals = list();
for Animal in file:
  Animals.append(Animal)

Uniq = list()


for a in range(5):
  for b in range(a,5):
    if(Animals[a].split()[1] == Animals[b].split()[1] and Animals[a].split()[2] != Animals[b].split()[2] and Uniq.count(Animals[a].split()[1]) == 0):
        Uniq.append(Animals[a].split()[1])

AnimalNumb = dict()
for a in range(6):
  if(Animals[a].split()[1] not in AnimalNumb.keys()):
    AnimalNumb[Animals[a].split()[1]] = 1
  else:
    AnimalNumb[Animals[a].split()[1]] += 1

CountSorted = sorted(AnimalNumb.items(), key=lambda x: x[1], reverse = 1)
    
AnimalSorted = sorted(Uniq, key = len)
print(AnimalSorted)
print(CountSorted)

file.close()
