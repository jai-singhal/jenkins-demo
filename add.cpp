#include <iostream> 
using namespace std; 
  
int main(int argc, char** argv) { 
    cout << "You have entered " << argc 
         << " arguments:" << "\n"; 
  
    if(argc == 3){
        cout << atoi(argv[1]) + atoi(argv[2]);
        cout << endl;
    }
  
    return 0; 
} 