cantidad=20


function factorial2 (){
	a=1
	y=$1
	if [ $y -le 1 ]
	then
		fac=1
	else
		while [ $y -gt 1 ]
		do
			a=`expr $a \* $y`
			y=`expr $y - 1`
		done
		fac=$a
	fi
}

for x in `seq 0 $cantidad`
do
	c=$x
	factorial2 $x
	echo "$c ! = $fac"
done
