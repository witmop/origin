// Вывод случайных чисел
#include <iostream>
#include <cmath>
// Если возникает ошибка возможно нужно #include <time.h>
using namespace std;

// int main(){
//     srand(time(NULL));     //убирает зависимость от времени(теперь при вызове программы каждый раз новое число)
//     int result= 1+ rand() %20; //число от 1 то 20
//     cout<<result<<endl;
//     return 0;
// }

// Циклы
// int main(){
//     for (int i=0;i<12;i+=2){
//         cout<<"Cycles for: "<<i<<endl;
//     }
//     int j=1;
//     while (j<33){
//         j*=2;
//         cout<<"Cycles while: "<<j<<endl;
//     }
//     int k=100;
//     do {            //отличие от while в том что цикл в любом случае сработает хотя бы 1 раз
//         k-=10;
//         cout<<"Cycles do while: "<<k<<endl; 
//     } while(k<10);
//     return 0;
// }


// Операторы в циклах
// int main(){
//     for (int i=0;i<15;i+=2){
//         cout<<"EL: "<<i<<endl;
//         // if (i==10){
//         //     break;
//         // }
//     }
// }


// Массивы в данных

// int main(){
//     int nums[3];
//     for (int i=0;i<3;i++){
//         nums[i]=pow(i,2);
//         cout<<nums[i]<<endl;
//     }
//     float nums2[3]={228,322,52};
//     cout<<nums2[0]<<endl;

//     float numbers[5];
//     for (int i=0;i<5;i++){
//     cout<<"Enter number: "<<endl;
//     cin>>numbers[i];
//     }
//     int nums_sum=0;
//     float min=numbers[0];
//     for (int el=0; el<5;el++){
//         nums_sum+=numbers[el];
//         if (numbers[el]<min){
//             min=numbers[el];
//         }
//     }
//     cout<<"Сумма "<<nums_sum<<endl;
//     cout<<"Минимальное число "<<min<<endl;
//     return 0;

// }


// Многомерные массивы

int main(){
    int matrix[3][2]={{1,2},{3,4},{5,6}};
    cout<<matrix[0][1]<<endl;
    return 0;
}