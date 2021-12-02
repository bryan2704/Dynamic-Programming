import math as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy as cp
import time

def Max(X,i,j,C):
    if (i,j) in C:
        return C[(i,j)]
    a=X
    m=X.shape[0] 
    n=X.shape[1]
    if i==m-1:
      return (a[i,j],j)
    else:
      k=j-1
      l=j+1
      x=Max(a,i+1,j,C)
      if k>=0:
          y=Max(a,i+1,k,C)
      else:
          y=(-mt.inf,k)
      if l<(n):
          z=Max(a,i+1,l,C)
      else:
          z=(-mt.inf,l)
      c=a[i,j]+max(x[0], y[0], z[0])
      if max(x[0], y[0], z[0])==x[0]:
          C[(i,j)]=(c,j)
          return (c,j)
      elif max(x[0], y[0], z[0])==y[0]:
          C[(i,j)]=(c,k)
          return (c,k)
      else:
          C[(i,j)]=(c,l)
          return (c,l)

def Travel(X,j,C):
    start_time=time.time()
    m=X.shape[0]
    A=[j]
    k=0
    while k<m-1:
        A.append(Max(X,k,j,C)[1])
        j=Max(X,k,j,C)[1]
        k=k+1
    end_time=time.time()    
    return A,end_time-start_time     

def Initialize():
   h=int(input("Gostaria que a matriz com os valores fosse gerada randômicamente ou através da inserção do usuário? 1 para geração randômica e 2 para inserção manual: "))
   C={}
   if h==1:
      b=int(input("\nOs valores da matriz seriam de qual tipo? 1 para int e 2 para float: "))
      k=[int(item) for item in input("\nInsira as dimensões da matriz na ordem linha e depois coluna: ").split()] 
      w=[float(item) for item in input("\nQuais seriam os valores limites? Inserir o limite inferior e superior na ordem: ").split()]
      if b==1:
          A=np.random.randint(w[0],w[1]+1,size=(k[0],k[1]))
      else:
          A=np.random.uniform(w[0],w[1]+2.3e-308,size=(k[0],k[1]))
      B=0
      aux=0
      for j in range(0,A.shape[1]):
          D=Max(A,0,j,C)[0]
          if D>B:
              B=D
              aux=j
      Result,total_time=Travel(A,aux,C) 
      return A,Result,total_time,B
   else:
       g=int(input("Os dados se encontram em um arquivo CSV? 1 para sim e 2 para não: "))
       if g==1:
           h=input("Endereço para o arquivo (sem o .csv): ")
           h=h+".csv"
           l=pd.read_csv(h,sep=';',header=None)
           A=np.array(l.values)
           B=0
           aux=0
           for j in range(0,A.shape[1]):
               D=Max(A,0,j,C)[0]
               if D>B:
                   B=D
                   aux=j
           Result,total_time=Travel(A,aux,C) 
           return A,Result,total_time,B
       else:
           b=int(input("\nOs valores da matriz seriam de qual tipo? 1 para int e 2 para float: "))
           k=[int(item) for item in input("\nInsira as dimensões da matriz na ordem linha e depois coluna: ").split()]
           if b==1:
               v=np.array(list(map(int, input("\nInsira os valores da matriz (Ao escrever o número de termos correspondente ao de colunas, a linha já é trocada automaticamente): ").split())))
           else:
               v=np.array(list(map(float, input("\nInsira os valores da matriz (Ao escrever o número de termos correspondente ao de colunas, a linha já é trocada automaticamente): ").split())))
           A=v.reshape(k[0],k[1])
           B=0
           aux=0
           for j in range(0,A.shape[1]):
               D=Max(A,0,j,C)[0]
               if D>B:
                   B=D
                   aux=j
           Result,total_time=Travel(A,aux,C) 
           return A,Result,total_time,B        

def Show(A,Result):
    B=cp.deepcopy(A)
    k=0
    for i in range(B.shape[0]):
        a=Result[k]
        for j in range(B.shape[1]):
                if j!=a:
                    B[i,j]=0
                else:
                    B[i,j]=1000
        k=k+1
    plt.matshow(B)
    plt.show()    
    
A,Result,total_time,Sum=Initialize()
print("\nPara a seguinte matriz: ")
print("\n")
print(A)
if Sum==0:
    print("\nA soma para o melhor caminho é menor ou igual a zero, sendo assim, não existe nenhuma escolha ótima.")
else:
    print("\nTemos como caminho que maximiza a soma o seguinte: ")
    if len(Result)>10:
        for i in range(0,5):
            print((i+1,Result[i]+1),"= ",A[i,Result[i]])
        print("\n    .")
        print("    .")
        print("    .")
        print("\n")
        for k in range(len(Result)-1-5,len(Result)):
            print((k+1,Result[k]+1),"= ",A[k,Result[k]])
        
    else:
        for i in range(len(Result)):
            print((i+1,Result[i]+1),"= ",A[i,Result[i]])
    print("\nCom a seguinte soma máxima: ",Sum)    
    Show(A,Result)
    if total_time!=0:
        print("\nTempo total para a execução completa do processo: ",total_time,"segundos")
    else:
        print("\nO Processo foi tão rápido que a precisão da máquina não conseguiu registrar o tempo")
    texto=int(input("Gostaria de salvar um arquivo txt com os dados obtidos? 1 para sim e 2 para não: "))
    if texto==1:
        salvar=input("Endereço para salvar o arquivo (sem o nome do mesmo): ")
        salvar=r"%s\dados_matrizes.txt" %salvar
        f=open(salvar,"w+")
        f.write("Soma total: %d" %Sum)
        f.write("\nCaminho ótimo:")
        f.writelines(["\n(%d,%d)" %(d+1,Result[d]) for d in range(len(Result))])
        f.write("\n")
        f.write("\nMatriz Analisada:")
        f.write("\n")
        f.write(str(A))
        f.close()
        print("\nSeus dados foram salvos como dados_matrizes.txt :)")
