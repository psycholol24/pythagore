import os
from mod import *
import time


while True:	

	print("que veut tu faire ?")
	print("<C> calculer l'hypotenuse d\'un triangle rectangle ou <V> verifier q\'un triangle est rectangle ou <A> pour arreter")

	
	try:	
		pythagore = input(">")

	except ValueError:
		
		print("erreur, sorry")
		time.sleep(10)

	
	if pythagore == "C":
		calculer_hypotenuse_Pythagore(2, 2)

	elif pythagore == "V":
		verifier_pythagore(2, 2, 2)

	elif pythagore == "A":
		os.system()

	else:
		print("je n\'ais pas compris")



os.system("pause")
  