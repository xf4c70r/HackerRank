#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int q ;
    cin >> q;
    map<string,int>m;
    for(int i = 0; i < q; i++){
        int type, x;
        string y;
        cin>>type;
        cin>>y;
        if(type == 1){
            cin>>x;
            m[y] += x;
        }
        else if(type == 2){
            m.erase(y);
        }
        else{
            map<string,int>::iterator itr = m.find(y);
            if (itr != m.end()){
                cout<<m.find(y)->second<<endl;
            }
            else{
                cout<<"0"<<endl;
            }
        }
    }
    return 0;
}
