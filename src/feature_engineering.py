skills_vector = ['machine learning', 'python', 'java', 'hadoop', 'spark', 'data mining', 'r', 'c++', 'hive','pig', 'sql', 'natural language processing', 'ai', 'nosql', 'image processing', 'tableau',
                 'sas', 'matlab', 'embedded software', 'spss', 'oop', 'azure', 'javascript', 'sdlc', '.net',
                 'perl', 'rest', 'big data', 'jenkins', 'oracle', 'management experience', 's3', 'jira',
                 'json', 'shell scripting', 'test automation', 'clojure', 'data science', 'go', 'biotechnology',
                 'ci', 'project management', 'excel', 'microsoft office', 'docker', 'data analysis', 'postgresql',
                 'ruby', 'laboratory experience', 'kubernetes', 'microsoft powerpoint', 'program management',
                 'd3.js', 'git', 'data warehouse', 'html5', 'microsoft sql server', 'hbase', 'ansible',
                 'google cloud platform', 'unit testing', 'node.js', 'php', 'react', 'marketing', 'spring',
                 'maven', 'signal processing', 'power bi', 'mysql', 'scripting', 'svn', 'angular',
                 'time management', 'analysis skills', 'visual basic', 'kafka', 'molecular biology','dynamodb',
                 'system design', 'weka', 'leadership experience', 'sentiment analytics', 'mirosoft word', 'sap',
                 'software development', 'clinical research', 'mongodb', 'predictive analytics',
                 'statistical analytics', 'genetics', 'cloud computing', 'visual studio', 'cassandra',
                 'supply chain experience', 'erp systems', 'multi arm bandit', 'profit curves', 'tfidf',
                 'cosine similarity', 'trials', 'rnn', 'regression', 'random forest', 'recommendation',
                 'customer lifetime value', 'pricing optimization', 'marketing attribution', 'media mixing model',
                 'product ranking', 'inventory model', 'advanced degree', 'phd', 'ms', 'master''s', 'teradata', 'aws',
                 'mysql', 'sklearn', 'linear regression', 'neural network', 'keras', 'tensorflow', 'random forest',
                 'decision tree', 'boosting', 'gradient boosting', 'gradient descent', 'pandas', 'numpy', 'accuracy',
                 'cross validation', 'logistic regression', 'classification', 'roc curve', 'precision', 'recall',
                 'web scraping', 'aws', 'spark', 'pyspark', 'model testing', 'pytorch', 'scipy', 'big data', 'spark',
                 'hadoop', 'millions of rows', 'a/b testing', 'experimental design', 'data visualization', 'nlp',
                 'time series', 'recommender systems', 'mongodb', 'statistics', 'calculus', 'public speaking',
                 'linear algebra', 'bayesian', 'naive bayes', 'hadoop', 'scala', 'bernoulli', 'poisson',
                 'cross validation', 'distributed systems', 'matrix factorization', 'statistical analysis',
                 'modeling', 'confidence intervals', 'svm', 'ab testing', 'overfitting', 'underfitting',
                 'optimization', 'game theory', 'networking', 'html', 'flask','tensorflow', 'keras', 'data wrangler',
                 'doctorate', 'master''s', 'mathematics', 'bayesian', 'data visualization', 'optimization',
                 'communication', 'r', 'engineering', 'analyze', 'analytical', 'collaboration', 'team player',
                 'pandas', 'seaborn', 'matplotlib', 'ggplot', 'hadoop', 'mongodb', 'aws', 'keras', 'sql', 'python',
                 'power bi', 'problem solving', 'deep learning', 'sklearn', 'big data', 'numerical analysis' ]
my_stop_words=['collaboration', 'marketing', 'clinical research']
skeelz = set(skills_vector)-set(my_stop_words)

data_visualization_front_end_skills = ['ggplot',
    'power bi',
    'data visualization',
    'matplotlib',
    'tableau',
    'powerbi',
    'excel',
    'seaborn',
    'd3.js',
    'processing.js',
    'polymaps',
    'sigma js',
    'n3-charts',
    'chartist.js',
    'leaflet',
    'chart.js',
    'highcharts',
    'fusioncharts',
    'google charts',
    'NVD3',
    'Ember Charts',
    'Visual.ly',
    'Plotly',
    'Qlikview',
    'Datawrapper',
    'flask',
    'html5',
    'html',
    'angular',
    'react',
    'rest']
management_skills = ['project management',
     'agile', 'scrum', 'direct reports', 'communication',
     'jira', 'management experience', 'time management',
     'public speaking', 'leadership experience',
     'program management', 'team player', 'erp systems',
     'maven', 'sap', 'sdlc']
machine_learning = ['sklearn', 'decision trees',
    'random forests', 'random forest','neural networks',
    'keras', 'gradient boosting', 'deep learning',
    'naive bayes', 'ai', 'natural language processing',
    'selenium', 'nlp', 'svm', 'tensorflow', 'data mining',
    'decision tree', 'rnn', 'cnn', 'machine learning',
    'gradient descent', 'overfitting', 'underfitting',
    'neural network', 'recommender systems', 'tfidf',
    'pytorch', 'weka']
programming = ['c++', 'c#', 'python', 'java', 'javascript',
    'numpy', 'node.js', 'oop', 'pandas', 'r', 'perl', 'software engineering', 'scripting', 'visual basic', 'visual studio', 'web scraping', 'svn', 'embedded software', 'go',
    'git', 'php', 'test automation', 'ruby', '.net', 'unit testing', 'shell scripting', 'software development', 'jenkins', 'clojure', 'spring']
cloud_computing = ['aws', 's3', 'azure', 'google cloud',
    'bigtable', 'cloud computing', 'google cloud platform']
math_statistics = ['linear regression',
    'logistic regression', 'bayes', 'ab testing',
    'a/b testing', 'bayesian', 'bernoulli',
    'calculus', 'confidence intervals', 'cosine similarity',
    'cross validation', 'game theory', 'matrix factorization',
    'linear algebra', 'multi arm bandit', 'poisson',
    'optimization', 'statistical analysis',
    'statistical analytics', 'matlab', 'spss', 'mathematics',
    'experimental design', 'boosting', 'numerical analysis',
    'classification', 'scipy', 'regression',
    'predictive analytics', 'sas', 'pricing optimization',
    'time series', 'statistics']
education = ['bachelor''s', 'master''s', 'doctoral',
    'doctorate', 'ms', 'advanced degree', 'phd']
data_engineering = ['sql', 'etl', 'data warehousing',
    'data warehouse', 'distributed systems', 'dynamodb',
    'mongodb', 'nosql', 'oracle', 'json',
    'postgresql', 'pig', 'pyspark', 'scala', 'spark',
    'data wrangler', 'hive', 'hadoop','mysql', 'big data',
    'teradata', 'cassandra', 'networking', 'ansible', 'ci',
    'docker', 'kafka', 'hbase', 'kubernetes']
problem_solving = ['analysis skills', 'analytical',
    'analyze', 'system design', 'accuracy', 'data science',
    'model testing', 'modeling', 'precision', 'recall',
    'profit curve', 'roc curve', 'microsoft word',
    'mirosoft word', 'microsoft office',
    'microsoft powerpoint', 'microsoft sql server',
    'millions of rows', 'data analysis',
    'marketing attribution', 'problem solving',
    'recommendation', 'profit curves', 'sentiment analytics']
miscellaneous = ['genetics', 'biotechnology',
    'molecular biology', 'media mixing model',
    'inventory model', 'image processing',
    'signal processing', 'supply chain experience',
    'customer lifetime value', 'laboratory experience',
    'product ranking', 'trials', 'engineering']

def get_occupation_bool_index(occupation, cleaned_df):
    '''returns boolean indexes of the cleaned_df filtering out this specific occupation'''
    return (cleaned_df['job_title'].str.lower().str.find(occupation)>=0)
def exclude_blacklisted_occupations(blacklisted_occupations, cleaned_df):
    '''
    takes in a dataframe of cleaned job postings
    removes job postings that have occupations in a blacklist
    '''
    index = get_occupation_bool_index(blacklisted_occupations[0],cleaned_df)
    for occupation in blacklisted_occupations[1:]:
        index = (index)|(get_occupation_bool_index(occupation, cleaned_df))
    return cleaned_df[~index]
