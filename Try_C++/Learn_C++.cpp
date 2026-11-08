// Вывод случайных чисел
#include <iostream>
// Если возникает ошибка возможно нужно #include <time.h>
using namespace std;

// int main(){
//     srand(time(NULL));     //убирает зависимость от времени(теперь при вызове программы каждый раз новое число)
//     int result= 1+ rand() %20; //число от 1 то 20
//     cout<<result<<endl;
//     return 0;
// }

// Циклы
int main(){
    for (int i=0;i<12;i+=2){
        cout<<"Cycles for: "<<i<<endl;
    }
    int j=1;
    while (j<33){
        j*=2;
        cout<<"Cycles while: "<<j<<endl;
    }
    int k=100;
    do {            //отличие от while в том что цикл в любом случае сработает хотя бы 1 раз
        k-=10;
        cout<<"Cycles do while: "<<k<<endl; 
    } while(k<10);
    return 0;
}