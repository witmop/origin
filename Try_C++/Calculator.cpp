#include <iostream>
#include <string>
using namespace std;

int main(){
    int num1,num2;
    char operation;
    cout<<"Введите первое число ";
    cin>>num1;

    cout<<"Введите операцию (+ - * /) ";
    cin>>operation;

    cout<<"Введите второе число ";
    cin>>num2;
    
    switch(operation){
        case '+':
            cout<<num1+num2<<endl;
            break;
        case '-':
            cout<<num1-num2<<endl;
            break;
        case '*':
            cout<<num1*num2<<endl;
            break;
        case '/':
            if (num2==0){
                cout<<"Невозможно деление на 0";
                break;
            }
            else{
                cout<<num1/num2<<endl;
                break;
            }
        default:
            cout<<"Неизвестная операция"<<endl;
            break;
    }       
    return 0;
}