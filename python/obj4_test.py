import pandas as pd
from datetime import datetime

daily_vac_df = pd.read_csv(
    'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by'
    '-manufacturer.csv')
daily_vac_df["date"] = pd.to_datetime(daily_vac_df["date"])
# print(daily_vac_df)
# list of vaccine used
vaccine_ls = daily_vac_df['vaccine'].unique().tolist()

df = pd.read_csv('vc.csv')
# ls2

# list of locations
date_ls = df['date'].unique().tolist()
dff = pd.DataFrame(columns=['date',
                            'Oxford/AstraZeneca',
                            'Sinopharm/Beijing',
                            'SputnikV',
                            'Pfizer/BioNTech',
                            'Moderna',
                            'CanSino',
                            'Johnson&Johnson',
                            'Novavax',
                            'Valneva',
                            'Medicago',
                            'Sinovac',
                            'Covaxin',
                            'SKYCovione'])
# dff['date']=date_ls

total = []

# for i in vaccine_ls:
#     for j, row in df.iterrows():
#         if row['vaccine'] == i:
#             x = 0
#             for k in date_ls:
#                 if row['date'] == k:
#                     # todo adding number_of_vaccine for a particular date on a particular date
#                     x += row['total_vaccinations']
#             total.append(x)
#             print(i, " ", total, "\n")
#                     # data = [{'date': total[0], k: total[1]}]
#                 # df2 = pd.DataFrame(data)
#     # dff[i] = total
#     # print(dff)
# # dff.to_csv('dff.csv')

for i,row in df.iterrows():
