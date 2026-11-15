int main(){
    int n;
    cout<<"Введите кол-во строк: ";
    cin>>n;
    string *words = new string[n];
    string word;
    string max_word=" ";
    bool swapped=false;
    for (int i=0;i<n;i++){
        cout<<"Введите "<<i<<" строку: ";
        cin>>word;
        words[i]=word;
        if (words[i].size()>max_word.size()){
            max_word=words[i];
        }
        cout<<endl;
    }
    for (int i=0;i<n-1;i++){
        swapped=false;
        for (int j=0;j<n-1-i;j++){
            if (words[j]>words[j+1]){ 
                swap(words[j],words[j+1]);
                swapped=true;
            }
        if (swapped==false){
            break;
        }
        }
    }
    cout<<"Отсортированный массив: "<<endl;
    for (int i=0;i<n;i++){
        cout<<words[i]<<" ";
    }
    cout<<endl;
    cout<<"Самое длинное слово: "<<max_word<<endl;
    return 0;
}
