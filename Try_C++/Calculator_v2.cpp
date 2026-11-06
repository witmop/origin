#include <iostream>

using namespace std;

int main(){
    float num1,num2;
    cout<<"Enter num1: ";
    cin>>num1;
    cout<<"Enter num2: ";
    cin>>num2;
    // + - * /
    char math;
    cout<<"Enter math simvol: ";
    cin>>math;
    if (math == '+'){
        cout<<"Sum result: "<<num1+num2<<endl;
    }

    else if (math== '-'){
        cout<<"Diff result: "<<num1-num2<<endl;
    }

    else if (math == '*'){
        cout<<"Multip result: "<<num1*num2<<endl;
    }

    else if (math == '/'){
        if (num2==0){
            cout<<"Невозможно деление на 0"<<endl;
        }
        else {
        cout<<"Div result: "<<num1/num2<<endl;
        }
    }
    else{
        cout<<"Неккоректный ввод"<<endl;
    }
    return 0;
}