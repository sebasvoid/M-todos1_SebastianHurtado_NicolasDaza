x=0
while IFS= read -r line
do
  rutas_archivos[x]=$line
  x=`expr $x + 1`
done < $1

echo " ${rutas_archivos[2]}"
