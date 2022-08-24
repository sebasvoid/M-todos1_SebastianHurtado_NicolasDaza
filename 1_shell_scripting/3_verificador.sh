
pass=0
function verif(){
	if [ $1 -eq 0 -o $1 -eq 1 ];then
		pass=1
	else
		echo "De nuevo"
	fi
}
while [ $pass -eq 0 ] 
do 
	echo "valor a ingresar: "
	read num
	n=$num
	verif $n
done

