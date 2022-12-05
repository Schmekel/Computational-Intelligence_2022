The following readme is for Task 1 and Task 2. 

Task 1 was solved by creating the optimal nim agent who uses the nim-sum and an XOR strategy to calculate the optimal move to perform at each turn. As the agent is optimal, it wins almost all of it's games. However, if two optimal agents play against eachother, it just depends on the structure of the board. If the nim-sum is at the start, the second agent wins, if the nim-sum is different from 0, the agent starting wins. 

In Task 2 i implemented some simple rules to use for the evolutionary strategies. These rules were the following:
Rule 1 - If there is only 1 row left, pick objects until there are only x elements left
Rule 2 - If there are 2 rows left and one row only has 1 element left, operate on the shorter/longer row and leave x elements behind in that row
Rule 3 - If there are 2 rows left and both rows have more than 1 element left, operate on the shorter/longer row and leave x elements behind in that row
Rule 4 - If there are more than 2 rows left, leave x elements on a random row

An individual then contains the parameters for each rule and a fitness. The fitness was calculated when letting the individual with the above rules play against external agents and store the number of wins. 
That is, let an individual play 10 rounds against an optimal agent, random agent and a silly agent. The number of wins against each agent are then stored in a tuple in the individual and kept as the fitness. 

The parents for the offspring are determined by a tournament where each parent is decided to be the one with the best fitness among 10 random individuals selected from the population. The crossover is to select a certain amount of the parameters for the rules from one parent and the rest from the other. A mutation is randomizing the number of elements left behind in the row. 