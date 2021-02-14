ListadeMaestros=[]
n=1
while n<5:
    print("Introduce los datos del maestro: ",n)
    nom=str(input("Cual es el nombre del maestro? \n"))
    uap=str(input("Cual es el nombre de la Unidad de aprendizaje? \n"))
    sem=int(input("Cual es el semestre en el que se imparte? \n"))
    maestro=[nom,uap,str(sem)]
    ListadeMaestros.append([maestro])
    print(maestro)
    n+=1    
    #i+=1
print(ListadeMaestros)
