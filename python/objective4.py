# todo: OBJECTIVE-4:--->    number of countries adopted vaccination vs time
#                           ----------------------------------------------
import pandas as pd

df = pd.read_csv("D:\\_Projects\\UOL\\pds\\pds_coursework_3\\data\\vaccination_data.csv")
df['FIRST_VACCINE_DATE']=pd.to_datetime(df['FIRST_VACCINE_DATE'])
print(df.info())