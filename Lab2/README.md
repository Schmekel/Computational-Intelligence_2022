This code was written by Mathias Schmekel in collaboration with Angelica Ferlin, Karl Wennerström and Leonor Gomes. Furthermore, the code posted in the lab description was copied and used.

For mu = 30 and lambda = 20
My results are the following:
N = 5 -> w = 5

N = 10 -> w = 10

N = 20 -> 26

N = 100 -> 200

N = 500 -> 1612

N = 1000 -> 3695

The result presented above is the first individual in the population list after an execution, that is population[0].

It was hypothesized that the solution would improve if the individual with best fintess was stored throughout the execution of the program and presented as the final solution in the end. Below are the results

For mu = 30 and lambda = 20
My results are the following:
N = 5 -> w = 5

N = 10 -> w = 10

N = 20 -> 29 (Missing 3 numbers)

N = 100 -> 214 (Missing 2 numbers)

N = 500 -> 1677 (Missing 5 numbers)

N = 1000 -> 3718 (Missing 4 numbers)

The results do not support the hypothesis. Furthermore, the results are missing some numbers required in the sequence making these invalid. It was determined it that this is due to the fintess function being inaccurate for these instances, as the term -1000*(missing numbers) seems to be forgotten for the solution. I was however unable to determine why within the scope of the deadline. 

In summary, the first solution manages to solve the problem, the second did not. 
