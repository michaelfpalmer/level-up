# level-up
## BusinessUnderstanding
As a job hunter, I want to know what are some skills to develop in order to level-up in my career. 

Based on a collection of existing skills, I will find the current market value of the skills, and the incremental value of adding new skills.

In addition, I will explore many aspects of job hunting. For example, what words should job seekers pay the most attention to in the hunt? Which words matter the least. Are there things that exist in every job description that are essentially meaningless, such as, "Excellent written and oral communication skills"? While these may be important in every job, they don't distinguish the particular job from other jobs.
## DataUnderstanding
Scraped all salaried job postings for Seattle from Glassdoor. Output to csv. Imported into a pandas dataframe. Initially had about 600 salaried job postings for the Seattle area job market. Now have about a dozen job markets for data scientists.
## DataPreparation
Some basic string searching for salaried information. In addition I vectorized data into a bag of words model. Additionally, I collected some data science buzzwords and did counts of buzzwords as a feature. Next, I bucketed these buzzwords to see if there are larger trends.
## Modeling
Some Exploratory Data Analysis with basic quantiling. Compare top paying jobs from bottom paying jobs. These visualizations give some practical and actionable insight into what is important in the Seattle Data Science job market.

We can apply some machine learning models to fit a regression on salary. One approach to give a recommendation is do a for loop. This runs into some issues with data sparsity and overfitting. We can get some recommendations that fit our training data well, but there's just so many combinations of skills out in the wild, we quickly get down to only a handful of relevant job postings after picking 2-3 skills.
## Evaluation
I evaluated my model using RMSE. This is quite similar to standard deviation and gives some interpretable units that roughly say "I'll be off by about $27,000".
## Deployment
Future state, with more robust recommendations, I'd like to build a web application.
