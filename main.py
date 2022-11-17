import pandas as p
from matplotlib import pyplot as plt

#todo vaccination data
main_df = p.read_csv("data/vaccination_data.csv")
print(main_df)
# main_df=main_df[main_df[]]

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# columns = ["COUNTRY", "TOTAL_VACCINATIONS"]
# print("Contents in csv file:", main_df)
# # x = "Cases - cumulative total"
# plt.plot(main_df.COUNTRY, main_df.TOTAL_VACCINATIONS)
# # plt.style.use('ggplot')
# plt.ticklabel_format(useOffset=False, style='plain', axis='y')
# plt.xticks(rotation='vertical')
# plt.show()




#todo piechrat
main_df=main_df.dropna()
# plt.figure(main_df.TOTAL_VACCINATIONS, dpi=72)
plt.pie(main_df.TOTAL_VACCINATIONS)
# plt.legend()
plt.legend(title="Vaccination:",labels=main_df.COUNTRY)
plt.show()

# ---------------------------------------------------------------------
# todo 2
# import matplotlib.pyplot as plt
# import csv
#
# x = []
# y = []
#
# with open('data/covid_data.csv', 'r') as csvfile:
#     lines = csv.reader(csvfile, delimiter=',')
#     for row in lines:
#         x.append(row[0])
#         y.append(int(row[1]))
#
# plt.plot(x, y, color='g', linestyle='dashed',
#          marker='o', label="Covid Data")
#
# plt.xticks(rotation=25)
# plt.xlabel('Dates')
# plt.ylabel('Temperature(°C)')
# plt.title('Weather Report', fontsize=20)
# plt.grid()
# plt.legend()
# plt.show()
