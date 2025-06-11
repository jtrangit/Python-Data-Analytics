# The Analysis

## 1. What are the most demanded skills for the top 3 most popular data roles?

To find the most demanded skills for the most popular data jobs
1. Filtered out the most popular positions
2. Get the top 5 skills for those roles

This highlights the most popular data jobs and their top skills, giving insight
to what skills are most important to consider depending on the role you are looking at

Here are the details from my Jupyter notebook:
[03_Skill_Demand.ipynb](Project/03_Skill_Demand.ipynb)

### Visualize Data
```
fig, ax = plt.subplots(len(job_titles), 1)

for i, job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc["job_title_short"] == job_title].head(5)
    sns.barplot(data=df_plot, x="skill_percent", y="job_skills", ax=ax[i], hue="skill_count", palette="dark:b_r")

plt.show()
```

### Results

![Visualization of Top Skills for Data Roles](https://raw.githubusercontent.com/jtrangit/Python-Data-Analytics/main/Project/images/skill_demand_all_data_roles.png)

### Insights
- Python and SQL are by far the most prevalent skills among the most common data roles
- Skills for Data Analyst roles are far less focused on programming, with python only making up about 27%, and much more focused on data management and analysis with
 SQL (51%) and excel(41%)
- SQL is common among all the data roles with the lowest percentage of SQL is 51% among Data Scientists and Data Analysts with the highest percentage of 68% in Data Engineers
- Among Data Scientists the most important skills are statistical programming with Python (72%) and R (44%), data management with SQL (51%), and data visualization/analytics with SAS (24%) and tableau(24%)

## 2. How are in-demand skills trending for Data Analysts?

### Visualize Data
```python

df_plot = df_DA_US_percent.iloc[:, :5]

sns.lineplot(data=df_plot, dashes=False, palette="tab10")
sns.set_theme(style="ticks")
sns.despine()

plt.title("Trending Top Skills for Data Analysts in the US")
plt.ylabel("Likelihood in Job Posting")
plt.xlabel("2023")
plt.legend().remove()

from matplotlib.ticker import PercentFormatter
ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals=0))

for i in range(5):
    plt.text(11.2, df_plot.iloc[-1, i], df_plot.columns[i])
```

### Results
![Trending Top Skills For Data Analysts in the US](https://raw.githubusercontent.com/jtrangit/Python-Data-Analytics/main/Project/images/skill_trend.png)

*Bar graph visualizing the trending top skills for data analysts in the US in 2023.*

### Insights:
- SQL is still the most in demand skill among Data roles, however it is showing signs of slowly decreasing in popularity.
- Excel mostly stayed the same being the 2nd most in demand skill, but there was a small increment of time where it dropped significantly (between August and October) but returned to a little below peak popularity by the end of the year.
- Python and Tableau both showed a stable demand and were very similar in demand, but by the end of the year Python surpassing Tableau just slightly.
- Power BI is the least in demand skill, however throughout the year it showed very stable demand with only minor and slight increases and decreases.

## 3. How well do Data Jobs and skills pay?

### Visualize Data

```python

sns.boxplot(data= df_US_top6, x= "salary_year_avg", y= "job_title_short", order= job_order)
sns.set_theme(style="ticks")

plt.title("Salary Distributions in the United States")
plt.xlabel("Yearly Salary (USD)")
plt.ylabel("")
plt.xlim(0, 600000)
ticks_x = plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K')
plt.gca().xaxis.set_major_formatter(ticks_x)
plt.show()

```

### Results

![Salary Distribution of Data Jobs in the US](https://raw.githubusercontent.com/jtrangit/Python-Data-Analytics/main/Project/images/data_salary.png)

### Insights

- The big 3 data roles from least paying to highest paying in order are: Data Analysts, Data Engineers, and Data Scientists.
- The pay for senior roles also follow the same trend with Data Scientists and Senior Data Scientists being the highest paid.
- Of all the data roles, the least paid is on average making around $90,000+ a year and the more specialized roles and senior roles are making over $100,000 a year.
- More senior and specialized roles like Data Engineers and Scientists also show a higher amount of outliers among the salary distributions, i.e: Data Scientists could potentially make close to $600,000 a year
- Data Analysts roles both senior and non senior jobs show the most consistent distribution and deviates less when it comes to outliers.
- Seniority increases the salary of the role considerably as well as increasing the potential range of outliers, meaning the more senior and specialized data roles could pay a lot more than the standard Analyst role.

### Highest Paid & Most Demanded Skills for Data Roles

### Visualize Data

```python

fig, ax = plt.subplots(2, 1)  

# Top 10 Highest Paid Skills for Data Analysts
sns.barplot(data=df_DA_top_pay, x='median', y=df_DA_top_pay.index, hue='median', ax=ax[0], palette='dark:b_r')
ax[0].legend().remove()
# original code:
# df_DA_top_pay[::-1].plot(kind='barh', y='median', ax=ax[0], legend=False) 
ax[0].set_title('Highest Paid Skills for Data Analysts in the US')
ax[0].set_ylabel('')
ax[0].set_xlabel('')
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x/1000)}K'))


# Top 10 Most In-Demand Skills for Data Analysts')
sns.barplot(data=df_DA_skills, x='median', y=df_DA_skills.index, hue='median', ax=ax[1], palette='light:b')
ax[1].legend().remove()
# original code:
# df_DA_skills[::-1].plot(kind='barh', y='median', ax=ax[1], legend=False)
ax[1].set_title('Most In-Demand Skills for Data Analysts in the US')
ax[1].set_ylabel('')
ax[1].set_xlabel('Median Salary (USD)')
ax[1].set_xlim(ax[0].get_xlim())  # Set the same x-axis limits as the first plot
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${int(x/1000)}K'))

sns.set_theme(style='ticks')
plt.tight_layout()
plt.show()

```

### Results

![Highest Paid Skills & Most in Demand Skills for Data Analysts](https://raw.githubusercontent.com/jtrangit/Python-Data-Analytics/main/Project/images/highest_paid_and_demanded_skills_data.png)

### Insights

- The highest paid skills for Data Analysts are not the most in demand skills, these skills and technologies have a salary of over $145,000 a year.
- These skills are hyper specialized as these are outliers, for each these skills there are less than 5 jobs that include these skills.
- Meanwhile the most in demand skills have jobs that pay around $80,000-$100,000 a year.
- These high demand skills are the fundamental skills for Data Roles. Data roles median salary is likely to increase depending on seniority and any new and specialized skills/technologies which is likely shown in the highest paid skills.

## 4. What are the most optimal skills to learn for Data Roles

### Visualize Data

```python

from adjustText import adjust_text

sns.scatterplot(
    data= df_skills_tech,
    x='skill_percent',
    y='median_salary',
    hue='technology'
)

sns.despine()
sns.set_theme(style='ticks')

# Prepare texts for adjustText
texts = []
for i, txt in enumerate(df_DA_skills_high_demand.index):
    texts.append(plt.text(df_DA_skills_high_demand['skill_percent'].iloc[i], df_DA_skills_high_demand['median_salary'].iloc[i], txt))

# Adjust text to avoid overlap
adjust_text(texts, expand=(2, 2), arrowprops=dict(arrowstyle='->', color='gray'))

# Set axis labels, title, and legend
plt.xlabel('Percent of Data Analyst Jobs')
plt.ylabel('Median Yearly Salary')
plt.title('Most Optimal Skills for Data Analysts in the US')
plt.legend(title='Technology')

from matplotlib.ticker import PercentFormatter
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, pos: f'${int(y/1000)}K'))
ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))

# Adjust layout and display plot 
plt.tight_layout()
plt.show()


```

### Results

![Most Optimal Skills for Data Roles](https://raw.githubusercontent.com/jtrangit/Python-Data-Analytics/main/Project/images/optimal_skills.png)

### Insights

- The most in demand skill is SQL, shows up in almost 60% of job postings. While it is the most in demand skill, it's pay is about middle of the pack compared to the pay of other skills.
- Programming skills and Data Visualization/Analyst tools make up the top 50% of the median yearly salary ($90,000 to $98,000).
- Non programming and analyst tools (powerpoint, excel, word) make up the least in demand skills (exception being excel), while also being the least paid (around $81,000 to $85,000)
- The most in demand skills are both programming skills and analyst tools (python, sql, tableau, and excel)
- The most paid skills are Oracle and Python both making around $95,000-$97,000. While python is a highly sought after skill, Oracle is not (making up <5% of job postings). Meaning, Oracle being a cloud technology is a highly specialized skill with low demand but for high paying data roles.
- The most optimal skills to pursue would be Programming skills, analyst tools, and then maybe cloud technologies. Programming skills and analyst tools make up the bulk of most Data Roles, then adding a specialized skill like Oracle would qualify you for a specialized role with a higher pay.