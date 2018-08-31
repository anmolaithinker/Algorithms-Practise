#include<bits/stdc++.h>
using namespace std;

int main(){

    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);

    for(int &x:q){
        cout<<x<<" ";
    }

    cout<<endl<<" ---------------------- "<<endl;

    q.pop();
    for(int &x:q){
        cout<<x<<" ";
    }
    
    return 0;
}