#creado en clase 


if [ $# -eq 0 ]; then
	echo --- Programa sin parametros ---
	echo --- Parametro 1: n-factorial ---
	exit 1
fi

n=$1

typeset -i factorial=1

if [ $n -eq 0 ] || [ $n -eq 1 ]; then
	echo $1 $factorial 
else
	while [ $n -gt 1 ]
	do
		let factorial=$factorial*$n
		let n=$n-1
	done
	echo $1 $factorial
fi
