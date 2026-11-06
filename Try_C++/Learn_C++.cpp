// Вывод случайных чисел
#include <iostream>
// Если возникает ошибка возможно нужно #include <time.h>
using namespace std;

int main(){
    srand(time(NULL));     //убирает зависимость от времени(теперь при вызове программы каждый раз новое число)
    int result= 1+ rand() %20; //число от 1 то 20
    cout<<result<<endl;
    return 0;
}