# Artificial Intelligence: An Overview of AI and Machine Learning
by Alex Castrounis

[Course page](https://learning.oreilly.com/live-events/artificial-intelligence-an-overview-of-ai-and-machine-learning/0636920054812/0636920078976/?utm_medium=email&utm_source=platform+b2b&utm_campaign=engagement&utm_content=lot+recording)
[Book: AI for Business and People](https://learning.oreilly.com/library/view/ai-for-people/9781492036562/)
[Video: Learn from the Experts about AI](https://learning.oreilly.com/videos/learn-from-the/9781492030010/)
[AI Superstream resources](https://learning.oreilly.com/beta-search/?q=AI%20Superstream&type=*&order_by=relevance)

## AI for People and Business (AIPB)

- Framework for AIPB
- AI is able to have very impactful benefits for business (revenue, profits, efficiencies) and for people (treatments in non-intrusive ways, retirement savings, professional work w/ making more productive and enjoyable, whether a tumor is cancerous)
- What is AI?
    - Intelligence - learning, understanding, and application of knowledge to achieve one or more goals. Learn over time and develop more understanding of the world around us. Common sense is based on our world model and helps us to achieve goals and complete tasks. 
    - Artificial Intelligence - simply intelligence exhibited by machines (e.g., predict stock price, product recommendation, determine if product is good/bad/neutral, detect email as spam). Been around since the 1950s. A lot of concepts - ML, neural networks, deep learning - thought of a long time ago. Try to artificially model the biological brain in an artificial way.
    - Related fields - neuroscience, phycology, philosophy, etc.
- Key part is how do machines learn - they way machines learn to get an understanding (becomes a model). Machines use learning algorithms to learn from data. Usually doesn't require explicit programming. 
    - Initially based on expert systems - aka rules based systems (i.e., consider logic diagrams). Have to think of all the scenarios, so not really true intelligence of how humans learn. Every rule needs to be considered in advance.
    - Machines came along and could learn from data with no explicit programming and no domain expertise. Could potentially train a model that needs to learn and know an industry based on data (note: this is a simplified view). 

## AI Concepts - Mostly ML

- Cognition - the mental action of acquiring knowledge and understanding through thought, experience, and the senses. Our brains detect patterns. Machines could do the same thing with enough data. Human brain much more complex than machine, however machines can learn with a model and data. (Note: AI is narrow and specialized, and can only do one specific task.)
- Machine Learning
    - Non-technical - automatically learn from data and be able to improve knowledge learned from expertise without programming or domain expertise.
    - Technical - using algorithms to learn a target functions that maps input variables to output variables (i.e., mapping functions).
    - Parametric - type of optimization problem w/ assumed model form (params, functions) and can learn optional parameters (coefficients). (Note: consider linear regression w/ data as a value or set of values.)
    - Non-parametric - no assumed model form. Learning algorithm learns model as part of learning process (i.e., decision trees). The tree itself learns as part of the parameters based on the data. Still consider optimization (i.e., CART) but aren't the same as gradient decent or loss. Could use genie coefficient and want to find best possible decision tree.
    - Data types
        - Structured - fits neatly into spreadsheet or relational database (i.e., tables, rows, keys, normalization).
        - Unstructured - data that doesn't fit into a table, spreadsheet, and database (e.g., image, audio, video, text).
        - Semi-structured - combination of both types of data - structured and unstructured (e.g., XML, JSON).
        - Labeled and Unlabeled data - specific data elements to map to model. Labeled includes features and target where unlabeled data has features only.
    - Most machine learning is not self-learning, it is based on model optimization. There is an area of AI called reinforcement learning that is self-learning and self-evolving.
    - Machine learning types - supervised, unsupervised, semi-supervised, self-supervised, reinforcement, and transfer (not an exhaustive list). Comes down to data, targeted and labeled versus not. (Example models - [GPT-3](https://www.technologyreview.com/2020/07/20/1005454/openai-machine-learning-language-generator-gpt-3-nlp/), [BERT](https://en.wikipedia.org/wiki/BERT_(language_model))). (GPT-3 developed by [OpenAI](https://openai.com/).)
    - Multiple learning algorithms - see the algorithm slide.

## Neural Networks and Deep Learning

- Artificial neurons - try to model the human brain. Use data inputs, combined with parameters (e.g., weights), then do simple calculation, receive output and pass to an activation function. If output, exceeds threshold number, then passed along to one or more inputs or outputs.
- Artificial neural network (ANN) - combined neuron mapping. Multiple hidden layers are considered deep learning. Not more than one layer then it's shallow learning.

## Increasing Levels of Sophistication w/ AI

- Artificial Narrow Intelligence (ANI) - where we are today (e.g., shallow learning, deep learning, applied AI).
- Artificial General Intelligence (AGI) - at the level of human intelligence. May never get here.
- Artificial Super Intelligence (ASI) - AI that exceeds human-level intelligence (i.e., doomsday scenario).

## Building These AI Models

- [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/)
- [GABDO AI Process Model](https://learning.oreilly.com/library/view/ai-for-people/9781492036562/app02.html)
    - Goals - opportunities and hypotheses
    - Acquire - identify, acquire, and prepare data
    - Build - explore, select, train, validate, test, improve a model
    - Deliver - present insights, take action, make decisions, deploy solutions
    - Optimize - monitor, analyze, and improve (models drift over time - analytical drift)

## Tradeoffs and Considerations w/ AI Models

- Model - overfitting and underfitting, performance and explainability
- Data and features - representative, adequate quality, depth, completeness
- Performance - error tradeoffs
* Note: Overfitting and underfitting - trying to match model to the data that you have.