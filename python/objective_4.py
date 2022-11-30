# todo---------------------Daily Vaccination-----------------------------------
import pandas as pd
from datetime import datetime

daily_vac_df = pd.read_csv(
    'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv')
daily_vac_df["date"] = pd.to_datetime(daily_vac_df["date"])
print(daily_vac_df)


# Calculating total number of vaccine for a particular vaccine type
# by individaul month
# daily_vac_df

# function for finding last day of month
def last_day_of_month(year, month):
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for i in last_days:
        try:
            end = datetime(year, month, i)
        except ValueError:
            continue
        else:
            return end.date()
    return None


# print(last_day_of_month(2001, 2))

# list of vaccine used
vaccine_ls = daily_vac_df['vaccine'].unique().tolist()

# list of locations
location_ls = daily_vac_df['location'].unique().tolist()

x = 0
ls = []
df = pd.DataFrame(columns=['location', 'date', 'vaccine', 'total_vaccinations'])
# find max value of a Y-vaccine for X-location
for i in location_ls:
    for j, row in daily_vac_df.iterrows():
        if row['location'] == i:
            for k in vaccine_ls:
                if row['vaccine'] == k:
                    full_date = str(row['date']).split('-')
                    year = full_date[0]
                    month = full_date[1]
                    date = last_day_of_month(int(year), int(month))
                    # find max value of vaccine
                    # for this row wee need vaccine quantity, we already have:
                    # vaccine name and location name
                    if row['date'] == date:
                        # x += 1
                        data = [{'location': i, 'date': date, 'vaccine': k,
                                 'total_vaccinations': row['total_vaccinations']}]
                        df2 = pd.DataFrame(data)
                        df = df.append(df2)
                        # print(df)
print(df)
# df = pd.read_csv('vc.csv')
# # ls2
#
# # list of locations
# date_ls = df['date'].unique().tolist()
# dff = pd.DataFrame(columns=['date',
#                             'Oxford/AstraZeneca',
#                             'Sinopharm/Beijing',
#                             'SputnikV',
#                             'Pfizer/BioNTech',
#                             'Moderna',
#                             'CanSino',
#                             'Johnson&Johnson',
#                             'Novavax',
#                             'Valneva',
#                             'Medicago',
#                             'Sinovac',
#                             'Covaxin',
#                             'SKYCovione'])
# # dff['date']=date_ls
#
# for i in vaccine_ls:
#     total = []
#     for j, row in df.iterrows():
#         if row['vaccine'] == i:
#             for k in date_ls:
#                 if row['date'] == k:
#                     total.append(row['total_vaccinations'])
#     print(total)
#                 # data = [{'date': total[0], k: total[1]}]
#                 # df2 = pd.DataFrame(data)
#     dff[i] = total
#     print(dff)
# dff.to_csv('dff.csv')
