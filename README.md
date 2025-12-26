# Sports Reference Engineering Prompt
Based on the data example given in the prompt, I treated the team win–loss records as a matrix, where each row represents a team and each column represents that team’s record against another team. Using a nested loop, the outer loop selects the current team , while the inner loop iterates over all opponents. If the teams from the outer and inner loop are the same, "--" is inserted to mimic the table example. When the teams are not the same, the number of wins against the opposing team is pulled from the data and added to the row.


