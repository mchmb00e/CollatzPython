import time

i=int(input("Numero: "))
count=True
var=i
while count == True:
    time.sleep(0.2)
    print(var)
    if var%2 == 0:
        var=var/2
        print("Par")
    elif var%2 == 1:
        var=(var*3)+1
        print("Impar")
    if var == 1.0:
        print("Ciclo infinito.")
        i=i+1
        var=i
        print("Siguiente numero: ",i)
    print("//////////////")