def my_function () :
 print("Selon la relation fondamentale de l'hydrostatique On a P2-P1= Mvessence.g.(Z1-Z2) ")
 Mves=input("Entrez la masse volumique de l'essence : ")
 P1=input("Entrez la pression exercée sur le point 1")
 H=input("Entrez la hauteur H :")
 try:
     Mves=float(Mves)
     P1=float(P1)
     H=float(H)
     g=10
     P2= P1 + (Mves*H*g)
     print("La pression en le point 2 est", P2)
 except:
     print("Erreur")
 print("Selon la relation fondamentale de l'hydrostatique On a P3-P2= Mvmercure.g.(Z1-Z2) ")
 Mvem=input("Entrez la masse volumique de mercure : ")
 h=input("Entrez la hauteur h :")
 try:
     Mvem=float(Mvem)
     h=float(h)
     g=10
     P3= P2 - (Mves*h*g)
     print("La pression en le point 3 est", P3)
 except:
     print("Erreur")
 my_function