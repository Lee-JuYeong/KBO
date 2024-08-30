# -*- coding: utf-8 -*-
"""주루,홈런.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11xffTVC5MYG8QdHDQ0KmfpElkQ4PGV9N

주루가 강한 타자는 홈런타자보다 연봉이 적을까?
"""

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np

df = pd.read_csv('/content/runner.csv')
df.drop(df[df['SBA']==0].index, inplace=True)

df2020 = df[df['연도']==2020]
df2021 = df[df['연도']==2021]
df2022 = df[df['연도']==2022]
df2023 = df[df['연도']==2023]
df2024 = df[df['연도']==2024]

df2020_h = df2023[df2023['팀명']=='한화']
df2020_h = df2020_h[~df2020_h['선수명'].isin(['터크먼','노수광'])]
df2020_h = df2020_h.drop(['순위','G','SBA','CS','SB%','OOB','PKO'], axis=1)
df_runner_hh = df2020_h.sort_values(by='SB',ascending=False)[:3]
df_runner_hh

df_runner_hh = df2020_h.sort_values(by='SB',ascending=False)[:3]
df_runner_hh['후년연봉'] = [10000,17800,35000]
df_runner_hh['구분'] = '도루'
df_runner_hh=df_runner_hh.to_csv('한화2023도루.csv', index = False)
df_runner_hh=pd.read_csv('/content/한화2023도루.csv')
df_runner_hh

df1 = pd.read_csv('/content/hitter_salary_stats_all.csv')

df1 = df1[df1['연도']==2023]

df2020_hh = df1[df1['팀명']=='한화']
df2020_hh = df2020_hh[['선수명','팀명','HR','연도','후년연봉']]
df_homerun_hh = df2020_hh.sort_values(by='HR',ascending=False)[:3]
df_homerun_hh['구분'] = '홈런'
# df_homerun_hh.loc[df_homerun_hh['선수명']=='최재훈', '후년연봉'] = 60000
df_homerun_hh.to_csv('한화2020홈런.csv', index = False)
df_homerun_hh=pd.read_csv('/content/한화2020홈런.csv')
df_homerun_hh

result = pd.concat([df_runner_hh,df_homerun_hh], axis=0)
result

import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
plt.rcParams['figure.figsize']=[10,8]
sns.set(style='whitegrid')
sns.set_palette('pastel')
warnings.filterwarnings('ignore')

from matplotlib import rc
import platform

if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else: #linux
    rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

ax1.bar(df_runner_hh['선수명'], df_runner_hh['후년연봉'], color='blue', alpha=0.7)
ax1.set_title('후년연봉 - Runner')
ax1.set_xlabel('선수명')
ax1.set_ylabel('후년연봉')
ax1.grid(True)

ax2.bar(df_homerun_hh['선수명'], df_homerun_hh['후년연봉'], color='green', alpha=0.7)
ax2.set_title('후년연봉 - Homerun')
ax2.set_xlabel('선수명')
ax2.set_ylabel('후년연봉')
ax2.grid(True)

plt.tight_layout()

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

ax1.bar(df_runner_hh['선수명'], df_runner_hh['후년연봉'], color='blue', alpha=0.7)
ax1.set_title('후년연봉 - Runner')
ax1.set_xlabel('선수명')
ax1.set_ylabel('후년연봉')
ax1.grid(True)

ax2.bar(df_homerun_hh['선수명'], df_homerun_hh['후년연봉'], color='green', alpha=0.7)
ax2.set_title('후년연봉 - Homerun')
ax2.set_xlabel('선수명')
ax2.set_ylabel('후년연봉')
ax2.grid(True)

plt.tight_layout()

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

ax1.bar(df_runner_hh['선수명'], df_runner_hh['후년연봉'], color='blue', alpha=0.7)
ax1.set_title('후년연봉 - Runner')
ax1.set_xlabel('선수명')
ax1.set_ylabel('후년연봉')
ax1.grid(True)

ax2.bar(df_homerun_hh['선수명'], df_homerun_hh['후년연봉'], color='green', alpha=0.7)
ax2.set_title('후년연봉 - Homerun')
ax2.set_xlabel('선수명')
ax2.set_ylabel('후년연봉')
ax2.grid(True)

plt.tight_layout()

plt.show()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

ax1.bar(df_runner_hh['선수명'], df_runner_hh['후년연봉'], color='blue', alpha=0.7)
ax1.set_title('후년연봉 - Runner')
ax1.set_xlabel('선수명')
ax1.set_ylabel('후년연봉')
ax1.grid(True)

ax2.bar(df_homerun_hh['선수명'], df_homerun_hh['후년연봉'], color='green', alpha=0.7)
ax2.set_title('후년연봉 - Homerun')
ax2.set_xlabel('선수명')
ax2.set_ylabel('후년연봉')
ax2.grid(True)

plt.tight_layout()

plt.show()

