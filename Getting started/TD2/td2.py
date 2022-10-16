#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:36:20 2022

@author: steven
"""

# %% zone de l'exo1
def Exo1():
    """
    Il s'agit de la méthode 1
    Elle ecrit un script qui recopie ces valeurs dans un autre fichier en les arrondissant en nombres entiers.
    """
    #with open...
    
    f=open(r'/Users/steven/Documents/ESILV/Python/TD2/fichier.txt', 'r')
    fmodif=open(r'/Users/steven/Documents/ESILV/Python/TD2/result.txt', 'w')
    
    for line in f:
        fmodif.write(line.replace('\n','').split('.')[0] + "\n")
        #str(round(float.....rstrip('\n')
                
    f.close()
    fmodif.close()
 
# %% zone de l'exo2
def Exo2():
    """
    Il s'agit de la méthode 2
    Elle présente différentes manipulations sur des dictionnaires
    """
    
    semestre2 = {'Janvier':31,'Février':28,'Mars':31,'Avril':30,'Mai':31,'Juin':30}
    print(*semestre2.keys())
    print(*semestre2.values())
    
    semestre1 = {'Septembre':26,'Octobre':31,'Novembre':30,'Decembre':31,'Janvier':31,'Février':28}
    
    annee = int(input("Veuillez saisir une année pour voir si elle est bissextile : "))
    
    if(Bissextile(annee)):
        print("C'est une année bissextile")
    else:
        print("C'est pas une année bissextile")
        
    anneeScolaire = semestre2 | semestre1
    #anneeScolaire.update(...)
    #anneeScolaire = {**semestre2, **semestre1}
    print(*anneeScolaire)
    print(*anneeScolaire.values())
    
    vacanceScolaire = {'Janvier':0,'Février':7,'Mars':0,'Avril':7,'Mai':0,'Juin':0,'Juillet':31,'Aout':31,'Septembre':0,'Octobre':7,'Novembre':0,'Decembre':12}
    weekend = {'Janvier':10,'Février':10,'Mars':10,'Avril':10,'Mai':10,'Juin':10,'Juillet':10,'Aout':10,'Septembre':10,'Octobre':10,'Novembre':10,'Decembre':10}
    
    #Trop simple
    joursTravail = {}
    
    #joursTravail = []
    for ele in weekend:
            joursTravail[ele] = (0 if(ele not in anneeScolaire) else anneeScolaire[ele] - weekend[ele] - vacanceScolaire[ele])
    
    print(*joursTravail)
    print(*joursTravail.values())
    
    
def Bissextile(a):
    if a%100 == a%400:
        return True
    
    return False

# %% zone de l'exo3
class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def Affichage(self):
        print("Coordonnées : x =",self.x,"; y =",self.y,"; z =",self.z)
    def Module(self):
        return ((self.x**2)+(self.y**2)+(self.z**2))**(1/2)
    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y and self.z == autre.z
    def __sub__(self,autre):
        return Point3D(self.x - autre.x,self.y - autre.y,self.z - autre.z)
    def __add__(self,autre):
        return Point3D(self.x + autre.x,self.y + autre.y,self.z + autre.z)
    def __mul__(self,scalaire):
        return Point3D(self.x*scalaire,self.y*scalaire,self.z*scalaire)
    def ProduitVec(self,autre):
        x_new = self.y*autre.z - self.z*autre.y
        y_new = self.z*autre.x - self.x*autre.z
        z_new = self.x*autre.y - self.y*autre.x
        return Point3D(x_new,y_new,z_new)
    def __setitem__(self,index,value):
        self.__dict__[list(self.__dict__.keys())[index]] = value
    def __getitem__(self,index):
        return self.__dict__[list(self.__dict__.keys())[index]]
    def __str__(self):
        return f"Coordonnées : x = {self.x} ; y = {self.y} ; z = {self.z}"

class Mass3D(Point3D):
    def __init__(self,point,m):
        #Point3D.__init__(self,x,y,z)
        self.point = point
        self.valeur = m
    def Affichage(self):
        print(self.point.Affichage(),"\nMasse =", self.valeur)
    def __eq__(self,autre):
        return self.point.__eq__(autre.point) and self.valeur == autre.valeur
    def __str__(self):
        return self.point.__str__() + f"\n Masse : {self.valeur}"

def Exo3():
    """
    Il s'agit de la méthode 3
    Elle rend compte de l'utilisation de classe (ici : Point3d et Masse3D....et 
    l'explication plus de la classe CompteBancaire')'
    """
    
    x = Point3D(1,2,3)
    #print(x.__getitem__(2))
    y = Point3D(1,2,3)
    
    a = Mass3D(x,3)
    b = Mass3D(y,3)
    if a == b:
        print(a)



class CompteBancaire:
    """" une classe pour gérer des comptes bancaires"""
    cb_count=2
    #constructeur
    def _init_(self, nomClient, iban, solde =2):
        #variables d'instances
        self.nomClient=nomClient
        self.solde=solde
        self.iban=iban
        #variables de classe
        CompteBancaire.cb_count+=1
    
    def Affichage(self):
        print("Compte appartenant à", self.nomClient,"IBAN : ", self.iban, "solde :", self. solde)
    
    #permet l'utilisation du test ==
    def __eq_(self, autrecompte):
        return self.iban == autrecompte.iban
    
    #permet l'utilisation de print(c2)
    def _str_(self):
        return f"Compte appartenant à {self.nomClient} IBAN : {self.iban} solde : {self.solde}"
   

# %% zone du main
if __name__ == '__main__' :
    #Exo1()
    #Exo2()
    Exo3()