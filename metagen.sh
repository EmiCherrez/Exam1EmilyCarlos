#Para trabajar con una columna e interfiera en el conteo
cut -d " " -f 1 exam1/data/metagen/infants_metagenome.txt | tail -n +7 > metagendata.txt

#Para realizar el conteo de registros de especies.

cut -d '|' -f 7 metagendata.txt | sort | uniq -c > metagen.txt

#busqueda de los fragmentos "TATA, GAGA O GATA"

grep -in -E "TATA|GAGA|GATA" exam1/data/metagen/mygenomemap.sam | sort > Gata.txt
