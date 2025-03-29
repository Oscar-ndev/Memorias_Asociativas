# Memorias Asociativas

## Definición
Una memoria asociativa es un sistema que asocia un estímulo con una respuesta. Posteriormente, cuando el estímulo se presenta, el sistema produce la respuesta correspondiente a dicho estímulo.

## Forma de trabajo
Una Memoria Asociativa es una estructura de contenido direccionable que mapea un conjunto de patrones de entrada (estímulos) a un conjunto de patrones de salida (respuestas).

## Tipos
- Memorias Autoasociativas: Los patrones de entrada son iguales a los de salida.
- Memorias Heteroasociativas: Los patrones de entrada son diferentes a los de salida.

## Descripción
En este repositorio se tienen las siguientes Memorias Asociativas

Memorias Clásicas:
* Lernmatrix: es una memoria heteroasociativa que puede funcionar como un clasificador de patrones binarios si se escogen adecuadamente los patrones de salida.
  
* Linear Associator: es una memoria asociativa simple que se utiliza para almacenar pares de patrones de entrada y salida. El modelo de este tipo de memoria se basa en una función lineal que toma un patrón de entrada y produce un patrón de salida asociado, es decir, la relación entre los patrones de entrada y salida es lineal.
  
* Hopfield: es una red neuronal recurrente que sirve como memoria asociativa. Está basada en unidades neuronales completamente conectadas, donde las salidas de las neuronas se retroalimentan entre sí. Es especialmente útil para almacenar patrones y recuperarlos incluso cuando están parcialmente dañados o incompletos.

Memorias No Clásicas:
* Alfa-Beta: se utiliza principalmente en el contexto de procesamiento de información temporal o memoria de corto plazo. Este modelo utiliza dos mecanismos: alfa y beta, que ajustan el nivel de activación de las neuronas basándose en el historial de entradas.
