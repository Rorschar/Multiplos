# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducci�n no es correcta.

def esmultiplo(num1, num2):
	multiplo = bool()
	if num1%num2==0:
		multiplo = True
	return multiplo

if __name__ == '__main__':
	numero1 = int()
	numero2 = int()
	print("N�mero 1:", end="")
	numero1 = int(input())
	print("N�mero 2:", end="")
	numero2 = int(input())
	if esmultiplo(numero1,numero2):
		print(numero1,"es multiplo de",numero2)
	else:
		print(numero1,"No es multiplo de",numero2)
