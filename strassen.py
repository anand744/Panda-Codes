def add(X,Y):
        n = len(X)
        C1 = []
        for i in range(0,n):
                C1.append([])
        for i in range(0,n):
                for j in range(0,n):
                        C1[i].append(j)
                        C1[i][j] = 0
        for i in range(0, n):
                for j in range(0,n):
                                C1[i][j] = X[i][j] + Y[i][j]
        return C1
def sub(X,Y):
        n = len(X)
        C1 = []
        for i in range(0,n):
                C1.append([])
        for i in range(0,n):
                for j in range(0,n):
                        C1[i].append(j)
                        C1[i][j] = 0
        for i in range(0, n):
                for j in range(0,n):
                        C1[i][j] = X[i][j] - Y[i][j]
        return C1
def multiply(X,Y):
        n = len(X)
        C1 = []
        for i in range(0,n):
                C1.append([])
        for i in range(0,n):
                for j in range(0,n):
                        C1[i].append(j)
                        C1[i][j] = 0
        for i in range(n):
                for k in range(n):
                        for j in range(n):
                                C1[i][j] += X[i][k] * Y[k][j]
        return C1
def strassen(X,Y):
        n = len(X)
        if (n == 2):
                return multiply(X,Y)
        else:
                newsize = n//2
                m=n//2
                a11 = []
                for i in range (0,newsize):
                        a11.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                a11[i].append(0)
                                #a11[i][j]=0
                a12 = []
                for i in range (0,newsize):
                        a12.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                a12[i].append(0)
                                #a12[i][j]=0
                a21 = []
                for i in range (0,newsize):
                        a21.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                a21[i].append(0)
                                #a21[i][j]=0
                a22 = []
                for i in range (0,newsize):
                        a22.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                a22[i].append(0)
                                #a22[i][j]=0
                b11 = []
                for i in range (0,newsize):
                        b11.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                b11[i].append(0)
                                #b11[i][j]=0
                b12 = []
                for i in range (0,newsize):
                        b12.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                b12[i].append(0)
                                #b12[i][j]=0
                b21 = []
                for i in range (0,newsize):
                        b21.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                b21[i].append(0)
                                #a21[i][j]=0
                b22 = []
                for i in range (0,newsize):
                        b22.append([])
                for i in range (0,m):
                        for j in range(0,newsize):
                                b22[i].append(0)
                                #b22[i][j]=0
                for i in range(0,newsize):
                        for j in range(0,newsize):
                                a11[i][j] = X[i][j]
                                a12[i][j] = X[i][j + newsize]
                                a21[i][j] = X[i+newsize][j]
                                a22[i][j] = X[i+newsize][j+newsize]
                                b11[i][j] = Y[i][j]
                                b12[i][j] = Y[i][j+newsize]
                                b21[i][j] = Y[i+newsize][j]
                                b22[i][j] = Y[i+newsize][j+newsize]
                aresult = add(a11, a22)
                bresult = add(b11, b22)
                p1 = strassen(aresult, bresult)

                aresult = add(a21, a22)     
                p2 = strassen(aresult, b11)  

                bresult = sub(b12, b22) 
                p3 = strassen(a11, bresult) 

                bresult = sub(b21, b11) 
                p4 =strassen(a22, bresult)   

                aresult = add(a11, a12)     
                p5 = strassen(aresult, b22) 

                aresult = sub(a21, a11) 
                bresult = add(b11, b12)      
                p6 = strassen(aresult, bresult) 

                aresult = sub(a12, a22) 
                bresult = add(b21, b22)      
                p7 = strassen(aresult, bresult) 

                
                c12 = add(p3, p5)
                c21 = add(p2, p4)  

                aresult = add(p1, p4) 
                bresult = add(aresult, p7) 
                c11 = sub(bresult, p5) 

                aresult = add(p1, p3) 
                bresult = add(aresult, p6) 
                c22 = sub(bresult, p2)
                C1=[]
                for i in range(0,n):
                        C1.append([])
                for i in range(0,n):
                        for j in range(0,n):
                                C1[i].append(0)
                                #C1[i][j] = 0
                for i in range(0,newsize):
                        for j in range(0,newsize):
                                C1[i][j]=c11[i][j]
                                C1[i][j+newsize]=c12[i][j]
                                C1[i+newsize][j]=c21[i][j]
                                C1[i+newsize][j+newsize]=c22[i][j]
                return C1
a = int(input("Enter the rows and coloumns: "))
f = 0
for i in range(a,100):
        for j in range(1,100):
                if(2**j == i):
                        m = i
                        f = 1
        if(f == 1):
                break
mat = []
for i in range (0,m):
        mat.append([])
for i in range (0,m):
        for j in range(0,m):
                mat[i].append(0)
                #mat[i][j]=0
for i in range(0,a):
        for j in range(0,a):
                mat[i][j] = int(input())
                
b = int(input("Enter the rows and coloumns: "))
f1 = 0
for i in range(b,100):
        for j in range(1,100):
                if(2**j == i):
                        m1 = i
                        f1 = 1
        if(f1 == 1):
                break
mat1 = []
for i in range (0,m1):
        mat1.append([])
for i in range (0,m1):
        for j in range(0,m):
                mat1[i].append(0)
                #mat1[i][j]=0
for i in range(0,b):
        for j in range(0,b):
                mat1[i][j] = int(input())
ans = strassen(mat,mat1)
print(ans)
