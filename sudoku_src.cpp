#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <vector>
#include <cstring>
#include <functional>

using namespace std;

vector<vector<char>> fill_solution(vector<vector<char>> &board)
{
    bool row[9][9];
    bool col[9][9];
    bool block[3][3][9];
    bool valid = false;
    memset(row, false, sizeof(row));
    memset(col, false, sizeof(col));
    memset(block, false, sizeof(block));

    vector<pair<int, int>> space;
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (board[i][j] == '.')
            {
                space.emplace_back(i, j);
            }
            else
            {
                int k = board[i][j] - '0';
                row[i][k - 1] = true;
                col[j][k - 1] = true;
                block[i / 3][j / 3][k - 1] = true;
            }
        }
    }

    function<void(int)> dfs;
    dfs = [&](int idx) -> void
    {
        if (idx == space.size())
        {
            valid = true;
            return;
        }
        int i = space[idx].first;
        int j = space[idx].second;
        for (int digit = 0; digit < 9 && !valid; digit++)
        {
            if (!row[i][digit] && !col[j][digit] && !block[i / 3][j / 3][digit])
            {
                row[i][digit] = true;
                col[j][digit] = true;
                block[i / 3][j / 3][digit] = true;
                board[i][j] = digit + 1 + '0';
                dfs(idx + 1);
                row[i][digit] = false;
                col[j][digit] = false;
                block[i / 3][j / 3][digit] = false;
            }
        }
    };
    dfs(0);
    return board;
}

void show(vector<vector<char>> board)
{
    for (auto x : board)
    {
        for (char i : x)
        {
            cout << i << ' ';
        }
        cout << endl;
    }
}

PYBIND11_MODULE(sudoku, m){
    m.def("fill_solution", &fill_solution, "fill the sudoku");
}