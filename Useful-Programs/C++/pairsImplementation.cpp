#include<iostream>

using namespace std;

int main(){

    pair<int,int> p;
    p.first = 2;
    p.second = 3;

    cout<<"Pair First : "<<p.first<<endl;
    cout<<"Pair Second : "<<p.second<<endl;

    pair<int,int> p1 = make_pair(2,2);
    cout<<"Pair First : "<<p1.first;
    cout<<"Pair Second : "<<p1.second;    
    return 0;
}