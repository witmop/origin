// Вывод случайных чисел
#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
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

// int main(){
//     int matrix[3][2]={{1,2},{3,4},{5,6}};
//     cout<<matrix[0][1]<<endl;
//     return 0;
// }


// Динамический массив данных

// int main(){
//     int *nums=new int[3];   // выделили память
//     nums[0]=45;
//     cout<<nums[0]<<endl;
//     delete[] nums;        // очистка памяти или просто delete nums если переменная

//     return 0;

// }


// Работа со строками и символами

// int main(){
//     char word[]={'H','i'};  //так бы пришлось делать в C
//     for (int i=0;i<2;i++){
//         cout<<word[i];
//     }
//     cout<<endl;
//     string words = "Hello world!";
//     cout<<words<<endl;
//     cout<<words[1]<<endl;
//     getline(cin,words);
//     cout<<"New words: "<<words<<endl;
//     return 0;
// }


// Создание функций

// void - если функция ничего не возвращает

// void print(string word);        // скелет функции (даёт возможность перенести саму функцию вниз)

// int add(int a,int b){
//     return a+b;
// }

// int main(){
//     string func_word="мир";
//     print("пир");       //или print(func_word) 
//     int result;
//     result=add(5,3);
//     cout<<result<<endl;
//     return 0;
// }

// void print(string word="world"){    
//     cout<<"Hello "<<word<<endl;
// }


// Перегрузка функций

// void print(string word){
//     cout<<word<<endl;
// }

// void print(int word){
//     cout<<word<<endl;
// }

// void add (int a, int b){
//     int res = a+b;
//     print(res);
// }

// void add(int a, int b, int c){
//     int res= a+b+c;
//     print(res);
// }

// int main(){
//     print("some");
//     add(5,10);
//     add(11,11,11);
//     return 0;
// }


// Указатели и ссылки

// int main(){
//     // Ссылки
//     int num=10;
//     int &a=num;     //теперь a не переменная, а ссылка(почти не занимает место), ссылка -указывает на ячейку, где хранятся данные
//     cout<<&num<<endl;       // выводит ссылку на переменную
//     cout<<&a<<endl;
//     // Указатели
//     int val=12;
//     int *ptrval=&val;
//     cout<<&val<<" - "<< val<<endl;
//     cout<<ptrval<<" - "<<*ptrval<<endl;
//     *ptrval=20;     // меняем знач. переменной
//     ptrval=nullptr; //сбрасываем знач. указателя
//     return 0;
// }
// Пример

// void minimal(int *arr,int len){            //если сделать (int arr[],int len) то кол-во занимаемой памяти увеличится в 2 раза
//     int min=*arr;       //если работаем с указателями, то в указатель передаётся не ввесь массив, а только первый элемент
//     for (int i=0; i<len;i++){
//         if (min>*(arr+i)){
//             min=*(arr+i);
//         }
//     }
//     cout<<"Minimal: "<<min<<endl;
// }

// int main(){
//     int arr[]={5,7,4,5,-2};
//     minimal(arr,5);

//     return 0;
// }


// Работа с файлами

// int main(){
//     // ofstream file("test.txt",ios_base::out);     записываем данные
//     // if (file.is_open()){    //на всякий случай проверяем открыт ли файл             
//     //     file<<"Hello world";
//     //     file.close();
//     // }     
     
//     ifstream file("test.txt");
//     // string temp;
//     // file >> temp;    так считается только первое слово
//     // cout<<temp<<endl;
//     char temp[100];
//     file.getline(temp,100);
//     cout<<temp<<endl;
//     file.close();

//     return 0;
// }


// Структуры данных

struct Point {
    int x,y;

};

struct Tree {
    string name;
    int ages;
    bool is_alive;
    float height;
    Point place;

    void get_info(){
        cout<<"Name: "<<name<<endl;
    }

};

int main(){
    Tree dub;
    dub.name="Дуб";
    dub.ages=24;
    cout<<dub.name<<endl;
    dub.get_info();
    dub.place.x=10;
    dub.place.y=5;
    cout<<dub.place.x<<endl;
    return 0;
}