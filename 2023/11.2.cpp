#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <map>
#include <cmath>
#include <limits>

using namespace std;

ofstream outputFile;

void setOutputStream()
{
    outputFile.open("output.txt");
    if (!outputFile.is_open())
    {
        exit(EXIT_FAILURE);
    }

    cout.rdbuf(outputFile.rdbuf());
}

void displayGrid(vector<vector<char>> &grid)
{
    for (auto &row : grid)
    {
        for (auto &ch : row)
        {
            cout << ch;
        }
        cout << endl;
    }
}

vector<vector<char>> parseInput()
{
    ifstream inputFile("input.txt");
    if (!inputFile.is_open())
    {
        exit(EXIT_FAILURE);
    }

    string line;
    vector<vector<char>> galaxy;
    while (getline(inputFile, line))
    {
        vector<char> singleLine;
        for (auto &ch : line)
        {
            singleLine.push_back(ch);
        }

        galaxy.push_back(singleLine);
    }

    // displayGrid(galaxy);

    return galaxy;
}

vector<pair<int, int>> getAllPositions(vector<vector<char>> &galaxy)
{
    vector<pair<int, int>> positions;

    for (size_t i = 0; i < galaxy.size(); i++)
    {
        for (size_t j = 0; j < galaxy[0].size(); j++)
        {
            if (galaxy[i][j] == '#')
            {
                positions.push_back(make_pair(i, j));
            }
        }
    }

    return positions;
}

void expandGalaxy(vector<pair<int, int>> &positions, int k)
{
    // Expand rows
    vector<int> expandedRows = {};
    expandedRows.push_back(positions[0].first * k);
    for (size_t i = 1; i < positions.size(); i++)
    {
        int diff = positions[i].first - positions[i - 1].first - 1;
        if (diff < 0)
        {
            expandedRows.push_back(expandedRows.back());
        }
        else
        {
            expandedRows.push_back(expandedRows.back() + (diff * k) + 1);
        }
    }
    for (size_t i = 0; i < positions.size(); i++)
    {
        positions[i].first = expandedRows[i];
    }

    sort(positions.begin(), positions.end(),
         [](const auto &left, const auto &right)
         {
             return left.second < right.second;
         });

    // Expand columns
    vector<int> expandedCols = {};
    expandedCols.push_back(positions[0].second * k);
    for (size_t i = 1; i < positions.size(); i++)
    {
        int diff = positions[i].second - positions[i - 1].second - 1;
        if (diff < 0)
        {
            expandedCols.push_back(expandedCols.back());
        }
        else
        {
            expandedCols.push_back(expandedCols.back() + (diff * k) + 1);
        }
    }
    for (size_t i = 0; i < positions.size(); i++)
    {
        positions[i].second = expandedCols[i];
    }
}

long long int calculateTotalDistance(vector<pair<int, int>> &positions)
{
    long long int dist = 0;
    for (size_t i = 0; i < positions.size(); i++)
    {
        for (size_t j = i + 1; j < positions.size(); j++)
        {
            dist += abs(positions[i].first - positions[j].first) + abs(positions[i].second - positions[j].second);
        }
    }

    return dist;
}

int main()
{
    setOutputStream();

    vector<vector<char>> galaxy = parseInput();
    vector<pair<int, int>> positions = getAllPositions(galaxy);

    expandGalaxy(positions, 1000000);
    long long int ans = calculateTotalDistance(positions);

    cout << "Ans: " << ans << endl;

    return 0;
}