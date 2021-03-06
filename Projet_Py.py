import pandas as pd
import math
import matplotlib.pyplot as plt


df=pd.read_csv('C:\Program Files\Projet Python\EIVP_KM.csv', sep=';')
def humidex (Tair):
    T=df.sent_at
    H=df.humidity
    Trosee=[]
    A=[]
    x=0
    a=0
    for k in range (len(Tair)):
        x=(237.7*(((17.27*Tair[k])/(237.7+Tair[k]))+math.log(H[k])))/(17.27-(((17.27*Tair[k])/(237.7+Tair[k]))+math.log(H[k])))
        Trosee.append(x)
    for k in range (len(Trosee)):
        a=Tair+0.5555*(math.exp(5417.7530*((1/273.16)-(1/(273.15+Trosee[k])))-10))
        A.append(a)
    return A

def anomalie():
    A=[]
    N1=[]
    T1=[]
    H1=[]
    L1=[]
    C1=[]
    N2=[]
    T2=[]
    H2=[]
    L2=[]
    C2=[]
    N3=[]
    T3=[]
    H3=[]
    L3=[]
    C3=[]
    N4=[]
    T4=[]
    H4=[]
    L4=[]
    C4=[]
    N5=[]
    T5=[]
    H5=[]
    L5=[]
    C5=[]
    N6=[]
    T6=[]
    H6=[]
    L6=[]
    C6=[]
    I=df.id
    N=df.noise
    T=df.temp
    H=df.humidity
    L=df.lum
    C=df.co2
    Nf=[]
    Tf=[]
    Hf=[]
    Lf=[]
    Cf=[]
    k=0
    a=0
    b=0
    c=0
    while (I[k]==1):
        N1.append(N[k])
        T1.append(T[k])
        H1.append(H[k])
        L1.append(L[k])
        C1.append(C[k])
        k+=1
    while (I[k]==2):
        N2.append(N[k])
        T2.append(T[k])
        H2.append(H[k])
        L2.append(L[k])
        C2.append(C[k])
        k+=1
    while (I[k]==3):
        N3.append(N[k])
        T3.append(T[k])
        H3.append(H[k])
        L3.append(L[k])
        C3.append(C[k])
        k+=1
    while (I[k]==4):
        N4.append(N[k])
        T4.append(T[k])
        H4.append(H[k])
        L4.append(L[k])
        C4.append(C[k])
        k+=1
    while (I[k]==5):
        N5.append(N[k])
        T5.append(T[k])
        H5.append(H[k])
        L5.append(L[k])
        C5.append(C[k])
        k+=1
    while (k!=len(I)):
        N6.append(N[k])
        T6.append(T[k])
        H6.append(H[k])
        L6.append(L[k])
        C6.append(C[k])
        k+=1
    a=25
    for i in range(a):
        Nf.append(N5[i])
        Tf.append(T5[i])
        Hf.append(H5[i])
        Lf.append(L5[i])
        Cf.append(C5[i])
        Nf.append(N6[i])
        Tf.append(T6[i])
        Hf.append(H6[i])
        Lf.append(L6[i])
        Cf.append(C6[i])
        Nf.append(N2[i])
        Tf.append(T2[i])
        Hf.append(H2[i])
        Lf.append(L2[i])
        Cf.append(C2[i])
        Nf.append(N3[i])
        Tf.append(T3[i])
        Hf.append(H3[i])
        Lf.append(L3[i])
        Cf.append(C3[i])
        Nf.append(N4[i])
        Tf.append(T4[i])
        Hf.append(H4[i])
        Lf.append(L4[i])
        Cf.append(C4[i])
    b=1165
    for i in range (a,b):
        Nf.append(N5[i])
        Tf.append(T5[i])
        Hf.append(H5[i])
        Lf.append(L5[i])
        Cf.append(C5[i])
        Nf.append(N6[i])
        Tf.append(T6[i])
        Hf.append(H6[i])
        Lf.append(L6[i])
        Cf.append(C6[i])
        Nf.append(N1[i-a])
        Tf.append(T1[i-a])
        Hf.append(H1[i-a])
        Lf.append(L1[i-a])
        Cf.append(C1[i-a])
        Nf.append(N2[i])
        Tf.append(T2[i])
        Hf.append(H2[i])
        Lf.append(L2[i])
        Cf.append(C2[i])
        Nf.append(N3[i])
        Tf.append(T3[i])
        Hf.append(H3[i])
        Lf.append(L3[i])
        Cf.append(C3[i])
        Nf.append(N4[i])
        Tf.append(T4[i])
        Hf.append(H4[i])
        Lf.append(L4[i])
        Cf.append(C4[i])
    c=1344
    for i in range(b,c):
        Nf.append(N6[i])
        Tf.append(T6[i])
        Hf.append(H6[i])
        Lf.append(L6[i])
        Cf.append(C6[i])
        Nf.append(N1[i-a])
        Tf.append(T1[i-a])
        Hf.append(H1[i-a])
        Lf.append(L1[i-a])
        Cf.append(C1[i-a])
        Nf.append(N2[i])
        Tf.append(T2[i])
        Hf.append(H2[i])
        Lf.append(L2[i])
        Cf.append(C2[i])
        Nf.append(N3[i])
        Tf.append(T3[i])
        Hf.append(H3[i])
        Lf.append(L3[i])
        Cf.append(C3[i])
        Nf.append(N4[i])
        Tf.append(T4[i])
        Hf.append(H4[i])
        Lf.append(L4[i])
        Cf.append(C4[i])
    Nf.append(N6[c])
    Tf.append(T6[c])
    Hf.append(H6[c])
    Lf.append(L6[c])
    Cf.append(C6[c])
    Nf.append(N1[c-a])
    Tf.append(T1[c-a])
    Hf.append(H1[c-a])
    Lf.append(L1[c-a])
    Cf.append(C1[c-a])
    Nf.append(N2[c])
    Tf.append(T2[c])
    Hf.append(H2[c])
    Lf.append(L2[c])
    Cf.append(C2[c])
    Nf.append(N3[c])
    Tf.append(T3[c])
    Hf.append(H3[c])
    Lf.append(L3[c])
    Cf.append(C3[c])
    for i in range (a):
        Nf.append(N1[-i])
        Tf.append(T1[-i])
        Hf.append(H1[-i])
        Lf.append(L1[-i])
        Cf.append(C1[-i])
    A=A+[Nf]
    A=A+[Tf]
    A=A+[Hf]
    A=A+[Lf]
    A=A+[Cf]
    return A

T=df.sent_at
def courbe_noise():
    plt.rcParams.update({'font.size':15})
    df.plot(x="sent_at",y=anomalie()[0],color='r',linestyle='dotted',label='Bruit en dBA',rot=45)
    plt.title('Bruit en fonction du temps',**csfont)
    ax=plt.axes()
    ax.set(xlabel='Temps',ylabel='Bruit')
    plt.show()

def courbe_temperature():
    plt.rcParams.update({'font.size':15})
    df.plot(x="sent_at",y=anomalie()[1],color='b',linestyle='dotted',label='Température en °C',rot=45)
    plt.title('Température en fonction du temps',**csfont)
    ax=plt.axes()
    ax.set(xlabel='Temps',ylabel='Température')
    plt.show()

def courbe_humidity():
    plt.rcParams.update({'font.size':15})
    df.plot(x="sent_at",y=anomalie()[2],color='y',linestyle='dotted',label='Humidité en %',rot=45)
    plt.title('Humidité en fonction du temps',**csfont)
    ax=plt.axes()
    ax.set(xlabel='Temps',ylabel='Humidité')
    plt.show()

def courbe_lum():
    plt.rcParams.update({'font.size':15})
    df.plot(x="sent_at",y=anomalie()[3],color='g',linestyle='dotted',label='Luminosité en lux',rot=45)
    plt.title('Luminosité en fonction du temps',**csfont)
    ax=plt.axes()
    ax.set(xlabel='Temps',ylabel='Luminosité')
    plt.show()

def courbe_co2():
    plt.rcParams.update({'font.size':15})
    df.plot(x="sent_at",y=anomalie()[4],color='k',linestyle='dotted',label='CO2 en ppm',rot=45)
    plt.title('Quantité de CO2 en fonction du temps',**csfont)
    ax=plt.axes()
    ax.set(xlabel='Temps',ylabel='CO2')
    plt.show()

