read x; read n
i=0
l=$x
while [ $i -lt $n ]
do
((l+=x))
read u
l=$((l - u))
((i++))
done
echo $l