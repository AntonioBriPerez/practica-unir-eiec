"""
License: Apache
Organization: UNIR
"""

import os
import sys

DEFAULT_FILENAME = "words.txt"
DEFAULT_DUPLICATES = False
DEFAULT_ORDER = "asc"  # Orden ascendente por defecto

def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise RuntimeError(f"{type(items)} can't be sorted")

    return sorted(items, reverse=(not ascending))

def remove_duplicates_from_list(items):
    return list(set(items))

if __name__ == "__main__":
    filename = DEFAULT_FILENAME
    remove_duplicates = DEFAULT_DUPLICATES
    order = DEFAULT_ORDER

    # Modificación para aceptar un tercer parámetro para el orden
    if len(sys.argv) == 4:
        filename = sys.argv[1]
        remove_duplicates = sys.argv[2].lower() == "yes"
        order = sys.argv[3].lower()
    else:
        print("Filename must be indicated as first argument")
        print("Second arguments asks if you want to remove duplicates")


        sys.exit(1)

    ascending = order == "asc"
    print(f"Se leerán las palabras del fichero {filename}")
    file_path = os.path.join(".", filename)
    if os.path.isfile(file_path):
        word_list = []
        with open(file_path, "r") as file:
            for line in file:
                word_list.append(line.strip())
    else:
        print(f"File {filename} does not exists")
        word_list = ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    if remove_duplicates:
        word_list = remove_duplicates_from_list(word_list)

    print(sort_list(word_list, ascending=ascending))
