#/usr/bin/python3

from clases import *
import functools
from parsers import parse, escribir_resultado
import sys

numero_libros = []
tiempos_registro = {}

in_file = 'input_data/' + sys.argv[1]
out_file = 'output_data/' + sys.argv[1]

books, libraries, days = parse(in_file)



def orden_libs_fn(l1, l2):
    if l1.treg < l2.treg:
        return -1
    elif l1.treg > l2.treg:
        return 1
    else:
        if l1.rate > l2.rate:
            return -1
        elif l1.rate < l2.rate:
            return 1
        else:
            if len(l1.books) > len(l2.books):
                return -1
            elif len(l1.books) < len(l2.books):
                return 1
            else:
                return 1

# hay que registrar primero las bibliotecas que tardan menos en 'registrarse'
total_libraries = sorted(libraries, key=functools.cmp_to_key(orden_libs_fn))

salida = []
nbooks = 30000
for library in total_libraries:
    salida.append((library, library.coge_libros(nbooks)))

escribir_resultado(salida, out_file)

