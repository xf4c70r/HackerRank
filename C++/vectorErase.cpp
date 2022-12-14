#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, m, o, p, q;
    cin>>n; 
    vector<int> g1; 
    for (int i = 1; i <= n; i++){
        cin>>m;
        g1.push_back(m);
    }
    cin>>o;
    g1.erase(g1.begin() + o - 1);
    cin>>p>>q;
    g1.erase(g1.begin() + p - 1, g1.begin() + q - 1);
    cout<<g1.size()<<"\n";
    for (auto x : g1){
        cout<<x<<" ";
        
    } 
    return 0;
}
