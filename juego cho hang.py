import random as rd

billetera=10
gana=0
continuar="si"
print("---Bienvenido a cho han---")
print("Usted tiene €{} en la billetera".format(billetera))
while billetera>0 and continuar=="si":
    apuesta=int(input("Ingrese apuesta: "))
    if apuesta <= billetera:
        dado1=rd.randint(1,6)
        dado2=rd.randint(1,6)
        total=dado1+dado2
        resto=total%2
        parimpar=input("Adivina ¿paro impar? ")# par o impar
        print("Salio: {} + {} = {}".format(dado1,dado2,total))
        if resto==0 and parimpar=="par":
            print("¡Gano¡")
            billetera+=apuesta
            gana+=1
        elif resto!=0 and parimpar=="impar":
            print("¡Gano¡")
            billetera+=apuesta
            gana+=1
        else:
            print("¡Perdio¡")
            billetera-=apuesta
        print("Billetera: {}".format(billetera))
        if billetera!=0:
            continuar = input("¿Desea seguir jugando?")#si o no
            print("--------------------")
    else:
        print("La apuesta mayor al dinero que tiene en la billetera")
print("usted gano {} partidas".format(gana))
print("Gracias por jugar¡")
