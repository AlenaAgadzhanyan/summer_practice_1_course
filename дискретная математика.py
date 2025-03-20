import math

f=open("discretka.txt",'r',encoding="utf-8")
s=f.readlines()
s=''.join(s)
dictionary={}
myset=set()
sp=[]

for i in s:
    for j in i:
        myset.add(j)
myset=sorted(myset)  

i1=math.ceil(math.log2(len(myset)))

news='{one}'.format(one=s[0])  
for i in range(len(myset)):
    dictionary.update({'{name}'.format(name=myset[i]):'0'*(i1-len(bin(i)[2::]))+bin(i)[2::]})

bit1=len(s)*len(bin(len(myset)-1)[2::])

bit2=0
sd=0
k=len(myset)
for i in range(1,len(s)+1):
    if i==len(s):
        sp.append('0'*(sd-len(dictionary[news]))+dictionary[news])
    elif news in dictionary:
        news+=s[i]
        if news not in dictionary:
            dictionary.update({'{name}'.format(name=news):bin(k)[2::]})
            sd=len(bin(k-1)[2::])
            sp.append('0'*(sd-len(dictionary[news[:-1:]]))+dictionary[news[:-1:]])
            k+=1
            news='{two}'.format(two=s[i])
for i in sp:
    bit2+=len(i)
file=open("discretka print.txt",'w',encoding="utf-16 LE")
for i in sp:
    file.write(i+" ")
file.write("\nСколькими битами закодирован исходный текст: "+str(bit1))
file.write("\nСколькими битами закодирован изменённый текст: "+str(bit2))
file.write("\nКоэффициент сжатия текста: "+str(((bit1-bit2)*100)/bit1)+" %")
f.close()
file.close()



