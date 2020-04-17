# Zipper 

Zipper.py es un script escrito en Python para comprimir archivos en modo multihilo.
Su funcionamiento es bastante básico, toma la lista de archivos candidatos, lo parte a la mitad y crea un hilo para cada subgrupo de archivos. Esto puede modificarse libremente dependiendo de la cantidad de hilos disponibles que tenga nuestro sistema.
La compresión es la misma que utiliza el comando "tar" en Linux. Esto significa que cualquier archivo que haya sido comprimido por este script, podrá ser descomprimido mediante la forma estándar de "tar".

<h2> Uso </h2>
