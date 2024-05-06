# Manejo de Excepciones en Python

Este repositorio contiene cuatro programas escritos en Python que ejemplifican el manejo de diferentes tipos de excepciones: `ZeroDivisionError`, `ValueError`, `IndexError` y `TypeError`.

## Programas

### 1. División por Cero

Este programa solicita al usuario dos números y realiza la división entre ellos. Se maneja la excepción `ZeroDivisionError` para evitar que el programa se detenga si el segundo número es cero.

### 2. Conversión de Tipo de Datos

En este programa, se solicita al usuario ingresar un número y se intenta convertirlo a un entero. Se maneja la excepción `ValueError` para informar al usuario si no ingresa un valor válido.

### 3. Acceso a un Índice Fuera de Rango

El programa crea una lista vacía y luego intenta acceder a un elemento en una posición específica. Se maneja la excepción `IndexError` para evitar que el programa se bloquee si se intenta acceder a un índice que está fuera del rango de la lista.

### 4. Operaciones con Tipos de Datos Incorrectos

Se proporciona una función que recibe dos argumentos y realiza alguna operación matemática entre ellos. Se maneja la excepción `TypeError` para evitar que el programa se bloquee si los argumentos no son del tipo de datos esperado.

## Manejo de Excepciones

Cada programa incluye comentarios en el código explicando cómo se manejan las excepciones correspondientes. Se utiliza un bloque `try-except` para capturar la excepción específica y manejarla de manera adecuada, evitando que el programa se detenga inesperadamente.
