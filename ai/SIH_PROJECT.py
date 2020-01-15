#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
import warnings
warnings.filterwarnings('ignore') # Hides warning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore",category=UserWarning)
sns.set_style("whitegrid") # Plotting style
get_ipython().run_line_magic('matplotlib', 'inline # Plots show up in notebook')
np.random.seed(7) # seeding random number generator


# In[55]:


df = pd.read_csv("/home/shamanth/Downloads/Datafiniti_Amazon_Consumer_Reviews_of_Amazon_Products.csv")
df.head()


# In[7]:


data = df.copy()
data.describe()


# In[8]:


data.info()


# In[10]:



data["asins"].unique()


# In[11]:


asins_unique = len(data["asins"].unique())
print("Number of Unique ASINs: " + str(asins_unique))


# In[12]:


data.hist(bins=50, figsize=(20,15)) # builds histogram and set the number of bins and fig size (width, height)
plt.show()


# In[56]:


from sklearn.model_selection import StratifiedShuffleSplit
print("Before {}".format(len(data)))
dataAfter = data.dropna(subset=["reviews.rating"]) # removes all NAN in reviews.rating
print("After {}".format(len(dataAfter)))
dataAfter["reviews.rating"] = dataAfter["reviews.rating"].astype(int)


# In[57]:


split = StratifiedShuffleSplit(n_splits=5, test_size=0.2)
for train_index, test_index in split.split(dataAfter, dataAfter["reviews.rating"]): 
    strat_train = dataAfter.reindex(train_index)
    strat_test = dataAfter.reindex(test_index)


# In[58]:


len(strat_train)


# In[59]:


strat_train["reviews.rating"].value_counts()/len(strat_train) # value_count() counts all the values based on column


# In[60]:


len(strat_test)


# In[61]:


strat_test["reviews.rating"].value_counts()/len(strat_test)


# In[62]:


reviews = strat_train.copy()
reviews.head(2)


# In[63]:


reviews.to_csv(r"/home/shamanth/Downloads/start_train.csv", index=False)


# In[64]:


n=len(reviews["name"].unique()), len(reviews["asins"].unique())
print(n)

reviews.info()


# In[23]:


reviews.groupby("asins")["name"].unique()


# In[65]:


# Lets see all the different names for this product that have 2 ASINs
different_names = reviews[reviews["asins"] == "B00L9EPT8O,B01E6AO69U"]["name"].unique()
for name in different_names:
    print(name)


# In[25]:


reviews[reviews["asins"] == "B00L9EPT8O,B01E6AO69U"]["name"].value_counts()


# In[66]:


fig = plt.figure(figsize=(16,10))
ax1 = plt.subplot(211)
ax2 = plt.subplot(212, sharex = ax1)
reviews["asins"].value_counts().plot(kind="bar", ax=ax1, title="ASIN Frequency")
np.log10(reviews["asins"].value_counts()).plot(kind="bar", ax=ax2, title="ASIN Frequency (Log10 Adjusted)") 
plt.show()


# In[67]:


# Entire training dataset average rating
reviews["reviews.rating"].mean()


# In[68]:


asins_count_ix = reviews["asins"].value_counts().index
plt.subplots(2,1,figsize=(16,12))
plt.subplot(2,1,1)
reviews["asins"].value_counts().plot(kind="bar", title="ASIN Frequency")
plt.subplot(2,1,2)
sns.pointplot(x="asins", y="reviews.rating", order=asins_count_ix, data=reviews)
plt.xticks(rotation=90)
plt.show()


# In[69]:


plt.subplots (2,1,figsize=(16,12))
plt.subplot(2,1,1)
reviews["asins"].value_counts().plot(kind="bar", title="ASIN Frequency")
plt.subplot(2,1,2)
sns.pointplot(x="asins", y="reviews.doRecommend", order=asins_count_ix, data=reviews)
plt.xticks(rotation=90)
plt.show()


# In[70]:


corr_matrix = reviews.corr()
corr_matrix
# Here we can analyze reviews.ratings with asins


# In[71]:


reviews.info()


# # MODEL IMPLEMENTATION

# In[72]:


def sentiments(rating):
    if (rating == 5) or (rating == 4):
        return "Positive"
    elif rating == 3:
        return "Neutral"
    elif (rating == 2) or (rating == 1):
        return "Negative"
# Add sentiments to the data
strat_train["Sentiment"] = strat_train["reviews.rating"].apply(sentiments)
strat_test["Sentiment"] = strat_test["reviews.rating"].apply(sentiments)
strat_train["Sentiment"][:20]


# In[73]:


X_train = strat_train["reviews.text"]
X_train_targetSentiment = strat_train["Sentiment"]
X_test = strat_test["reviews.text"]
X_test_targetSentiment = strat_test["Sentiment"]
print(len(X_train), len(X_test))


# In[74]:


# Replace "nan" with space
X_train = X_train.fillna(' ')
X_test = X_test.fillna(' ')
X_train_targetSentiment = X_train_targetSentiment.fillna(' ')
X_test_targetSentiment = X_test_targetSentiment.fillna(' ')

# Text preprocessing and occurance counting
from sklearn.feature_extraction.text import CountVectorizer 
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train) 
X_train_counts.shape


# In[75]:


from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer(use_idf=False)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape



# # SUPPORT VECTOR MACHINE

# In[79]:


from sklearn.svm import LinearSVC
clf_linearSVC_pipe = Pipeline([("vect", CountVectorizer()), ("tfidf", TfidfTransformer()), ("clf_linearSVC", LinearSVC())])
clf_linearSVC_pipe.fit(X_train, X_train_targetSentiment)

predictedLinearSVC = clf_linearSVC_pipe.predict(X_test)
np.mean(predictedLinearSVC == X_test_targetSentiment)


# In[80]:


from sklearn.model_selection import GridSearchCV
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],    
             'tfidf__use_idf': (True, False), 
             } 
gs_clf_LinearSVC_pipe = GridSearchCV(clf_linearSVC_pipe, parameters, n_jobs=-1)
gs_clf_LinearSVC_pipe = gs_clf_LinearSVC_pipe.fit(X_train, X_train_targetSentiment)
new_text = ["The tablet is good, really liked it.", # positive
            "The tablet is ok, but it works fine.", # neutral
            "The tablet is not good, does not work very well.","The carpet was ok","The bottle was not bad","It's not big enough to completely cover a horse's head,and it doesnt provide enough air flow for them either","The pen was not good","The book is completely misleading","Almost all of the experiments in the book are really cool, but most of them are meant for people who do this sort of thing a lot and have the technical know-how to understand half of the stuff that the book is talking about and where to get most of the parts. Not reccomended for beginners.","This incredible reading device doesn't just raise the bar, it's a paradigm sh"] # negative

X_train_targetSentiment[gs_clf_LinearSVC_pipe.predict(new_text)]


# In[81]:


X_train


# In[53]:


check=["I thought I owned every kindle model and was surprised to find this one. I loved the shape of this devise and was totally fascinated by it.","lost interest 
       didnt exactly flow with the previous four books"]
X_train_targetSentiment[gs_clf_LinearSVC_pipe.predict(check)]


# In[ ]:




