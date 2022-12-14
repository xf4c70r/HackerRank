#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int q ;
    cin >> q;
    set <int> s;
    for(int i = 0; i < q; i++){
        int x, y;
        cin>>y;
        //cout<<y<<"\n";
        cin>>x;
        //cout<<x<<"\n";
        if(y == 1){
            //cout<<"One"<<"\n";
            s.insert(x);
        }
        else if(y == 2){
            //cout<<"Two"<<"\n";
            s.erase(x);
        }
        else{
            //cout<<"Three"<<"\n";
            set<int>::iterator itr=s.find(x);
            if (itr == s.end())
                cout<<"No"<<endl;
            else
                cout<<"Yes"<<endl;
        }
    }
    return 0;
}



