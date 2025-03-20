def delete(matrix,size,row,col,new_matrix):
    offsetrow=0
    offsetcol=0
    for i in range(size-1):
        if (i==row):
            offsetrow=1
        offsetcol=0
        for j in range(size-1):
            if (j==col):
                offsetcol=1
            new_matrix[i][j]=matrix[i+offsetrow][j+offsetcol]

def matrix_det(matrix, size):
    det=0
    degree=1
    if (size==1):
        return matrix[0][0]
    if (size==2):
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        new_matrix=[[0]*(size-1) for _ in range(size-1)]
        for j in range(size):
            delete(matrix,size,0,j,new_matrix)
            det=det+(degree*matrix[0][j]*matrix_det(new_matrix,size-1))
            degree=-degree
        for i in range(len(new_matrix)-1,-1,-1):
            del new_matrix[i]
    return det

def zam(matrix,col):
    cope=[]
    for i in range(size):
        cope.append(matrix[i].copy())
    for j in range(len(matrix[col])):
         cope[j][col]=b[j][0]
    return matrix_det(cope,size)

f=open('alg.txt')
size=len(f.readlines())
matrix=[]
f=open('alg.txt')
for i in range(size):
    a=str(f.readline()).split()
    matrix.append(a)

for i in range(size):
    for j in  range(len(matrix[i])-1,-1,-1):
        if (matrix[i][j]=='x' or matrix[i][j]=='=' or matrix[i][j]==' ' or matrix[i][j]=='*' or matrix[i][j]=='*x' or matrix[i][j]=='*x='):
            del matrix[i][j]
           
for i in range(size):
    for j in range(size):
        matrix[i][j]=int(matrix[i][j])
        
file=open('alg print.txt','w')
matrix_determinate=matrix_det(matrix,size)
answer=[]
zero=[]
b=[]
for i in matrix:
    b.append([int(i[-1])])
    del i[-1]

for i in range(size):
    x=zam(matrix,i)
    answer.append(x)
    if (x==0):
        zero.append(x)
if (len(zero)==size and matrix_determinate==0):
    file.write("Система имеет множество решений")
elif (len(zero)!=size and matrix_determinate==0):
    file.write('Решений нет')
elif (matrix_determinate!=0):
    for i in range(size):
        x=answer[i]/matrix_det(matrix,size)
        if (x==0):
            file.write('x'+str(i+1)+' = '+str(abs(x))+'\n')
        else:
            file.write('x'+str(i+1)+' = '+str(x)+'\n')
    file.write("\n")
f.close()
file.close()
    

