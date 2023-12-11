#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <queue>
#include <utility>
#include <tuple>
#include <unordered_map>
#include <algorithm>

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
        exit(EXIT_FAILURE);

    string line;
    vector<vector<char>> pipes;
    while (getline(inputFile, line))
    {
        vector<char> singleLine;
        for (auto &ch : line)
            singleLine.push_back(ch);

        pipes.push_back(singleLine);
    }

    // displayGrid(pipes);

    return pipes;
}

pair<int, int> getSourcePos(vector<vector<char>> &grid)
{
    for (size_t i = 0; i < grid.size(); i++)
    {
        for (size_t j = 0; j < grid[0].size(); j++)
        {
            if (grid[i][j] == 'S')
            {
                return make_pair(i, j);
            }
        }
    }

    return make_pair(-1, -1);
}

void fixSourceChar(vector<vector<char>> &grid, int sx, int sy)
{
    int m = grid.size();
    int n = grid[0].size();

    map<vector<int>, char> positions = {
        {{1, 0, 1, 0}, 'J'},
        {{1, 1, 0, 0}, '-'},
        {{1, 0, 0, 1}, '7'},
        {{0, 1, 0, 1}, 'F'},
        {{0, 1, 1, 0}, 'L'},
        {{0, 0, 1, 1}, '|'},
    };

    int left = 0;
    int right = 0;
    int top = 0;
    int bottom = 0;

    if (sy - 1 >= 0 && (grid[sx][sy - 1] == '-' || grid[sx][sy - 1] == 'L' || grid[sx][sy - 1] == 'F'))
    {
        left = 1;
    }
    if (sy + 1 < n && (grid[sx][sy + 1] == '-' || grid[sx][sy + 1] == 'J' || grid[sx][sy + 1] == '7'))
    {
        right = 1;
    }
    if (sx - 1 >= 0 && (grid[sx - 1][sy] == '|' || grid[sx - 1][sy] == '7' || grid[sx - 1][sy] == 'F'))
    {
        top = 1;
    }
    if (sx + 1 < m && (grid[sx + 1][sy] == '|' || grid[sx + 1][sy] == 'L' || grid[sx + 1][sy] == 'J'))
    {
        bottom = 1;
    }

    vector<int> positionsKey = {left, right, top, bottom};

    // for (const auto &element : positionsKey)
    // {
    //     std::cout << element << " ";
    // }

    grid[sx][sy] = positions[positionsKey];
}

int findLongestLoopLength(vector<vector<char>> &grid, vector<vector<int>> &distanceGrid, int sx, int sy)
{
    int m = grid.size();
    int n = grid[0].size();

    unordered_map<char, vector<pair<int, int>>> directions = {
        {'|', {{-1, 0}, {1, 0}}},
        {'-', {{0, -1}, {0, 1}}},
        {'L', {{0, 1}, {-1, 0}}},
        {'J', {{0, -1}, {-1, 0}}},
        {'7', {{0, -1}, {1, 0}}},
        {'F', {{1, 0}, {0, 1}}},
        {'S', {{0, 1}, {1, 0}, {-1, 0}, {0, -1}}}};

    queue<tuple<int, int, int>> que;

    que.push(make_tuple(sx, sy, 0));
    tuple<int, int, int> front;

    while (!que.empty())
    {
        front = que.front();
        que.pop();
        int x = get<0>(front), y = get<1>(front), steps = get<2>(front);

        if (distanceGrid[x][y] != -1)
        {
            continue;
        }
        distanceGrid[x][y] = steps;

        for (auto &pr : directions[grid[x][y]])
        {
            // cout << pr.first << " " << pr.second << endl;
            int dx = pr.first, dy = pr.second;
            int next_x = x + dx, next_y = y + dy;

            if (0 <= next_x && next_x < m && 0 <= next_y && next_y < n && distanceGrid[next_x][next_y] == -1)
            {
                que.push(make_tuple(next_x, next_y, steps + 1));
            }
        }
    }

    int farthest = 0;
    for (auto &row : distanceGrid)
    {
        auto maxInRow = max_element(row.begin(), row.end());
        farthest = max(farthest, static_cast<int>(*maxInRow));
    }

    return farthest;
}

void cleanPipes(vector<vector<char>> &pipes, vector<vector<int>> &distanceGrid)
{
    for (size_t i = 0; i < distanceGrid.size(); i++)
    {
        for (size_t j = 0; j < distanceGrid[i].size(); j++)
        {
            if (distanceGrid[i][j] == -1)
            {
                pipes[i][j] = '.';
            }
        }
    }
}

int rayCastArea(vector<vector<char>> &pipes)
{
    long int area = 0;

    for (size_t i = 0; i < pipes.size(); i++)
    {
        for (size_t j = 0; j < pipes[i].size(); j++)
        {
            // J, F, L, 7, | count
            int cnt[5] = {0};

            if (pipes[i][j] == '.')
            {
                for (size_t k = j + 1; k < pipes[i].size(); k++)
                {
                    if (pipes[i][k] == 'J')
                    {
                        ++cnt[0];
                    }
                    else if (pipes[i][k] == 'F')
                    {
                        ++cnt[1];
                    }
                    else if (pipes[i][k] == 'L')
                    {
                        ++cnt[2];
                    }
                    else if (pipes[i][k] == '7')
                    {
                        ++cnt[3];
                    }
                    else if (pipes[i][k] == '|')
                    {
                        ++cnt[4];
                    }
                }
                int intersections = cnt[4] + min(cnt[0], cnt[1]) + min(cnt[2], cnt[3]);
                if (intersections % 2)
                {
                    ++area;
                }
            }
        }
    }

    return area;
}

int main()
{
    setOutputStream();
    vector<vector<char>> pipes = parseInput();

    // displayGrid(pipes);

    pair<int, int> sourcePos = getSourcePos(pipes);
    int sx = sourcePos.first, sy = sourcePos.second;

    // cout << sx << " " << sy << endl;

    fixSourceChar(pipes, sx, sy);

    // displayGrid(pipes);

    int longestLoopLength = 0;
    vector<pair<int, int>> loopPositions;

    vector<vector<int>> distanceGrid(pipes.size(), vector<int>(pipes[0].size(), -1));
    int loop_length = findLongestLoopLength(pipes, distanceGrid, sx, sy);

    cout << "Loop length: " << loop_length << endl;

    cleanPipes(pipes, distanceGrid);
    // displayGrid(pipes);

    long int area = rayCastArea(pipes);
    cout << "Area: " << area << endl;

    return 0;
}