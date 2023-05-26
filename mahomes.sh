cut -d ',' -f 5,18,21 exam1/data/mahomes/sites.csv > pdb.csv

#Conteo unicos de columnas

cut -d ',' -f 1,2,3 pdb.csv | sort | uniq -c > pdb_count.csv

# Para imprimir el valor total de elementos unicos.

cut -d ',' -f 1,2,3 pdb.csv | sort | uniq -c | wc -l

