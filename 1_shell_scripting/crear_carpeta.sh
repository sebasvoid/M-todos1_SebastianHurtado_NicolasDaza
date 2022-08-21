echo "ingrese el nombre de la carpeta";
read nombre
for x in *; 
do

 if [[ $x == $nombre ]]; then

   echo "la carpeta esta en el directorio actual"
   exit
   

 else
   mkdir $nombre
   echo "se ha creado la carpeta"
   exit
  fi
done


~
~
~

