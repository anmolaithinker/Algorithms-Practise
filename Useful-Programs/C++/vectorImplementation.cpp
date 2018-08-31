#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char const *argv[])
{   
    vector<int> v;
    for(int i=0;i<10;i++){
        v.push_back(i);
    }

    cout<<endl<<" ------ "<<endl;

    for(auto itr = v.begin() ; itr!=v.end() ; itr++){
        cout<<(*itr)<<" ";
    }

    cout<<endl<<" -------- "<<endl;

    for(auto itr = v.rbegin() ; itr!=v.rend();itr++){
        cout<<(*itr)<<" ";
    }

    cout<<endl;

    cout<<"Number of elements inside vector : "<<v.size()<<endl;
    cout<<"Max number of elements a vector can hold : "<<v.max_size()<<endl;
    cout<<"Capacity of vector : "<<v.capacity()<<endl;   
    cout<<"Resizing the vector : (only contains 5 elements) : "<<endl;
    v.resize(5);
    cout<<"New Size : "<<v.size()<<endl;
    cout<<v.empty()<<endl;

    cout<<" -----------------------"<<endl;
    cout<<"Reference Operator indexing : 2 : "<<v[2]<<endl;
    cout<<"Using at function : "<<v.at(2)<<endl;
    cout<<"Front Func : "<<v.front()<<endl;
    cout<<"Back Func. : "<<v.back()<<endl;

    cout<<" -------------------------- "<<endl;

    v.push_back(10);
    cout<<v.back()<<endl;
    v.pop_back();
    cout<<v.back()<<endl;
    v.emplace_back(10);
    cout<<v.back()<<endl;

    // Erase
    //v.erase();

    //insert at position in vector
    //v.insert(v.begin(),5)



    return 0;
}
