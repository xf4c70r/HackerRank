#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n, m;
    cin>>n; 
    vector<int> g1; 
    for (int i = 1; i <= n; i++){
        cin>>m;
        g1.push_back(m);
    }
    sort(g1.begin(), g1.end());
    for (auto x : g1){
        cout<<x<<" ";
    }
    return 0;
}
