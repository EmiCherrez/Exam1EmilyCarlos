find exam1/data/singlecell . -type f | sed -rn 's|.*/[^/]+\.([^/.]+)$|\1|p' | sort | uniq -c | sort -nr > extensiones2.txt
