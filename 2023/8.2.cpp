#include <bits/stdc++.h>
#include <iostream>
#include <sstream>

#define ll long long int

using namespace std;

vector<string> split(const string &input, char delimiter)
{
    vector<string> tokens;
    istringstream stream(input);
    string token;

    while (getline(stream, token, delimiter))
    {
        tokens.push_back(token);
    }

    return tokens;
}

string strip(const std::string &input)
{
    size_t first = input.find_first_not_of(" \t\n\r"); // Find first non-whitespace character
    size_t last = input.find_last_not_of(" \t\n\r");   // Find last non-whitespace character

    if (first == std::string::npos)
    {
        // The string is empty or contains only whitespace
        return "";
    }

    return input.substr(first, last - first + 1);
}

int main()
{
    ifstream inputFile("input.txt");
    if (!inputFile.is_open())
        return 1;

    // Read the file
    string directions;
    getline(inputFile, directions);
    // cout << directions << endl;

    unordered_map<string, pair<string, string>> resultMap;
    vector<string> nodes;

    string line;
    while (getline(inputFile, line))
    {
        if (line.empty())
            continue;
        vector<string> splitInputStrings = split(line, '=');
        string LHS = strip(splitInputStrings[0]);
        string RHS = strip(splitInputStrings[1]);
        RHS = RHS.substr(1, RHS.length() - 2);
        vector<string> RHSsplit = split(RHS, ',');

        for (size_t i = 0; i < RHSsplit.size(); i++)
        {
            RHSsplit[i] = strip(RHSsplit[i]);
        }

        resultMap[LHS] = make_pair(RHSsplit[0], RHSsplit[1]);

        if (LHS[LHS.length() - 1] == 'A')
        {
            nodes.push_back(LHS);
        }
    }

    // for (auto &x : resultMap)
    // {
    //     cout << x.first << " " << x.second.first << " " << x.second.second << endl;
    // }

    ll steps = 0, dirx = 0;
    size_t node_size = nodes.size();

    // This doesn't work, because brute force is too slow
    while (true)
    {
        // Check if all nodes have 'Z' as their last character
        bool allZ = true;
        for (auto &x : nodes)
        {
            if (x[x.length() - 1] != 'Z')
            {
                allZ = false;
                break;
            }
        }
        if (allZ)
            break;

        for (size_t i = 0; i < node_size; i++)
        {
            if (directions[dirx] == 'L')
                nodes[i] = resultMap[nodes[i]].first;
            else
                nodes[i] = resultMap[nodes[i]].second;
        }
        dirx = (dirx + 1) % directions.length();
        ++steps;

        // Just a progress indicator
        if (steps % 1000000 == 0)
            cout << steps / 1000000 << '\n';
    }
    cout << "ANS: " << steps << endl;

    return 0;
}