#Exo1 - a
import json
import requests
#Exo1 - j
from datetime import datetime
#Exo1 - i
import matplotlib.pyplot as plt
#Exo2
import time
#Exo3
import tkinter as tkt

# %% zone de l'exo1
def Exo1():
    # - b
    url = "https://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=UUtfSA9xVHYALVBnVCIELVE5DjsIfgUiBnpXNA9qAH1SOVIzVjZSNFc5A34HKAcxV3oFZgoxBTUAawZ%2BC3lWN1E7XzMPZFQzAG9QNVR7BC9Rfw5vCCgFIgZsVzEPfABiUjdSNlYrUjFXOAN%2FBzYHN1dhBXoKKgU8AGUGZQtuVj1RMF8zD21UNABpUC1UewQ2UWAOaggwBTwGMFdkDzcAY1JkUjFWZlJmVzsDfwc1BzVXZAVhCjAFNQBrBmkLeVYqUUtfSA9xVHYALVBnVCIELVE3DjAIYw%3D%3D&_c=9ecb7356947e26938fe1bf5854198bfd"
    # - c
    try:
        api_request = requests.get(url)
        data = json.loads(api_request.content)
    except Exception as e:
        data = "Error..."
    # - d
    print(type(data) is dict)
    # - e et f
    ele = ['request_key','request_state','message','model_run','source']
    print("\n".join(str(data.pop(x)) for x in ele if x in data.keys()))
    #  - g
    print(type(data['2022-04-01 11:00:00']) is dict)
    print(data['2022-04-01 11:00:00'])
    # - h
    print(data['2022-04-01 11:00:00']['temperature']['2m'])
    print(data['2022-04-01 11:00:00']['temperature']['sol'])
    # - i
    print(data['2022-04-01 11:00:00']['humidite'])
    # - k
    char_to_sup = {'-' : '', ':' : '', ' ' : ''}
    dates_str = list(filter(lambda y : all(map(str.isdigit, y.translate(str.maketrans(char_to_sup)))),data.keys()))
    lesDates = list(map(lambda x : datetime.strptime(x,"%Y-%m-%d %H:%M:%S"), dates_str))
    print(lesDates)
    lesTempA2m = list(map(lambda x : round(x - 273.15,2), [data[x]['temperature']['2m'] for x in dates_str]))
    print(lesTempA2m)
    lesTempAuSol = list(map(lambda x : round(x - 273.15,2), [data[x]['temperature']['sol'] for x in dates_str]))
    print(lesTempAuSol)
    lesHumiditesA2m = [data[x]['humidite']['2m'] for x in dates_str]
    print(lesHumiditesA2m)
    # - m
    plt.figure(figsize=(10,10))
    plt.subplot(211)
    plt.title("Température et Humidité")
    plt.plot(lesDates, lesTempA2m,"b:o",label='2m')
    plt.plot(lesDates, lesTempAuSol,"r:o", label = 'sol')
    plt.ylabel("Température °C")
    plt.grid('on')
    plt.legend()
    
    plt.subplot(212)
    plt.plot(lesDates,lesHumiditesA2m,"g:o")
    plt.ylabel("Humidité")
    plt.xlabel("Date")
    plt.grid('on')
    plt.legend()
    
    plt.show()

# %% zone de l'exo2
def Exo2():
    Affichage("Début exo 2")
    Affichage2("Temps en secondes de la fonction")
    
def temps_fonction(fonction):
    def inner(*param, **param2):
        start = time.process_time()
        fonction(*param, **param2)
        end = time.process_time()
        print(f"\nLe temps écoulé est de {round(end - start,10)} secondes...")
    return inner

@temps_fonction
def Affichage2(v):
    print("Execution des instructions", v)

def mon_decorateur(fonction):
    def inner(*param, **param2):
        print("Action avant .............. ")
        fonction(*param, **param2)
        print("Action après ..............")
    return inner

#pour appliquer le décorateur à une fonction, il suffit d’ajouter
# @mon_decorateur juste avant la méthode
@mon_decorateur
def Affichage(v):
    print("Execution des instructions", v)

# %% zone de l'exo3
def Exo3():
    fenetre = tkt.Tk()
    #créer un widget label
    #monlable = tkt.Label(fenetre, text="premier code tkinter")
    #empaqueter le widget dans la fenetre
    #monlable.pack()
    #monlabel.pack(slide="left")
    #monlabel.pack(expand=1)
    # lancer la fenetre
    #fenetre.mainloop()
    
    fenetre.title('deuxieme fenetre ')
    #fenetre.iconbitmap( ' iconedeprog. ico ' )
    fenetre.geometry( "450x150" )
    #créer un widget Label
    monlabel1=tkt.Label(fenetre, text="label1")
    monlabel2=tkt.Label(fenetre,text="1abel2")
    monlabel3=tkt.Label(fenetre,text="1abel3")
    monlabel4=tkt.Label(fenetre, text="1abel4")
    #empaqueter Ie widget dans ta fenetre ave grid
    monlabel1.grid(row=1, column=0)
    monlabel2.grid(row=1, column=1)
    monlabel3.grid(row=2, column=2)
    monlabel4.grid(row=3, column=0, columnspan=3)
    entreeNom = tkt.Entry(fenetre, width=50, bg="grey", fg="blue")
    def myClick():
        monlabel4.config(text="Hello" + entreeNom.get(),fg="red")
   
    entreeNom.grid(row=0, column=0, columnspan=3)
    #Ajouter un boutton pour quiter
    monbouton= tkt.Button(fenetre, text="changer" ,padx=10,pady=10,comnand=myClick()).grid(row=4,column=4)


# %% zone du main
if __name__ == '__main__' :
    #Exo1()
    #Exo2()
    Exo3()