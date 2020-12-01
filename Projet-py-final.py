+                       ## Rapport de projet | codes python                                     

# Durant notre devoir, nous utiliserons les librairies : pandas,matplotlib et numpy
# Nous allons donc à cet effet commencer par les importer

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Lecture du fichier csv

#méthode 1 : avec fonction 'open'

import csv

fn=r'C:\Users\hicha\OneDrive\Documents\Bureau\EIVP\Projet_Informatique\post-32566-EIVP_KM.csv'# "r" en préfixe pour fixer les slash (\)
 
def affichage_fichier_csv():
    with open(fn) as csvfile:                         #ouverture   du fichier
        readcsv=csv.reader(csvfile,delimiter=';')     #lecture du fichier
        print(readcsv)
       
        for row in readcsv:                           #extraction des lignes 
            print(row)

#affichage_fichier_csv()
#affiche  7881 listes de chaines de caractères

#méthode 2 avec la librairie pandas

#f="C:\Users\hicha\OneDrive\Documents\Bureau\EIVP_KM1.csv"                                      #ancien fichier
f1=r'C:\Users\hicha\OneDrive\Documents\Bureau\EIVP\Projet_Informatique\post-32566-EIVP_KM.csv' # "r" en préfixe pour fixer les slash (\)
df = pd.read_csv(f1,sep=";")                                                                   # lecture
print(df)                                                                                      # affichage des données au sein du fichier

>>> (executing lines 12 to 14 of "Projet_data.py")
      Unnamed: 0  id  noise  ...  lum  co2                    sent_at
0              0   1   35.5  ...  282  448  2019-08-11 17:48:06+02:00
1              1   1   44.5  ...  288  429  2019-08-11 18:03:03+02:00
2              2   1   34.5  ...  286  417  2019-08-11 18:18:03+02:00
3              3   1   37.5  ...  282  433  2019-08-11 18:33:03+02:00
4              4   1   36.0  ...  274  403  2019-08-11 18:48:03+02:00
...          ...  ..    ...  ...  ...  ...                        ...
7875        7875   6   41.0  ...  728  479  2019-08-25 10:45:51+02:00
7876        7876   6   41.0  ...  270  482  2019-08-25 11:00:52+02:00
7877        7877   6   42.0  ...  302  475  2019-08-25 11:15:52+02:00
7878        7878   6   39.5  ...  336  478  2019-08-25 11:30:54+02:00
7879        7879   6   38.5  ...  366  459  2019-08-25 11:45:54+02:00

[7880 rows x 8 columns]


#Problème rencontré : nécessité d'utiliser "r" en préfixe pour garder les slash tels quels

##1 Affichage de la température en fonction du temps

#Essai 1 :avec la fonction scatter de matplotlib, puis avec la fonction plot dans pandas
    
def temperature1():
    df=pd.read_csv(r"C: \Users\hicha\OneDrive\Documents\Bureau\EIVP_KM1.csv",sep=';',nrows=7880,skiprows=[1])
    y=df["lum"];
    x=df["sent_at"]
    plt.xlabel("sent_at(date)")plt.ylabel("lum(lux)")
    plt.scatter(x,y)
    plt.show()
    
def temperature2():
    df.plot(x="sent_at",y="temp",color='b')
    plt.title("Température en fontion du temps ")
    plt.xlabel('sent_at(date)')
    plt.ylabel('temp(°C)')
    plt.grid()
    plt.show()
#la fonction temperature1 affiche la courbe beaucoup plus rapidement grâce à la librairie pandas
#affichage cf.rapport figure 2.a.1

#Essai 2 : apport du paramétre 'rot' pour améliorer l'affichage de l'axe des temps

#Pour mettre le titre en gras nécessité d'implémenter ce code
'''
del matplotlib.font_manager.weight_dict['roman']   # source : https://stackoverrun.com/fr/q/5172841
matplotlib.font_manager._rebuild()
'''
Afont = {'fontname':'Arial'}

def temperature3():
    import matplotlib.pyplot as plt
    df.plot(x="sent_at",y="temp",label='Température(°C)',color='b',rot=45)           # facultatif : 'linestyle='dotted'
    plt.legend(loc='best')
    plt.title('Température en fonction du temps',**Afont,fontweight="bold")
    plt.xlabel('sent_at(date)')
    plt.ylabel('temp(°C)')
    plt.grid()
    plt.tight_layout()
    plt.show()
    
#affichage cf.rapport figure 2.a.1
    
##2 Affichage de courbe représentant l'évolution d'une variable au cours de temps avec intervalle prédéfinie

# Essai 1; parvient seulement à intégrer manuellement les valeurs de start_at et end_at

df3=pd.DataFrame({'Joined_date':pd.to_datetime(df['sent_at']),"temp":df['temp'],"humidity":df['humidity']})

#'2019-08-11 11:30:50+02:00' à '2019-08-11 17:46:40+02:00'
#'2019-08-11 18:05:11+02:00' à '2019-08-11 18:18:03+02:00'
#'2019-08-11 18:03:03+02:00'  à  '2019-08-11 19:50:11+02:00'

#df4=df3.query("Joined_date >= '2019-08-11 11:30:50+02:00' and Joined_date <= '2019-08-11 17:46:40+02:00'")
#df4=df3.query("Joined_date >= '2019-08-11 18:05:11+02:00' and Joined_date <= '2019-08-11 18:18:03+02:00'")
#df4=df3.query("Joined_date >= '2019-08-11 18:03:03+02:00' and Joined_date <='2019-08-11 19:50:11+02:00'")

def courbe_temperature_avec_intervalle1():           #entrer des valeurs manuellelement
    df3=pd.DataFrame({'Joined_date':pd.to_datetime(df['sent_at']),"temp":df['temp'],"humidity":df['humidity']})
    df4=df3.query("Joined_date >= '2019-08-11 18:00:44+02:00' and Joined_date <='2019-08-11 18:48:03+02:00'")
    ax=df4.plot(kind='line', x='Joined_date', y='temp', color='DarkBlue',rot=45)
    ax.set_ylabel('temp (°C)')
    ax.set_xlabel('sent_at (date)')
    plt.grid()                                      #plt.title('T=f(t)',**Afont,fontweight="bold")
    plt.tight_layout()
    plt.show()
    

#affichage cf.rapport : figur 2.a.3


def courbe_lumiere():
    ax=df.plot(x='sent_at', y='lum', color='DarkBlue',rot=45)
    ax.set_ylabel('lum (lux)')
    ax.set_xlabel('sent_at (date)')
    plt.grid()               #plt.title('T=f(t)',**Afont,fontweight="bold")                   
    plt.tight_layout()
    plt.show()

#affichage cf.rapport figure 2.a.4

def courbe_lumiere_avec_intervalle():
    df5=pd.DataFrame({'Joined_date':pd.to_datetime(df['sent_at']),"lum":df['lum'],"humidity":df['humidity']})
   # df6=df5.query("Joined_date >= '2019-08-11 18:00:44+02:00' and Joined_date <= '2019-08-11 18:48:03+02:00'")
    df6=df5.query("Joined_date >= '2019-08-11 18:00:44+02:00' and Joined_date <= '2019-08-11 18:48:03+02:00'")
    ax=df6.plot(kind='line', x='Joined_date', y='lum', color='DarkBlue',rot=45)
    ax.set_ylabel('lum (lux)')
    ax.set_xlabel('sent_at (date)')
    plt.grid()                        #plt.title('T=f(t)',**Afont,fontweight="bold")
    plt.tight_layout()
    plt.show()
    
# affichage cf.rapport : figure 2.a.5

def courbe_temperature_avec_intervalle():
    df1=pd.DataFrame({'Joined_date':pd.to_datetime(df["sent_at"]),"temp":df['temp'],"humidity":df['humidity']}) #création d'une nouvelle dataframe
    df2=df1.query("Joined_date >= '2019-08-11 18:03:03+02:00' and Joined_date <= '2019-08-11 19:50:11+02:00' ") #filtre
    df2.plot(x="Joined_date",y="temp",color='r',linestyle='dotted',label='Température')
    plt.title('Température en fonction du temps')
    plt.legend(loc='lower left')
    ax=plt.axes()
    ax.set(xlabel='temps',ylabel='température')
    plt.show()

#affichage meme que figure 2.a.3

#Essai 2 : l'intégration d'un intervalle a été réalisé

#Méthode 1
#En utilisant la fonction 'datetime'

from datetime import tzinfo, timedelta, datetime 


class TZ(tzinfo):                           # nécessité d'implémenter ce code pour enlever le sépérateur T ( < type 'str' >) entre la date et l'heure
    def utcoffset(self,dt):
        return timedelta(hours=2,minutes=0)
    


start_date=datetime(2019,8,11,18,3,3,tzinfo=TZ()).isoformat(' ')
end_date=datetime(2019,8,11,19,50,11,tzinfo=TZ()).isoformat(' ')

def courbe_humidity_avec_intervalle1(a1,m1,j1,h1,s1,ms1,a2,m2,j2,h2,s2,ms2):                    #code 
    start_date=datetime(a1,m1,j1,h1,s1,ms1,tzinfo=TZ()).isoformat(' ')
    end_date=datetime(a2,m2,j2,h2,s2,ms2,tzinfo=TZ()).isoformat(' ')
    df1=pd.DataFrame({'Joined_date':pd.to_datetime(df['sent_at']),"temp":df['temp'],"humidity":df['humidity']})
    mask = (df1['Joined_date'] > start_date) & (df1['Joined_date'] <= end_date)
    df2=df1.loc[mask]
    ax=df2.plot(kind='line', x='Joined_date', y='humidity', color='DarkBlue',rot=45)
    ax.set_ylabel('humidity (%)')
    ax.set_xlabel('sent_at (date)')
    plt.grid()                                                                                  #facultatif : #plt.title('T=f(t)',**Afont,fontweight="bold")
    plt.tight_layout()
    plt.show()

# affichage de la courbe avec start_date='2019-08-11 18:03:03+02:00' et end_date='2019-08-11 19:50:11+02:00'
# cf. rapport : figure 2.a.6

#Méthode 2    
#L'utilisateur entre les données qu'ils souhaitent sans faire au module "datetime"

start_date =input("Date de debut ? \n"))
end_date=input("Date de fin ? \n")

def courbe_humidity_avec_intervalle2(start_date,end_date):
    df1=pd.DataFrame({'Joined_date':pd.to_datetime(df['sent_at']),"temp":df['temp'],"humidity":df['humidity']})
    mask = (df1['Joined_date'] > start_date) & (df1['Joined_date'] <= end_date)
    df2=df1.loc[mask]
    ax=df2.plot(kind='line', x='Joined_date', y='humidity', color='DarkBlue',rot=45)
    ax.set_ylabel('humidity (%)')
    ax.set_xlabel('sent_at (date)')
    plt.grid()                                # on peut ajouter un titre avec : plt.title('T=f(t)',**Afont,fontweight="bold")
    plt.tight_layout()
    plt.show()
    
# puis courbe_humidity(start_date,end_date)
# même affichage


##3 Affichage de valeurs statistiques


import seaborn as sns

def diagramme_boite_temperature():
    sns.set(style="whitegrid")
    plt.figure(figsize=(10,8))
    ax = sns.boxplot(x='temp',data=df)
    ax.set_xlabel("temp(°C)")
    plt.title('Boîte à moustache de la température du bâtiment',**Afont,fontweight="bold")
    plt.show()

#affichage cf.rapport figure 2.b.1

def diagramme_boite_lumiere():
    sns.set(style="whitegrid")
    plt.figure(figsize=(10,8))
    ax = sns.boxplot(x='lum',data=df)
    ax.set_xlabel("lum(lux)")
    plt.title('Boîte à moustache relative à la lumière du bâtiment',**Afont,fontweight="bold")
    plt.show()

#affichage cf.rapport figure 2.b.2

##4 Calcul du coefficient de correlation

#Moyenne d'une liste

def moyenne(L):
    return (sum(L[i] for i in range(len(L)))/len(L))

# sans la fonction 'sum'

def moyenne1(L):
    s=0
    for i in range(len(L)):
        s+=L[i]
    return s/len(L)

def covariance(L1,L2):
    if len(L1)==len(L2):
        x=moyenne(L1)
        y=moyenne(L2)
        S=0
        for i in range(len(L1)):
            S+=(L1[i]-x)*(L2[i]-y)
            S=S/len(L1)
        return S
    else:
        print("il faut des listes de même taille")

covariance(df["temp"],df["humidity"])

>>> covariance(df["temp"],df["humidity"])
0.004888479171290153

##5 Calcul de l'indice humidex

def humidex(temp,humidity):
    a=5/9
    b=6.112
    c=7.5
    d=237.7
    return (temp + a*((b*10**(c*temp/(temp+d))*humidity/100)-10))

>>> humidex(df['temp'],df['humidity'])
0       30.374665
1       29.896373
2       29.896373
3       29.805901
4       29.579038
          ...    
7875    21.997125
7876    21.926870
7877    21.926870
7878    21.856615
7879    21.856615
Length: 7880, dtype: float64

ax=df.plot(kind='line', x='Joined_date', y='lum', color='DarkBlue',rot=45)
ax.set_ylabel('lum (lux)')
ax.set_xlabel('sent_at (date)')
plt.grid()
plt.tight_layout()
plt.show()


##6 Affichage de deux courbes dans un même graphique
def courbe_temperature_et_humidite():
    ax=df.plot(kind='line', x='sent_at', y='temp', color='DarkBlue',rot=45)
    ax2=df.plot(kind='line', x='sent_at', y='humidity', secondary_y=True,color='Red', ax=ax,rot=45)
    ax.set_ylabel('temp(°C)')
    ax2.set_ylabel('relative humidity(%)')
    ax.set_xlabel('sent_at (date)')
    plt.text(2019,72,'indice de corrélation : 0.0048',**Afont,fontweight="bold")                              # facultatif : plt.title('T=f(t) | H=g(t)',**Afont,fontweight="bold")   
    plt.tight_layout()
    plt.show()

#affichage cf. rapport figure 2.c.1

>>> (executing lines 35 to 40 of "Projet_data.py")                              # cf.rapport Figure 3



##7 Anomalies

def anomalie():
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
    print(Nf)
    print(Tf)
    print(Hf)
    print(Lf)
    print(Cf)



