#include <iostream>
#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
    ll time = 60808676;
    ll dist = 601116315591300;

    ll cnt = 0, dist_covered;

    for (ll a = 0; a <= time; a++)
    {

        dist_covered = a * (time - a);
        if (dist_covered > dist)
            cnt++;
    }

    cout << "Ans: " << cnt;

    return 0;
}