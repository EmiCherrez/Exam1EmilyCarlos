find exam1/data/singlecell . -type f | sed -n 's/..*\.//p' | sort | uniq -c > extensiones.txt
