import random
import statistics
import numpy as np

#Create list of 1 million random salaries (between 50000 to 100000)
salary_list = [random.randint(50000, 100000) for _ in range(1_000_000)]

print(statistics.mean(salary_list)) # statistics is significantly slower than numpy (a couple seconds)

print(np.mean(salary_list)) # numpy is faster (less than a second)