#include<bits/stdc++.h>
using namespace std;

void showD(deque<int> d){
    for(int &x:d){
        cout<<x<<" ";
    }
}

int main(){

    deque<int> d;
    d.push_back(10);
    d.push_front(20);
    d.push_back(30);
    d.push_front(40);

    showD(d);
    cout<<endl<<"-------------------"<<endl;

    d.pop_front();
    d.pop_back();
    cout<<" --------------------------- "<<endl;
    showD(d);

    // other func are same as vector


    return 0;
}