# Conversión de temperatura:
#Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

def converted_temperature(celsius):
    #formula para pasar de celsius a fahrenheit
    fahrenheit = celsius * 9/5 +32
    #retornamos ese valor
    return fahrenheit

#le damos la temperatura
temp_celsius = 25
#llamamos a la funcion 
temp_fahrenheit = converted_temperature(temp_celsius)
#imprimimos 
print(f"La temperatura {temp_celsius} en grados celsius, pasamos a fahrenheit y queda en {temp_fahrenheit}")