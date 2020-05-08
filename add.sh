echo "add.sh is running"
echo "It will add two number given as args"
echo "First arg: $1"
echo "Second arg: $2"
a=$1
b=$2
sum=` expr $a + $b `
echo $sum
