#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include<string>
#include<cstdlib>
#include<queue>

//THIS SOLUTION WAS GIVEN IN C++, I AM COPYING HERE TO UNDERSTAND

using namespace std;

int main()
{
    #define int long long
    int n,k;
    cin>>n>>k;
    priority_queue<int, std::vector<int>, std::greater<int> > pq;
    //adding from input to pq
    for(int i=0;i<n;i++)
    {
        int val;
        cin>>val;
        pq.push(val);
    }

    int count=0;
    bool ans=true;
    while(1) {
        //if queue is empty, no solution
        if(pq.empty()) {
            ans=false;
            break;
        }

        //get min value, if its >= k we have a solution
        int a1=pq.top();
        pq.pop();
        if(a1>=k) {
            break;
        }

        //if queue is now empty, return
        if(pq.empty()) {
            if(a1<k)
            {
                ans=false;
            }
            break;
        }
        
        //get second min value from queue
        int a2=pq.top();
        pq.pop();

        //get the new cookie and push that
        int nv=a1+2*a2;
        count++;
        pq.push(nv);

    }

    //return ans
    if(ans)
        cout<<count;
    else
        cout<<"-1";
    cout<<endl;
}

//my solution is the same logic as this, i just do not use a min queue
//i tried to sort originally but did not see the .sort() as an option