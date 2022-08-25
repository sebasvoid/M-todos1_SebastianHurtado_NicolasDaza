n=20
r=3
let resta=$n*$r
function factorial(){
	a=1
	if [ $1 -le 1 ] 
	then
		valor=1
	else
		var=$1
		while [ $var -gt 1 ] 
		do
			let a=$a*$var
			let var=$var-1 
		done
		valor=$a
	fi
}
factorial $n 
num1=$valor

factorial $r
num2=$valor

let resultado=$num1/$num2
echo $resultado
