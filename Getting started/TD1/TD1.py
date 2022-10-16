# -*- coding: utf-8 -*-
import math
import numpy
#import re
# %% zone de l'exo zéro elle doit contenir l'Exo 0 et les méthodes afférentes
def Exo0():
    """
    Il s'agit d'une méthode à titre d'exemple
    l'instruction help(Exo0) vous retourne cette documentation
    grâce à l'utilisation des triples guillemets
    ou bien dans la console de spyder saisissez Exo0?
    """
    print("voila mon Exo de bienvenue")
# %% zone de l'exo1
def Exo1():
    temps = 6.892
    distance = 19.7
    vitesse = distance / temps
    print("Exo1 - a")
    print("Pour une distance de", distance, "et de temps ", temps,"la vitesse est de : ", vitesse)
    print("Exo1 - b")
    """"on pourrait utiliser print("{.2f}".format(str)) ou print(f"vitesse {vitesse}")"""
    print("Pour une distance de", round(distance,2), "et de temps ", round(temps,2),"la vitesse est de : ", round(vitesse,2))
# %% zone de l'exo2
def Exo2():
    """
    Il s'agit de la méthode 2
    Elle affche le min et le max entre 2 chiffres
    3 test conditionnel sont possibles : alternatif, simple, ternaire
    """
    a = input("chiffre 1 :")
    b = input("chiffre 2 :")
    
    print(f"max : {Test_Alternatif(a,b)[1]} et min : {Test_Alternatif(a,b)[0]}")
    print(f"max : {TTest_Simple(a,b)[1]} et min : {Test_Simple(a,b)[0]}")
    print(f"max : {Test_Ternaire(a,b)[1]} et min : {Test_Ternaire(a,b)[0]}")
    
  
def Test_Alternatif(a,b):
    if(a < b):
        minValue, maxValue = a, b
    else:
        minValue, maxValue = b, a
        
    return minValue, maxValue
    

def Test_Simple(a,b):
    if(a <= b):
        minValue,maxValue = a, b
    return minValue, maxValue

    
def Test_Ternaire(a,b):
    egale = a if a == b else 0
    minValue = a if a < b else b
    maxValue = a if a >= b else b
    #print(......)
    return minValue, maxValue
# %% zone de l'exo3
def Exo3():
    """
    Il s'agit de la méthode 3
    Elle affche le volume d'un cube, d'un parallépipède ou d'un prisme selon le nombre de paramètres'
    """
    print("La valeur  1: {}".format(volBoite())) # donne -1 ou None (-> erreur).
    print("La valeur  2: {}".format(round(volBoite(5.2),2))) # donne 140.608
    print("La valeur  3: {}".format(round(volBoite(5.2, 3),2))) # donne 81.12
    print("La valeur  4: {}".format(round(volBoite(5.2, 3, 7.4),2))) # donne 115.44
    
def volBoite(*args):
    if not (args):
        return -1
    elif(len(args) == 1): 
        return args[0]**3 
    elif(len(args) == 2):  
        return (args[0]**2)*args[1] 
    elif(len(args) == 3):  
        return args[0]*args[1]*args[2] 
# %% zone de l'exo4
def Exo4():
    """
    Il s'agit de la méthode 4
    Elle affche une liste selon le nombre de paramètres qui vont faire varier sa taille'
    """
    serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
    print(eleMax(serie))
    print(eleMax(serie, 2, 5))
    print(eleMax(serie, 2))
    print(eleMax(serie, fin = 3, debut = 1))
    
def eleMax(liste, debut = - 1, fin = - 1):
    if not (liste):
        return -1
    elif (debut == -1):
        return max(liste)
    elif (fin == -1):
        return max(liste[debut:])
    else:
        return max(liste[debut:fin])
# %% zone de l'exo5
def Exo5():
    """
    Il s'agit de la méthode 5
    Elle affiche une liste qui est la combinaison alternatif de 2 listes
    """
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre','Novembre', 'Décembre']
    t3 = CombineListe(t1,t2)
    print(t3)

def CombineListe(t1,t2):
    if t1 and t2 :
        t3 = [None]*(len(t1) + len(t2))
        t3[::2] = t1
        t3[1::2] = t2
        return t3
# %% zone de l'exo6
def Exo6():
    """
    Il s'agit de la méthode 6
    Elle affiche un texte inversé
    """
    texte1 = input("Veuillez insérer un texte : ")
    texte_reverse = Reverse(texte1)
    print(texte_reverse)
    
def Reverse(txt):
    if txt:
        return txt[::-1]
# %% zone de l'exo7
def Exo7():
    """
    Il s'agit de la méthode 7
    Elle affiche la sortie de la méthode mafonction
    """
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mafonction(t1)
    print(t1)
    """La fonction range la liste dans l'ordre croissant"""
    
def mafonction(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
                if arr[j] > arr[j+1] :
                        arr[j], arr[j+1] = arr[j+1], arr[j]   
# %% zone de l'exo8
def Exo8():
    """
    Il s'agit de la méthode 8
    Elle affche une liste trié avec un algorithme de TriFusion
    """
    tab = []
    with open(r'/Users/steven/Documents/ESILV/Python/TD1/tableau.dat', 'r') as f:
        for line in f:
            x = line.replace('\n','').split(";")
            for ele in x:
                tab.append(ele)    
    
    mat = [int(i) for i in tab]
    print(mat)
    tab2 = TriFusion(mat)
    print(tab2)

    
def TriFusion (myList):
    if (len(myList)<=1):
        return myList
    else:
        mid = len(myList) // 2
        t1 = myList[:mid]
        t2 = myList[mid:]
        return Fusion(TriFusion(t1),TriFusion(t2))
        #return Fusion2(TriFusion(t1),TriFusion(t2))
    
def Fusion(t1,t2):
    tab = []
    x,y = 0,0
    while(x < len(t1) and y < len(t2)):
            if(t1[x] <= t2[y]):
                tab.append(t1[x])
                x+=1
            else:
                tab.append(t2[y])
                y+=1

    if t1:
        tab.extend(t1[x:])
    if t2:
        tab.extend(t2[y:])
        
    return list(tab)

def Fusion2(t1, t2):
    if not t1:
        return t2
    elif not t2:
        return t1
    elif t1[0] < t2[0]:
        return [t1[0]]+Fusion2(t1[1:],t2)
    else:
        return [t2[0]]+Fusion2(t1,t2[1:])
# %% zone du main
if __name__ == '__main__' :
    #Exo0()
    #Exo1()
    #Exo2()
    #Exo3()
    #Exo4()
    #Exo5()
    #Exo6()
    #Exo7()
    Exo8()

