from fractions import Fraction

f=open("matan.txt",'r+')
s=f.readline()
sp=[s[i] for i in range(len(s)) if (s[i]!="*" and s[i]!="x" and s[i]!="," and s[i]!=" " and s[i]!='\n')]
s1=[]
for i in range(len(sp)):
    if (sp[i]=="["):
        index1=sp.index(sp[i])
s1=''.join(sp[index1+1:-1:]).split(";")
s1=[int(i) for i in s1]
del sp[index1::]
step2=[]
coefficient=[]
degree=[]
for i in range(1,len(sp)):
    if (sp[i]=="^" or sp[i]=="-" or sp[i]=="+"):
        step2.append(i)
step2.insert(0,0)
step2.append(len(sp))
k=0
p=[]
for i in range(len(step2)-1):
    if (k%2==0):
        if '/' in ''.join(sp[step2[i]:step2[i+1]]):
            p=''.join(sp[step2[i]:step2[i+1]]).split("/")
            coefficient.append(Fraction(int(p[0]),int(p[1])))
        else:
            coefficient.append(float(''.join(sp[step2[i]:step2[i+1]])))
    else:
        degree.append(int(''.join(sp[step2[i]+1:step2[i+1]])))
    k+=1
suma=sumb=0
a=s1[0]
b=s1[1]
for i in range(len(degree)):
    degree[i]+=1
    coefficient[i]/=degree[i]
    suma+=a**degree[i]*coefficient[i]
    sumb+=b**degree[i]*coefficient[i]
integ=str(sumb-suma)
f.write('\nОпределённый интеграл = '+integ)
f.close()
