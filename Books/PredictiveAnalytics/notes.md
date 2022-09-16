# Predictive Analytics: Data Mining, Machine Learning and Data Science for Practitioners, 2nd Edition
By [Dursun Delen](https://learning.oreilly.com/beta-search/?q=author%3A%22Dursun%20Delen%22&type=*&order_by=relevance)
[O'Reilly page](https://learning.oreilly.com/library/view/predictive-analytics-data/9780135946527/)

## Forward

- [With business analytics,] the goal is always the same: creating actionable insight from large and feature-rich data.
- Predictive analytics, which is the main topic of this book, comes after descriptive analytics and before prescriptive analytics. 
- Organizations usually start with descriptive analytics, then move into predictive analytics, and finally reach prescriptive analytics.
- Hierarchical nature of the term business analytics - descriptive, predictive, and prescriptive.
- Firms commonly apply analytics to business data to describe, predict, and optimize their business opportunities and maximize their performance. 
- Analytics (or perhaps more appropriately, data analytics) can simply be defined as the discovery of meaningful patterns‚ new and novel information and knowledge in data.
- With business analytics, firms can utilize data to understand what happened, foresee what will happen, and implement what should happen.
- Business analytics in general, and predictive analytics specifically, is all about foreseeing the future and making smarter and faster business decisions.

## Ch1: Introduction to Analytics

- Effectiveness of business analytics systems, no matter the level in the analytics hierarchy, depends largely on the quality and quantity of the data.
- Figure 1.4 provides a tabular representation of the three hierarchical levels of analytics, along with the questions answered and techniques used at each level. 
- If what is being predicted is a categorical variable, the act of prediction is called classification; otherwise, it is called regression. If the predicted variable is time dependent, the prediction process is often called time-series forecasting.
- Prediction essentially is the process of making intelligent/scientific estimates about the future values of some variables, such as customer demand, interest rates, and stock market movements.
- Descriptive analytics is also called business intelligence (BI), and predictive and prescriptive analytics are collectively called advanced analytics.
- Moving from one level to the next essentially means that the maturity at one level is completed and the next level is being widely exploited. Figure 1.3 provides a graphical depiction of the simple taxonomy developed by INFORMS and widely adopted by most industry leaders as well as academic institutions.
- The Capgemini study produced a concise definition of analytics: ‚ÄúAnalytics facilitates realization of business objectives through reporting of data to analyze trends, creating predictive models for forecasting and optimizing business processes for enhanced performance.
- Industry experts and leading consulting companies are projecting that analytics will grow faster than any other business segments in upcoming years; they have also named analytics (and data science) as one of the top business trends of this decade.
- In the 2000s the DW-driven decision support systems began to be called business intelligence systems.
- In the 1990s, the need for more versatile reporting led to the development of executive information systems (decision support systems designed and developed specifically for executives and their decision-making needs). 
- In the 1980s, these systems were integrated as enterprise-level information systems that we now commonly call ERP systems.
- During the early days of analytics, prior to the 1970s, data was often obtained from the domain experts using manual processes (i.e., interviews and surveys) to build mathematical or knowledge-based models to solve constraint optimization problems.
- It's possible to find references to corporate analytics as far back as the 1940s, during the World War II era, when more effective methods were needed to maximize output with limited resources.
Data mining is the process of discovering new knowledge in the forms of patterns and relationships in large data sets. The goal of analytics is to convert data/facts into actionable insight, and data mining is the key enabler of that goal.
- Analytics, on the other hand, encompasses a variety of methods, technologies, and associated tools for creating new knowledge/insight to solve complex problems and make better decisions more quickly.

## Ch2: Introduction to Predictive Analytics and Data Mining

- The main difference between commercial tools, such as Enterprise Miner, IBM SPSS Modeler, and Statistica, and free tools, such as Weka, RapidMiner, and KNIME, is often the computational efficiency.
- Two techniques often associated with data mining are visualization and time-series forecasting.
- Cluster analysis is also used to identify natural groupings of events or objects so that a common set of characteristics of these groups can be identified to describe them.
- Cluster analysis is a means of identifying classes of items so that items in a cluster have more in common with each other than with items in other clusters.
- Clustering techniques include optimization. The goal of clustering is to create groups so that the members within each group have maximum similarity and the members across groups have minimum similarity. 
- Clustering involves partitioning a collection of things (e.g., objects, events, etc., presented in a structured data set) into segments (or natural groupings) whose members share similar characteristics. 
- Two commonly used derivatives of association rule mining are link analysis and sequence mining.
associations‚Äîwhich are commonly called association rules in data mining
- A related category of classification tools is rule induction.
- Decision trees classify data into a finite number of classes, based on the values of the input variables.
- Common classification tools include neural networks and decision trees (from machine learning), logistic regression and discriminant analysis (from traditional statistics), and emerging tools such as rough sets, support vector machines, and genetic algorithms. 
- Classification, or supervised induction, is perhaps the most common of all data mining tasks. The objective of classification is to analyze the historical data stored in a database and automatically generate a model that can predict future behavior.
- In data mining terminology, prediction and forecasting are used synonymously, and the term prediction is used as the common representation of the act.
- Prediction is commonly used to indicate telling about the future.
- Figure 2.3 shows a simple taxonomy for data mining tasks, along with the learning methods and popular algorithms for each of the data mining tasks.
- Data mining is one of the most important enablers of data analytics in general and predictive analytics in specific.

## Ch3: Standardized Processes for Predictive Analytics

- The acronym SEMMA stands for Sample, Explore, Modify, Model, Assess.
- SEMMA, primarily developed by the SAS Institute.
- Another standardized data mining processes‚Äîarguably the most popular one‚Äîis called Cross-Industry Standard Process for Data Mining (CRISP-DM).
- One of the earliest and perhaps the first data mining process was called with the name of knowledge discovery in databases (KDD) methodology.

## Ch4: Data and Methods for Predictive Analytics

- Cluster analysis involves grouping a set of records (i.e., samples or objects) in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups (or clusters).
- In classification problems, the primary source for all accuracy estimation metrics is a confusion matrix, also called a classification matrix or a contingency table.
- Classification is perhaps the most commonly used predictive analytics and data mining method for real-world problems.
- Based on the variable we are predicting, the method of prediction can be labeled as classification (if we are predicting a discrete outcome), regression (if we are predicting a numeric value), or time-series forecasting (if we are predicting the future projection of a time-dependent value series). The underlying assumption is that what we already know about the past.
- Business planning and problem solving rely heavily on the estimation of the future event and occurrences.
few high-level data mining tasks. Depending on the need and the nature of the problem, the data mining task can be classified as prediction (either classification or regression), association, or clustering.
- The final phase of data preprocessing is data reduction.
- In the third phase of data preprocessing, the data is transformed for better processing.
- In the second phase of data preprocessing, known as data scrubbing.
- In the first phase of data preprocessing, the relevant data is collected from the identified sources
diligent effort is necessary to clean and transform the data into a form that can be mined while making sure that the preprocessing does not bias the data.
- Data preprocessing demands and consumes the most time and effort, often accounting for more than 80% of the total time spent on a project.
- The quality and usefulness of models created using data mining methods depends largely on the quality of the data used to build them.
- Ratio data includes measurement variables commonly found in the physical sciences and engineering.
- Interval data includes variables that can be measured on interval scales.
- Numeric data represents the numeric values of specific variables.
- Ordinal data includes codes assigned to objects or events as labels that also represent the rank order among them.
- Nominal data includes measurements of simple codes assigned to objects as labels, which are not measurements.
- Categorical data falls into multiple classes used to divide a variable into specific groups. 
Identifying the best method to use usually requires quite a bit of experimentation and sound comparative assessment.
- Data mining and predictive analytics are popular because they make it possible to discover hidden patterns deep inside large data repositories.

## Ch5: Algorithms for Predictive Analytics

- A time series is a sequence of data points of the variable of interest, measured and represented at successive points in time and spaced at uniform time intervals.
- Logistic regression is a very popular, statistically sound, probability-based classification algorithm that employs supervised learning. It was developed in the 1940s as a complement to linear regression and linear discriminant analysis methods.
- Regression can be used for two different purposes: hypothesis testing‚ investigating potential relationships between different variables‚ and prediction/forecasting‚ estimating values of response variables based on one or more explanatory variables.
- Regression is essentially a relatively simple statistical technique for modeling the dependence of a variable (response or output variable) on one or more explanatory (input) variables.
- Regression, especially linear regression, is perhaps the most widely used analysis technique in statistics.
- Historically speaking, the roots of regression date back to the 1920s and 1930s
- Support vector machines (SVMs) are among the most popular machine learning techniques of the recent past, largely because of their superior predictive performance and their theoretical foundation.
- The model that results from neural computing is often called an artificial neural network (ANN) or a neural network. 
- Neural networks represent a brain metaphor for information processing. 
- k-NN is a prediction method for classification- as well as regression-type prediction problems.
- Two popular ones‚Äîartificial neural networks and support vector machines‚Äîare involved in overly - Time-demanding, computationally intensive iterative mathematical derivations.
- Bayes‚ theorem (also called Bayes‚Äô rule), named after the British mathematician Thomas Bayes (1701‚Äì1761), is a mathematical formula for determining conditional probabilities.
- Naive Bayes is a simple probability-based classification method derived from the well-known Bayes‚Äô theorem.
- The statistical methods that have had the biggest impact in the evolution of predictive analytics and data mining include discriminant analysis, linear regression, and logistic regression. The most popular machine learning techniques used in numerous successful predictive analytics projects include decision trees, k-nearest neighbor, artificial neural networks, and support vector machines. 
- Predictive analytics algorithms are mostly derived from either traditional statistical methods or from contemporary machine learning techniques.

## Ch6: Advanced Topics in Predictive Modeling

- In developing machine learning models for predictive analytics, there is always a trade-off between simplicity/parsimony and complexity, generalizability (i.e., capture of the signal) and overfitting (including the noise), predictive accuracy and explainability, overtraining/curve-fitting and undertraining, training error and validation error.
- One of the prevalent concepts in statistics and predictive modeling that is highly relevant to model ensembles is the bias‚Äìvariance trade-off. 
- Usually researchers and practitioners build ensembles for two main reasons: better accuracy and more stable/robust/consistent/reliable outcomes.
- With ensemble modeling, outcomes produced by two or more analytics models are combined into a compound output. Ensembles are primarily used for prediction modeling, where the scores of two or more models are combined to produce better predictions.

## Ch7: Text Analytics, Topic Modeling, and Sentiment Analysis

- Text analytics is a broader concept that includes information retrieval (e.g., searching and identifying relevant documents for a given set of key terms) as well as information extraction, data mining, and web mining, whereas text mining is primarily focused on discovering new and useful knowledge from textual data sources.
- The information age that we are living in is characterized by rapid growth in the amount of data and information collected, stored, and made available in electronic format.