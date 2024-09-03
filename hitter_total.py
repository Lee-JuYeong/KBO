# -*- coding: utf-8 -*-
"""hitter total.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gz1EdmztvSz-xzNKhzuT1iyfk6SbbxtY
"""

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series, DataFrame
import warnings
warnings.filterwarnings('ignore')
plt.rc('font', family='NanumBarunGothic')

df_hitter = pd.read_csv('/content/hitter_salary_stats_all (2).csv')

df_hitter.columns

df_hitter.head()

df_hitter.info()

df_hitter['연봉(만원)'].hist(bins=100)

df_hitter['후년연봉'].hist(bins=100)

df_hitter.boxplot(column=['연봉(만원)'])

df_hitter.boxplot(column=['후년연봉'])

hitter_feature = df_hitter[['AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR',
       'TB', 'RBI', 'SAC', 'SF', 'BB', 'IBB', 'HBP', 'SO', 'GDP', 'SLG', 'OBP',
       'OPS', 'MH', 'RISP', 'PH-BA', '연도', '연봉(만원)', 'WAR', '후년연봉']]

def plot_hist_each_column(df_hitter):
  plt.rcParams['figure.figsize'] = [20,16]
  fig = plt.figure(1)

  for i in range(len(df_hitter.columns)):
    ax = fig.add_subplot(4,5,i+1)
    plt.hist(df_hitter[df_hitter.columns[i]], bins=50)
    ax.set_title(df_hitter.columns[i])

  plt.show()

plot_hist_each_column(hitter_feature)

pd.options.mode.chained_assignment = None

def standard_scaling(df,scale_columns):
  for col in scale_columns:
    series_mean = df[col].mean()
    series_std = df[col].std()
    df[col] = df[col].apply(lambda x: (x - series_mean) / series_std)


  return df

scale_columns = ['AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR',
       'TB', 'RBI', 'SAC', 'SF', 'BB', 'IBB', 'HBP', 'SO', 'GDP', 'SLG', 'OBP',
       'OPS', 'MH', 'RISP', 'PH-BA', '연도', '연봉(만원)', 'WAR']

hitter_df = standard_scaling(df_hitter, scale_columns)

hitter_df = hitter_df.rename(columns = {'후년연봉' : 'y'})

team_encoding = pd.get_dummies(df_hitter['팀명'])

hitter_df = hitter_df.drop('팀명', axis = 1)

hitter_df = hitter_df.join(team_encoding)

# team_encoding = pd.get_dummies(df_hitter['팀명'])
# hitter_df = df_hitter.drop('팀명', axis = 1)
# hitter_df = hitter_df.join(team_encoding)
# hitter_df

# team_encoding.head()

hitter_df.info()

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

X = hitter_df[hitter_df.columns.difference(['선수명','y'])]
y = hitter_df['y']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=19)

lr = linear_model.LinearRegression()

model = lr.fit(X_train, y_train)

lr.coef_

hitter_df.columns

import statsmodels.api as sm
X_train = X_train.astype(int)
# X_train = X_train.select_dtypes(include=[np.number])
# train = y_train.astype(float)
X_train = sm.add_constant(X_train)
model = sm.OLS(y_train, X_train).fit()
model.summary()

coefs = model.params.tolist()
coefs_series = pd.Series(coefs)

x_labels = model.params.index.tolist()

ax = coefs_series.plot(kind = 'bar')
ax.set_title('feature_coef_graph')
ax.set_xlabel('x_features')
ax.set_ylabel('coef')
ax.set_xticklabels(x_labels)

X = hitter_df[hitter_df.columns.difference(['선수명','y'])]
y = hitter_df['y']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=19)

y_predictions = lr.predict(X_train)
print(sqrt(mean_squared_error(y_train, y_predictions)))
y_predictions = lr.predict(X_test)
print(sqrt(mean_squared_error(y_test, y_predictions)))

"""#EDA"""

import seaborn as sns

corr = hitter_df[scale_columns].corr(method='pearson')
show_cols = ['AVG', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR',
       'TB', 'RBI', 'SAC', 'SF', 'BB', 'IBB', 'HBP', 'SO', 'GDP', 'SLG', 'OBP',
       'OPS', 'MH', 'RISP', 'PH-BA', '연도', '연봉(만원)', 'WAR']
hm = sns.heatmap(corr.values,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size':15},
                 yticklabels=show_cols,
                 xticklabels=show_cols)
plt.tight_layout()
plt.show()

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif['VIF Factor'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

df_k = df_hitter[df_hitter['팀명']=='KIA']
df_k

plt.figure
plt.hist(df_k['연봉(만원)'], bins=100)
# plt.hist(df['예측연봉'], bins=20)


# plt.legend(('현재연봉','예측연봉'))
plt.show()

df_k.describe()

df_k['연봉(만원)'] = pd.to_numeric(df_k['연봉(만원)'], errors='coerce')
df_k['연봉(만원)'].dtype

# 연봉 구간 분류 함수
def salarygap(salary):
    if salary < 3500:
        return '1'
    elif salary < 6000:
        return '2'
    else:
        return '3'
df_k1= df_k['연봉(만원)'].apply(salarygap)
df_k2= df_k['후년연봉'].apply(salarygap)

df_k['올해연봉구간'] = df_k1
df_k['후년연봉구간'] = df_k2

df_k

