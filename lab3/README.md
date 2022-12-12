The following readme is for Task 1 and Task 2. Below you can find the update for task 3 and 4.

Collaboration with Angelica Ferlin, Leonor Gomes and Karl Wennerström. 

Task 1 was solved by creating the optimal nim agent who uses the nim-sum and an XOR strategy to calculate the optimal move to perform at each turn. As the agent is optimal, it wins almost all of it's games. However, if two optimal agents play against eachother, it just depends on the structure of the board. If the nim-sum is at the start, the second agent wins, if the nim-sum is different from 0, the agent starting wins. 

In Task 2 i implemented some simple rules to use for the evolutionary strategies. These rules were the following:
Rule 1 - If there is only 1 row left, pick objects until there are only x elements left
Rule 2 - If there are 2 rows left and one row only has 1 element left, operate on the shorter/longer row and leave x elements behind in that row
Rule 3 - If there are 2 rows left and both rows have more than 1 element left, operate on the shorter/longer row and leave x elements behind in that row
Rule 4 - If there are more than 2 rows left, leave x elements on a random row

An individual then contains the parameters for each rule and a fitness. The fitness was calculated when letting the individual with the above rules play against external agents and store the number of wins. 
That is, let an individual play 10 rounds against an optimal agent, random agent and a silly agent. The number of wins against each agent are then stored in a tuple in the individual and kept as the fitness. 

The parents for the offspring are determined by a tournament where each parent is decided to be the one with the best fitness among 10 random individuals selected from the population. The crossover is to select a certain amount of the parameters for the rules from one parent and the rest from the other. A mutation is randomizing the number of elements left behind in the row. 

UPDATE

Readme file for Task 3 and Task 4. 

Collaboration with Angelica Ferlin, Leonor Gomes and the following online sources: [https://realpython.com/python-minimax-nim/], [https://andrewrowell.blog/2020/05/19/q-learning-nim-with-python/].

Task 3 was solved by using minmax to obtain the optimal solution. No limit on depth or generation was implemented on the search tree, however alpha-beta pruning was. In the end, the algorithm solves problems of depth no more than 3 very efficiently. Since a nim board of depth equal to 4 doesn't have an optimal solution in the beginning this one takes very long time to solve, since the algorithm even with alpha-beta pruning tests a bunch of solutions. And for boards of depth higher or equal to 5 this algorithm is unfeasible in its current implementation, it simply takes too long to calculate. 

Task 4 was solved using a RL agent for a board with 5 depth. The agent was trained for 1000 iterations against 3 opponents: a stupid one, a pure random one and an optimal one. The agent in the end was able to beat the stupid one 100% of the times, the random one ~70% of the time and the optimal one only a few procent 0-10%. A lot of focus was put on the exploration of the agent. Since the board has so many different configurations it's really important that the agent gets to play a lot of games in the different states to being able to update it's reward and thus policy. Since the game is deterministic the learning rate can be set high wich speeds this up. However, since there's only a reward at the end of the game and no continuous rewards throughout the game, this slows down the training process immensely. 
