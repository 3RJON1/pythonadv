# file_path = "example"
# file = open(file_path)
#
# content = file.read()
# print(content)
#
# file.close()

import os


with open('example', 'r') as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()


with open("example", 'w') as file:
    file.write("A miri nuk po shkrun kod po rrin telefon")


lines = ["Amiri edhe Noarti shkrujn shume shpejt\n", "Eerjoni edhe germaniumi hajne shume haribo"]

with open("example", 'w') as file:
    file.writelines(lines)