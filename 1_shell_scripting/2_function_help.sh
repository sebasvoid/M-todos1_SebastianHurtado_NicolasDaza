function help(){
        echo "Debe incluir 3 parametros : posicion inicial, velocidad inicial y tiempo total."
}
if ! [ $# -eq 3 ]; then
        echo "son tres"
        help
        exit 1
else
        echo "corriendo programa"
fi

