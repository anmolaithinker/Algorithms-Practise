#include<bits/stdc++.h>

using namespace std;

// Ascenfing Order
bool Comp(const vector<int> &v1,const vector<int> &v2){
    return v2.size()>v1.size();
}

int main(){

    vector<vector<int> > v{{1,2},
                            {3,4,5},
                            {6}};
    for(int i=0;i<v.size();i++){
        for(int j=0;j<v[i].size();j++){
            cout<<v[i][j]<<" ";
        }
        cout<<endl;
    }    

    sort(v.begin(),v.end(),Comp);                

    for(int i=0;i<v.size();i++){
        for(int j=0;j<v[i].size();j++){
            cout<<v[i][j]<<" ";
        }
        cout<<endl;
    }    

    return 0;
}