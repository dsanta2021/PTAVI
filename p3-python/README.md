# p3-python

Repositorio de plantilla para la práctica 3 (Python avanzado) de PTAVI.

Recuerda que antes de empezar a trabajar con esta practica deberías realizar un
fork de este repositorio, con lo que crearás un nuevo repositorio en tu cuenta,
cuyos contenidos serán una copia de los de este.
Luego tendrás que clonar ese repositorio para tener una copia local con
la que podrás trabajar. No olvides luego hacer commits frecuentes, y
sincronizarlos con el servidor (`git push`) antes de la fecha de entrega
final de la práctica. Recuerda también que para que pueda ser corregido, el
repositorio deberá ser público a partir de la fecha de entrega.

[Enunciado de esta práctica](https://gitlab.com/cursomminet/code/-/blob/master/p3-python/ejercicios.md).

**- Ejercicio 4_"test_mio":**

Un programa que relaiza un test que prueba diferntes aspectos del fichero 
**mysound.py**, hecho con una función *test_sound* que usa **unittest** para 
comprobar que:
 
  - Comprueba que el número de muestras generadas es el esperado.
  - Comprueba que los valores de una onda senoidal coinciden, se acerca al 
    valor esperado,
    son más grandes, pequeños o no son los esperados.
  - Compara el valor de dos señales sonoidales diferentes. Usa recursos de 
    **unittest** para saber si los valores de las señales son iguales, uno 
    mayor que otro, menor, diferentes ...

**- Ejercicio 5_ "mysoundsin":**

Un programa que consta de una calse, **SoundSin**, que hereda los parámetros de
la clase **Sound** del fichero **mysound**. Al inicializarlo se creará un buffer
y una señal soinoidal con parámetros.

**- Ejercicio 6_ "test_soundsin":**

En este test, se han creado tres métodos de prueba: *test_init*, *test_sin* y 
*test_bar*. El primero, verifica si todos los atributos (duración, frecuencia y 
amplitud) de la instancia de *SoundSin* se han inicializado correctamente. El segundo,
hace algunas comprobaciones de la señal senoidal como: calcular el valor esperado 
para la primera muestra según la fórmula del sonido senoidal o comprobar que el primer
valor de la lista samples coincide con ese valor esperado. Por último, el tercero,
Comprueba que el número de líneas y la longitud de cada línea son los esperados según 
los valores pasados al constructor.

**- Ejercicio 7_ "soundops"**

El programa consta de una sola función *soundadd* que puede sumar dos listas de forma 
funcional. Si las listas tienen el mismo número de elementos, se usa la función *map* 
junto con *operator.add* para sumar las dos listas. Por otro lado, si las listas tienen
un tamaño diferente se utiliza *zip_longest* de la biblioteca **itertools**. Esta 
función combina las listas rellenando los valores faltantes con un valor predeterminado 
(por defecto None), que en este caso *fillvalue* es 0.

**- Ejercicio 8_ "test_soundadd"**

Un test compuesto por cinco funciones que usan **unittest** y que sirven todas para 
comprobar el funcionamiento de la función *soundadd* del ejercicio anterior, mas 
concretamente, para: 

    - *test_different_lenght* -> Verifica que al sumar dos señales con diferentes 
      tiempos la duración de la señal resultante es el mismo que el mayor de las que
      se han sumado.
    - *test_equal_lenght* -> Confirma que en el caso de que las señales que se suman
      tengam una duración igual, la duración de la señal final tendrá la misma duración
      que las otras señales.
    - *test_s1_longer* y *test_s2_longer* -> Ambas verifican que si una de las dos
      señales es más pequeña que la otra en timpo, el timpo del sonido final será
      igual al de la señal de mayor duración.
    - *test_non_lenght* -> Si hay un caso en el que las señales no tengan nada de 
      duración, la señal final tendrá la misma duración (0) y los mismo valores de 
      amplitus, ninguno.

