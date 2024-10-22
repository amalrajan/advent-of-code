#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// Function to parse input
pair<unordered_map<string, vector<string>>, string> parse_input() {
  ifstream input("input.txt");
  string line;
  vector<string> inputs;

  // Read input file line by line
  while (getline(input, line)) {
    inputs.push_back(line);
  }

  unordered_map<string, vector<string>> transformations;
  string molecule = inputs.back();

  for (const string &line : inputs) {
    if (line.empty()) continue;

    size_t pos = line.find("=>");
    if (pos != string::npos) {
      string from = line.substr(0, pos - 1);
      string to = line.substr(pos + 3);
      transformations[from].push_back(to);
    }
  }

  return {transformations, molecule};
}

// Function to solve the problem
int solve(unordered_map<string, vector<string>> &transformations,
          const string &target_molecule) {
  unordered_map<string, vector<string>> rev_transformations;

  for (const auto &entry : transformations) {
    for (const string &item : entry.second) {
      rev_transformations[item].push_back(entry.first);
    }
  }

  int max_key_len = 0;
  for (const auto &entry : rev_transformations) {
    max_key_len = max(max_key_len, (int)entry.first.size());
  }

  int ans = numeric_limits<int>::max();
  unordered_set<string> visited;

  int prev_length = target_molecule.length();

  // Backtrack function
  function<void(string, int)> backtrack = [&](const string &molecule,
                                              int steps) {
    if (molecule == "e") {
      ans = min(ans, steps);
      return;
    }

    if (molecule.size() <= 0 || molecule.find("e") != string::npos) {
      return;
    }

    if (molecule.length() < prev_length) {
      prev_length = molecule.length();
      cout << molecule << " " << steps << '\n';
    }

    visited.insert(molecule);

    for (size_t i = 0; i < molecule.size(); ++i) {
      for (int j = 0; j < max_key_len && i + j < molecule.size(); ++j) {
        string key = molecule.substr(i, j + 1);
        for (const string &repl_text : rev_transformations[key]) {
          string new_molecule =
              molecule.substr(0, i) + repl_text + molecule.substr(i + j + 1);
          if (visited.find(new_molecule) == visited.end()) {
            visited.insert(new_molecule);
            backtrack(new_molecule, steps + 1);
          }
        }
      }
    }
  };

  backtrack(target_molecule, 0);

  return ans;
}

int main() {
  auto [transformations, molecule] = parse_input();
  cout << solve(transformations, molecule) << endl;
  return 0;
}
