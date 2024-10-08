# -*- coding: utf-8 -*-
"""Senior & Junior.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/137Zr6TKLvk1wKL3si04sxiTLCH68j6os
"""

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

from matplotlib import rc
import platform
import pandas as pd
import matplotlib.pyplot as plt

if platform.system() == 'Windows':
    rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    rc('font', family='AppleGothic')
else: #linux
    rc('font', family='NanumGothic')

plt.rcParams['axes.unicode_minus'] = False

# df2 = pd.read_csv('/content/pitchers_salary_current&predict.csv')
# df2

import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('/content/hitter_salary_number.csv')

df1_s = df1[df1['연차']>=9]
df1_j = df1[df1['연차']<=5]

# df1_s_d = df1_s[df1_s['팀명']=='한화']
# df1_s_d2020 = df1_s_d[df1_s_d['연도']==2020]
# # df1_s_d2020 = df1_s_d2020['현재연봉'].sum()
# df1_s_d2020

# df1_j_d = df1_j[df1_j['팀명']=='SSG']
# df1_j_d
# df1_j_d2023 = df1_j_d[df1_j_d['연도']==2020]
# #df1_j_d2023 = df1_j_d2023['현재연봉'].sum()
# df1_j_d2023

# df1_s_d.describe()

# df1_j_d.describe()

# df1_j = pd.DataFrame(df1_j)
# df1_j.columns

df1_j = df1_j[['팀명','연도','H','연차','후년연봉']]
df1_s = df1_s[['팀명','연도','H','연차','후년연봉']]

# # 2020년 데이터 추출(저연차)
# df1_jd = df1_j[df1_j['팀명']=='두산']
# df1_jd2020= df1_jd[df1_jd['연도']==2020]
# df1_j_era = df1_jd2020['ERA'].mean()
# df1_j_sum = df1_jd2020['현재연봉'].sum()

# #2020년 데이터 추출(고연차)
# df1_sd = df1_s[df1_s['팀명']=='두산']
# df1_sd2020= df1_sd[df1_sd['연도']==2020]
# df1_s_era = df1_sd2020['ERA'].mean()
# df1_s_sum = df1_sd2020['현재연봉'].sum()

# #데이터 프레임 생성
# df1_sjd2020 = {'팀명' : '두산',
#               '연도' : '2020',
#               '연차' : ['저연차','고연차'],
#               '평균ERA' : [df1_j_era, df1_s_era],
#               '현재연봉' : [df1_j_sum, df1_s_sum]}

# df1_sjd2020 =pd.DataFrame(df1_sjd2020)
# df1_sjd2020

import pandas as pd

teams = ['한화', '삼성', '롯데', 'KIA', 'LG', '키움', 'KT', 'SSG', 'NC', '두산']
years = [2020, 2021, 2022, 2023]

results = []

for team in teams:
    for year in years:
        df1_jd = df1_j[df1_j['팀명'] == team]
        df1_jd_year = df1_jd[df1_jd['연도'] == year]
        df1_j_era = df1_jd_year['H'].median()
        df1_j_sum = df1_jd_year['후년연봉'].median()

        df1_sd = df1_s[df1_s['팀명'] == team]
        df1_sd_year = df1_sd[df1_sd['연도'] == year]
        df1_s_era = df1_sd_year['H'].mean()
        df1_s_sum = df1_sd_year['후년연봉'].mean()

        result = {
            '팀명': team,
            '연도': year,
            '연차': ['저연차','고연차'],
            '안타 평균값': [df1_j_era, df1_s_era],
            '후년연봉 평균값': [df1_j_sum, df1_s_sum]
        }

        results.append(pd.DataFrame(result))

df1_sjd_all = pd.concat(results, ignore_index=True)
df1_sjd_all

# df1_sjd_all=df1_sjd_all[df1_sjd_all['팀명']=='두산']
# df1_sjd_all

import matplotlib.pyplot as plt

teams = ['한화', '삼성', '롯데', 'KIA', 'LG', '키움', 'KT', 'SSG', 'NC', '두산']

fig, axes = plt.subplots(len(teams), 2, figsize=(16, 40))

for i, team in enumerate(teams):
    team_data = df1_sjd_all[df1_sjd_all['팀명'] == team]

    team_jo = team_data[team_data['연차'] == '저연차']
    team_go = team_data[team_data['연차'] == '고연차']

    ax1 = axes[i, 0]
    ax1.plot(team_jo['연도'], team_jo['안타 평균값'], marker='o', label='저연차 H', color='mediumblue')
    ax1.plot(team_go['연도'], team_go['안타 평균값'], marker='o', label='고연차 H', color='deeppink')
    ax1.set_title(f'{team} 팀의 연도별 안타 평균값')
    ax1.set_xlabel('연도')
    ax1.set_ylabel('안타 평균값')
    ax1.legend()

    ax1.set_xticks(team_jo['연도'].unique())
    ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

    ax2 = axes[i, 1]
    ax2.plot(team_jo['연도'], team_jo['후년연봉 평균값'], marker='o', label='저연차 후년연봉 평균값', color='mediumblue')
    ax2.plot(team_go['연도'], team_go['후년연봉 평균값'], marker='o', label='고연차 후년연봉 평균값', color='deeppink')
    ax2.set_title(f'{team} 팀의 연도별 후년연봉 평균값')
    ax2.set_xlabel('연도')
    ax2.set_ylabel('후년연봉 평균값')
    ax2.legend()

    ax2.set_xticks(team_jo['연도'].unique())
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

plt.tight_layout()
plt.show()

df = pd.read_csv('/content/pitchers_stat_cluster.csv')

df_s = df[df['연차']>=9]
df_j = df[df['연차']<=5]

df_j = df_j[['팀명','연도','WAR_x','연차','예측연봉']]
df_s = df_s[['팀명','연도','WAR_x','연차','예측연봉']]

# df_j[df_j['팀명'] == 'SSG']

import pandas as pd

teams = ['한화', '삼성', '롯데', 'KIA', 'LG', '키움', 'KT', 'SSG', 'NC', '두산']
years = [2020, 2021, 2022, 2023]

results = []

for team in teams:
    for year in years:
        df_jd = df_j[df_j['팀명'] == team]
        df_jd_year = df_jd[df_jd['연도'] == year]
        df_j_era = df_jd_year['WAR_x'].mean()
        df_j_sum = df_jd_year['예측연봉'].mean()

        df_sd = df_s[df_s['팀명'] == team]
        df_sd_year = df_sd[df_sd['연도'] == year]
        df_s_era = df_sd_year['WAR_x'].mean()
        df_s_sum = df_sd_year['예측연봉'].mean()

        result = {
            '팀명': team,
            '연도': year,
            '연차': ['저연차','고연차'],
            'WAR 평균값': [df_j_era, df_s_era],
            '후년연봉 평균값': [df_j_sum, df_s_sum]
        }

        results.append(pd.DataFrame(result))

df_sjd_all = pd.concat(results, ignore_index=True)
df_sjd_all

import matplotlib.pyplot as plt

teams = ['한화', '삼성', '롯데', 'KIA', 'LG', '키움', 'KT', 'SSG', 'NC', '두산']

fig, axes = plt.subplots(len(teams), 2, figsize=(16, 40))

for i, team in enumerate(teams):
    team_data = df_sjd_all[df_sjd_all['팀명'] == team]

    team_jo = team_data[team_data['연차'] == '저연차']
    team_go = team_data[team_data['연차'] == '고연차']

    ax1 = axes[i, 0]
    ax1.plot(team_jo['연도'], team_jo['WAR 평균값'], marker='o', label='저연차 WAR', color='mediumblue')
    ax1.plot(team_go['연도'], team_go['WAR 평균값'], marker='o', label='고연차 WAR', color='deeppink')
    ax1.set_title(f'{team} 팀의 연도별 WAR 평균값')
    ax1.set_xlabel('연도')
    ax1.set_ylabel('WAR 평균값')
    ax1.legend()

    ax1.set_xticks(team_jo['연도'].unique())
    ax1.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

    ax2 = axes[i, 1]
    ax2.plot(team_jo['연도'], team_jo['후년연봉 평균값'], marker='o', label='저연차 후년연봉 평균값', color='mediumblue')
    ax2.plot(team_go['연도'], team_go['후년연봉 평균값'], marker='o', label='고연차 후년연봉 평균값', color='deeppink')
    ax2.set_title(f'{team} 팀의 연도별 후년연봉 평균값')
    ax2.set_xlabel('연도')
    ax2.set_ylabel('후년연봉 평균값')
    ax2.legend()

    ax2.set_xticks(team_jo['연도'].unique())
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: int(x)))

plt.tight_layout()
plt.show()

