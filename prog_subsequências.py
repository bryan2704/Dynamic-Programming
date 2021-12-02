import numpy as np
import pandas as pd
import time

def Initialization(Control):
    if Control==1:
       j=int(input("\nQual seria o tamanho da sequência? "))
       r=int(input("\nOs valores da sequência são de quais tipo? 1 para int e 2 para float: "))
       if r==1:
           t=np.array([int(item) for item in input("\nQuais seriam os valores limites da sequência? Inserir limite inferior e superior na ordem: ").split()])
           v=np.random.randint(t[0],t[1]+1,size=j)
       if r==2:
           t=np.array([float(item) for item in input("\nQuais seriam os valores limites da sequência? Inserir limite inferior e superior na ordem: ").split()])
           v=np.random.uniform(t[0],t[1]+2.3e-308,size=j)
       return Max(v)
    if Control==2:
        x=int(input("\nA sequência se encontra em um arquivo CSV? 1 para sim e 2 para não: "))
        if x==2:
            r=int(input("\nOs valores da sequência são de quais tipo? 1 para int e 2 para float: "))
            if r==1:
                v=np.array([int(item) for item in input("\nInsira a sequência : ").split()])
            if r==2:
                v=np.array([float(item) for item in input("\nInsira a sequência : ").split()])
            return Max(v)
        if x==1:
           b=input("\nInsira aqui o endereço de seu arquivo (sem o .csv): ")
           v=pd.read_csv(b+".csv", sep=';', header=None)
           v=np.array(v.values).flatten()
           return Max(v)    

def Max(v):
    start_time=time.time()
    a=0
    b=0
    att_value=0
    initial_value=0
    final_value=0
    if max(v)<=0:
        end_time=time.time()
        return max(v), np.where(v==np.amax(v))[0][0],np.where(v==np.amax(v))[0][0],v,end_time-start_time
    for i in range(0,len(v)):
        a=max(0,a+v[i])
        if a==0:
            att_value=i+1
        if max(a,b)==a:
            b=a
            initial_value=att_value
            final_value=i
    end_time=time.time()        
    return b,initial_value,final_value,v,end_time-start_time


Control=int(input("Você gostaria que uma sequência fosse gerada randomicamente ou prefere inserir uma manualmente? 1 para geração randômica e 2 para manual: "))    
Sum,initial_value,final_value,vector,total_time=Initialization(Control)
print("\nPara a sequência: ",vector)
print("\nTemos como resultado de soma máxima: ",Sum)
print("\nTal soma ocorre na subsequência que se inicia no elemento número",initial_value+1,"e termina no elemento número",final_value+1)
print("\nSubsequência que maximiza a soma: ",vector[initial_value:final_value+1])
if total_time>0:
    print("\nO processo todo levou um tempo total de:","{:.5f}".format(total_time),"segundos")
else:
    print("\nO processo todo foi tão rápido que a precisão da máquina não conseguiu registrar o tempo corretamente")
texto=int(input("Gostaria de salvar um arquivo txt com os dados obtidos? 1 para sim e 2 para não: "))
if texto==1:
    salvar=input("Endereço para salvar o arquivo (sem o nome do mesmo): ")
    salvar=r"%s\dados_subsequências.txt" %salvar
    f=open(salvar,"w+")
    f.write("Início da sequência: %d" %initial_value)
    f.write("\nFinal da sequência: %d" %final_value)
    f.write("\nSoma total: %f" %Sum)
    f.write("\n")
    f.write("\nSequência inserida:")
    f.writelines([" %f" %c for c in vector])
    f.write("\n")
    f.write("\nSubsequência ótima:")
    f.writelines([" %f" %d for d in vector[initial_value:final_value+1]])
    f.close()
    print("\nSeus dados foram salvos como dados_subsequências.txt :)")
    
    
    