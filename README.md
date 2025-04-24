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