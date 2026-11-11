#include <iostream>

using namespace std;

int main(){
    srand(time(NULL));
    int rand_num=1+rand()%100;
    bool stop=false;
    int user_num;
    while (!stop){
        cout<<"Введите ваше число: ";
        cin>>user_num;
        if (user_num>rand_num){
            cout<<"Ваше число больше загаданного "<<endl;
        }
        else if (user_num<rand_num){
            cout<<"Ваше число меньше загаданного"<<endl;
        }
        else if (user_num==rand_num){
            cout<<"Поздравляю вы угадали число "<<user_num<<endl;
            stop=true;
        }
    }
    return 0;
}