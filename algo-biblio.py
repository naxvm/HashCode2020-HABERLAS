#/usr/bin/python3

from clases import *
import functools
from parsers import parse, escribir_resultado
import sys

numero_libros = []
tiempos_registro = {}

in_file = 'input_data/' + sys.argv[1]
out_file = 'output_data/' + sys.argv[1]
print(in_file)
books, libraries, days = parse(in_file)





def mejor_biblio(libraries, scanned):
    puntuaciones = []
    best_library = libraries[0]
    rest = []
    best_score = 0
    for library in libraries[1:]:
        score = library.getScore(scanned)
        if score > best_score:
            best_score = score
            best_library = library
        else:
            rest.append(library)
        
    return best_library, rest
 
    # puntuaciones = list(map(calcular_puntuacion, libraries)).sort()

    # return puntuaciones[-1]





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

salida = []
libros_ya_escaneados = []
while len(libraries) > 0:
    best_lib, libraries = mejor_biblio(libraries, libros_ya_escaneados)
    libros = best_lib.scan_books()
    libros_ya_escaneados = list(set(libros + libros_ya_escaneados))
    salida.append((best_lib, libros))

escribir_resultado(salida, out_file)

