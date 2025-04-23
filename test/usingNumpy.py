import numpy as np

# Job titles
job_titles = np.array(['Data Analyst', 'Data Scientist', 'Data Engineer', 'Machine Learning Engineer', 'AI Engineer'])

# Base salaries
base_salaries = np.array([60000, 80000, 75000, 90000, np.nan]) # Numpy nan (not a number) is a float datatype used for things with no data

# Bonus rates
bonus_rates = np.array([.05, .1, .08, .12, np.nan]) # Using nan and np.nan will allow the same calculations without the missing data to affect the other data

total_salaries = base_salaries * (1 + bonus_rates)
print(total_salaries) # salaries can still be seen even with a nan value
print(np.nanmean(total_salaries)) # the mean is still correctly calculated even with a nan value