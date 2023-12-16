#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
#include <map>
#include <tuple>
#include <unordered_set>
#include <algorithm>

using namespace std;

ofstream outputFile;
const string inputFileName = "input.txt";
const string outputFileName = "output.txt";

struct TupleHashFunction
{
    size_t operator()(const tuple<int, int, int, int> &x) const
    {
        return get<0>(x) ^ get<1>(x) ^ get<2>(x) ^ get<3>(x);
    }
};

void setOutputStream()
{
    outputFile.open(outputFileName);
    if (!outputFile.is_open())
        exit(EXIT_FAILURE);

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
    ifstream inputFile(inputFileName);
    if (!inputFile.is_open())
    {
        exit(EXIT_FAILURE);
    }

    string line;
    vector<vector<char>> grid;
    while (getline(inputFile, line))
    {
        vector<char> singleLine;
        for (auto &ch : line)
        {
            singleLine.push_back(ch);
        }

        grid.push_back(singleLine);
    }

    return grid;
}

vector<vector<char>> simulateBeamPath(vector<vector<char>> &grid, int start_x, int start_y, int dx, int dy)
{
    const size_t M = grid.size(), N = grid[0].size();

    map<char, pair<int, int>> coordinates = {
        {'L', {0, -1}},
        {'R', {0, 1}},
        {'T', {-1, 0}},
        {'B', {1, 0}}};

    map<pair<int, int>, map<char, vector<char>>> directionMap = {
        {{0, -1}, {{'-', {'L'}}, {'|', {'B', 'T'}}, {'/', {'B'}}, {'\\', {'T'}}, {'.', {'L'}}}},
        {{0, 1}, {{'-', {'R'}}, {'|', {'B', 'T'}}, {'/', {'T'}}, {'\\', {'B'}}, {'.', {'R'}}}},
        {{-1, 0}, {{'-', {'L', 'R'}}, {'|', {'T'}}, {'/', {'R'}}, {'\\', {'L'}}, {'.', {'T'}}}},
        {{1, 0}, {{'-', {'L', 'R'}}, {'|', {'B'}}, {'/', {'L'}}, {'\\', {'R'}}, {'.', {'B'}}}}};

    vector<vector<char>> track(M, vector<char>(N, '.'));

    stack<tuple<int, int, int, int>> dfsStack;
    // start_x, start_y, dx, dy
    dfsStack.push(make_tuple(start_x, start_y, dx, dy));
    unordered_set<tuple<int, int, int, int>, TupleHashFunction> visited;

    while (!dfsStack.empty())
    {
        int x, y, dx, dy;
        tuple<int, int, int, int> front = dfsStack.top();
        tie(x, y, dx, dy) = front;
        dfsStack.pop();

        if (visited.find(front) != visited.end())
        {
            continue;
        }
        visited.insert(front);
        track[x][y] = '#';

        char curr = grid[x][y];
        for (auto &ch : directionMap[make_pair(dx, dy)][curr])
        {
            int ndx, ndy;
            tie(ndx, ndy) = coordinates[ch];
            if (0 <= x + ndx && x + ndx < M && 0 <= y + ndy && y + ndy < N)
            {
                dfsStack.push(make_tuple(x + ndx, y + ndy, ndx, ndy));
            }
        }
    }

    return track;
}

int countEnergizedTiles(vector<vector<char>> &track)
{
    int cnt = 0;
    for (auto &row : track)
    {
        cnt += count(row.begin(), row.end(), '#');
    }

    return cnt;
}

int findMaxPossibleEnergizedTiles(vector<vector<char>> &grid)
{
    int maxTiles = 0;
    vector<vector<char>> tempTrack;

    // Check left and right
    for (size_t i = 0; i < grid.size(); i++)
    {
        tempTrack = simulateBeamPath(grid, i, 0, 0, 1);
        maxTiles = max(maxTiles, countEnergizedTiles(tempTrack));

        tempTrack = simulateBeamPath(grid, i, grid.size() - 1, 0, -1);
        maxTiles = max(maxTiles, countEnergizedTiles(tempTrack));
    }

    // Check top and bottom
    for (size_t j = 0; j < grid[0].size(); j++)
    {
        tempTrack = simulateBeamPath(grid, 0, j, 1, 0);
        maxTiles = max(maxTiles, countEnergizedTiles(tempTrack));

        tempTrack = simulateBeamPath(grid, grid[0].size() - 1, j, -1, 0);
        maxTiles = max(maxTiles, countEnergizedTiles(tempTrack));
    }

    return maxTiles;
}

int main()
{
    setOutputStream();

    vector<vector<char>> grid = parseInput();
    // displayGrid(grid);

    cout << "Ans: " << findMaxPossibleEnergizedTiles(grid) << endl;

    return 0;
}