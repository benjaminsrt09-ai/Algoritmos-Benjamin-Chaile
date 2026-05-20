#6. De un operario se conoce su sueldo y los años de antigüedad. Se pide
#confeccionar un programa que lea los datos de entrada e informe:
#a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10
#años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10
#años, otorgarle un aumento de 5 %.
#c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
#cambios.

sueldo = int(input("ingrese el valor de su sueldo "))
años = int(input("ingrese sus años de antigüedad "))

if sueldo < 500 and años >= 10:
    aumento20 = (sueldo * 20)/100
    print("su sueldo más el aumento correspondiente pasa a ser de ")
    print(sueldo + aumento20)

if sueldo < 500 and años < 10:
    aumento5 = (sueldo * 5 )/100
    print("su sueldo más el aumento correspondiente pasa a ser de ")
    print(sueldo + aumento5)

else:
    if sueldo >= 500:
        print("a usted no le corresponde aumento, su sueldo es sigue siendo de ")
        print(sueldo)

