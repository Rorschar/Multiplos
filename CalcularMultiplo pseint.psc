Funcion Multiplo <- EsMultiplo (num1,num2)
	Definir multiplo como Logico;
	Si num1 % num2 = 0 Entonces
		multiplo <- Verdadero
	FinSi
Fin Funcion

Proceso CalcularMultiplo
	Definir numero1,numero2 Como Entero;
	Escribir Sin Saltar "Número 1:";
	Leer numero1;
	Escribir Sin Saltar "Número 2:";
	Leer numero2;
	Si EsMultiplo(numero1,numero2) Entonces
		Escribir numero1, "es multiplo de" numero2;
	SiNo
		Escribir numero1, "No es multiplo de",numero2;
	FinSi
FinProceso
	