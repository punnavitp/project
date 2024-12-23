# -*- coding: utf-8 -*-
"""สำเนาของ E-san_coding.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A9JWfdh3bRYqZl6Gr7VsZmJDntxUXw33

# **Download Datasets**
"""

!wget -q -cO - https://zenodo.org/records/3941387/files/teaching_2018_features_tfidf_256.csv?download=1 > teaching_2018.csv
!wget -q -cO -  https://zenodo.org/records/3941387/files/teaching_2019_features_tfidf_256.csv?download=1 > teaching_2019.csv
!wget -q -cO -  https://zenodo.org/records/3941387/files/mentalhealth_2018_features_tfidf_256.csv?download=1 > mental.csv

"""# **Import packages**"""

import pandas as pd
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.decomposition import KernelPCA, PCA

"""# **Load data**"""

teaching_2018 = pd.read_csv('teaching_2018.csv')
teaching_2019 = pd.read_csv('teaching_2019.csv')
mental = pd.read_csv('mental.csv')

teaching_2018#.head(2)

teaching_2019.head(2)

mental.head(2)

"""**Combine data together**"""

df = pd.concat([teaching_2018, teaching_2019, mental])
del teaching_2018, teaching_2019, mental

df

j = 0
for i in df.columns:
  if i[:5] == 'tfidf':
    print(j)
  j +=1

"""# **Data exploration**"""

df.subreddit.value_counts().plot(kind='bar')

df[df.subreddit == 'mentalhealth']

txt = ' '.join(df[df.subreddit == 'teaching'].post.values)
word_list = txt.split()
Counter(word_list).most_common()

txt = ' '.join(df[df.subreddit == 'mentalhealth'].post.values)
word_list = txt.split()
Counter(word_list).most_common()[:20]

wordcloud = WordCloud(
        background_color = 'black',
        width = 500,
        height = 500,
        max_words=100,
        stopwords = set(STOPWORDS)).generate(str(' '.join(df.post.values)))

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.show()

# สร้าง Wordcloud ประเภท Teaching ด้วยตนเอง
wordcloud = WordCloud(
        background_color = 'blue',
        width = 400,
        height = 400,
        max_words=500,
        stopwords=set(STOPWORDS)).generate(str(' '.join(df[df['subreddit'] == 'teaching'].post.values)))

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.show()

# สร้าง Wordcloud ประเภท Mentalhealth ด้วยตนเอง
wordcloud = WordCloud(
        background_color = 'blue',
        width = 400,
        height = 400,
        max_words=500,
        stopwords=set(STOPWORDS)).generate(str(' '.join(df[df['subreddit'] == 'mentalhealth'].post.values)))

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
fig.show()

"""# **Feature extraction**"""

vectorizer = CountVectorizer()

# ให้ทำการแปลงข้อความให้เป็น Feature โดยการระบุข้อมูลที่ใช้ในการแปลงให้ถูกต้อง
X = vectorizer.fit_transform(df['post'])

# X = vectorizer.fit_transform(_____)

print(X.shape)
print(X.toarray())
print(vectorizer.get_feature_names_out())

"""# **Split Data into training and test sets**"""

df['label'] = pd.Categorical(df.subreddit).codes

df

# ให้ระบุคอลัมน์ ที่จะใช้เป็น label เพื่อที่จะใช้ในการสอนและทำนาย

y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

"""# **Modelling**"""

log = LogisticRegression(random_state=0).fit(X_train, y_train)

print(log.predict(X_test[:10]))
print(log.predict_proba(X_test[:10]))
print(log.score(X_test, y_test))

"""**ให้ทดลองสร้างโมเดล ด้วย Algorithms อื่นๆ ด้วยตัวเอง อีก 2 โมเดล**"""

from sklearn.ensemble import RandomForestClassifier

clf1 = RandomForestClassifier(random_state=0)

clf1.fit(X_train, y_train)

predictions = clf1.predict(X_test[:10])

probabilities = clf1.predict_proba(X_test[:10])

accuracy = clf1.score(X_test, y_test)

print("Predictions for the first 10 test samples:", predictions)
print("Predicted probabilities for the first 10 test samples:", probabilities)
print("Model accuracy on the test set:", accuracy)

from xgboost import XGBClassifier

clf2 = XGBClassifier(random_state=0)

clf2.fit(X_train, y_train)

predictions = clf2.predict(X_test[:10])

probabilities = clf2.predict_proba(X_test[:10])

accuracy = clf2.score(X_test, y_test)

print("Predictions for the first 10 test samples:", predictions)
print("Predicted probabilities for the first 10 test samples:", probabilities)
print("Model accuracy on the test set:", accuracy)

"""# **Evaluation**"""

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล


y_true = y_test
y_pred = log.predict(X_test)

target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล clf1


y_true = y_test
y_pred = clf1.predict(X_test)


target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล clf2


y_true = y_test
y_pred = clf2.predict(X_test)


target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))

"""**ให้สร้างโมเดลด้วยตัวเองโดยใช้ LIWC features ที่มีให้ใน Dataset เพื่อใช้ในการ Train และ Test โมเดลด้วยตัวเอง**"""

# คอลัมน์ LIWC features จะอยู่ในคอลัมน์ที่ 4 ถึง 94

df.columns[4:94]

df.iloc[:, 4:94]

X = df.iloc[:, 4:94]
y = df['label']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

log = LogisticRegression(random_state=0).fit(X_train, y_train)

print(log.predict(X_test[:10]))
print(log.predict_proba(X_test[:10]))
print(log.score(X_test, y_test))

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล



y_true = y_test[:10]
y_pred = log.predict(X_test[:10])



target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))

"""**ให้สร้างโมเดลด้วยตัวเองโดยใช้ TF-IDF features ที่มีให้ใน Dataset เพื่อใช้ในการ Train และ Test โมเดลด้วยตัวเอง**"""

# คอลัมน์ LIWC features จะอยู่ในคอลัมน์ที่ 94 ถึง 350

df.columns[94:350]

X = df.iloc[:, 94:350]
y = df['label']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

log = LogisticRegression(random_state=0).fit(X_train, y_train)

print(log.predict(X_test[:10]))
print(log.predict_proba(X_test[:10]))
print(log.score(X_test, y_test))

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล



y_true = y_test[:10]
y_pred = log.predict(X_test[:10])



target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))

"""**ให้สร้างโมเดลด้วยตัวเองโดยใช้ TF-IDF และ LIWC features ที่มีให้ใน Dataset เพื่อใช้ในการ Train และ Test โมเดลด้วยตัวเอง**"""

X = df[df.columns[4:350]]
y = df['label']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

log = LogisticRegression(random_state=0).fit(X_train, y_train)

print(log.predict(X_test[:10]))
print(log.predict_proba(X_test[:10]))
print(log.score(X_test, y_test))

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล



y_true = df['label'][:10]
y_pred = log.predict(X_test[:10])




target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))

"""**ให้สร้างโมเดลด้วยตัวเองโดยใช้ TF-IDF และ LIWC features ที่มีให้ใน Dataset เพื่อใช้ในการ Train และ Test โมเดลด้วยตัวเอง จากนั้นให้ทำการลด Dimensions ของข้อมูลเพื่อเปรียบเทียบประสิทธิภาพ**"""

pca = PCA(n_components=100, whiten=True) # n_components สามารถแก้ไขจำนวน Dimensions ตามต้องการได้

X = df[df.columns[4:350]]
y = df['label']



X = pca.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42)

log = LogisticRegression(random_state=0).fit(X_train, y_train)

print(log.predict(X_test[:10]))
print(log.predict_proba(X_test[:10]))
print(log.score(X_test, y_test))

# ระบุ y_true และ y_pred ด้วยตัวเองให้ถูกต้อง เพื่อใช้แสดงประสิทธิภาพของโมเดล

y_true = df['label'][:10]
y_pred = log.predict(X_test[:10])


target_names = ['MentalHealth', 'Teaching']
print(classification_report(y_true, y_pred, target_names=target_names))