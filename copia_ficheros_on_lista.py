#copia ficheros de un directorio a otro, seleccionando únicamnete aquellos que aparezcan en una lista almacenada en formato txt
#para poder utilizar r' en los directorios fuente y destino, han de ir sin \ al final
#es necesario quitarle el último caracter a la cadena final de la linea line[:-1]

from shutil import copyfile

source_directory = r'c:\source_directory'
destination_directory = r'c:\destination_directory'
file_list = r'C:\file_list.txt'

f = open(file_list)
for line in iter(f):
    
    source_file =  source_directory +'\\' + line[:-1]
    
    destination_file = destination_directory  +'\\' + line[:-1]
    print line[:-1]
    copyfile(source_file, destination_file)
f.close()
