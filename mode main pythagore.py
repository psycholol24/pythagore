# -*-coding:Latin-1 -*
import time
import os
import math

def calculer_hypotenuse_Pythagore(AB, AC):

    try:    

        AB = input("cote AB : ")
        AC = input("cote AC : ")
   
        AB = int(AB)
        AC = int(AC)

    except ValueError:

        print("erreur, veuller reessayer")
        time.sleep(10)


        hypo = AB * AB + AC * AC
        hypo = math.sqrt(hypo)
        print(hypo)




def verifier_pythagore(BC, AB, AC):

    BC = input("cote BC (hypotenuse) : ")
    AB = input("cote AB : ")
    AC = input("cote AC : ")
       
    AB = int(AB)
    AC = int(AC)
    BC = int(BC)

    verif_1 = BC * BC
    verif_2 = AB * AB + AC * AC

    if verif_1 == verif_2:
        print("le triangle est rectangle")
    else:
        print("le triangle n'est pas rectangle")



if __name__ == "__main__":
    calculer_hypotenuse_Pythagore(3, 3)
    os.system("pause")
