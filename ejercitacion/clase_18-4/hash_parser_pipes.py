'''Considerando el programa noblock.py, realizar un programa que lance dos procesos hijos que intenten encontrar el 
nonce para un No-Bloque con una dificultad dada. El hijo que lo encuentre primero debe comunicarse con el padre mediante 
una señal guardando el nonce en una fifo para que el padre pueda leerla. Hacer otra versión pero utilizando pipes.'''