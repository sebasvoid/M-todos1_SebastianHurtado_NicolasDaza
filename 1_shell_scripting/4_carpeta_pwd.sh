v=0
for i in *;
do 
	if [ $i == "$1" ]
	then
		v=`expr $v + 1`
	fi
done

if [ $v -eq 0 ]
then
	mkdir $1
	echo "Carpeta anadida al dispositivo"
else
	echo "Ya se encuentra"
fi

