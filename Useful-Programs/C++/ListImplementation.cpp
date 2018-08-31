#include<bits/stdc++.h>

using namespace std;

int main(){

    list<int> l;
    
    // 4 3 2 1 0 0 1 2 3 4
    for(int i=0;i<5;i++){
        l.emplace_back(i);
        l.emplace_front(i);
    }

    for(int &x:l){
        cout<<x<<" ";
    }

    cout<<endl<<"--------------------"<<endl;

    // merge
    list<int> l1 = {1,2,3};
    list<int> l2 = {4,5,6};

    l1.merge(l2);

    for(int &x:l1){
        cout<<x<<" ";
    }

    cout<<endl<<"-----------------------"<<endl;

    // remove
    l1.remove_if([](int x){return x%2 == 0;});
    for(int &x:l1){
        cout<<x<<" ";
    }

    cout<<endl<<"--------------------------"<<endl;

    //unique
    l1 = {1,2,3,4,5,6,2,2,2,2,2};
    l1.unique();
    for(int &x:l1){
        cout<<x<<" ";
    }

    // iterator
    // advance is used to increment iterator 
    list<int>::iterator it = l1.begin();
    advance(it,3);

    //
    cout<<endl;
    cout<<"-----------------------------"<<endl;
    l1.pop_back();
    l1.pop_front();
    for(int &x:l1){
        cout<<x<<" ";
    }
        
    return 0;
}