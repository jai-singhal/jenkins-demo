echo "Run add.py with arg 6, 4"
python3 add.py 6 4
echo "-----------------------------"

echo "Run add.cpp with arg 5, 97"
g++ add.cpp -o "add"
./add 5 97
echo "-----------------------------"

echo "Execute run all files uing python which uses subprocess"
python3 runAllfiles.py
echo "-----------------------------"

echo "Run add.sh with arg 65, 21"
sh add.sh 65 21
echo "-----------------------------"
