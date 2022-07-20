import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filename = "WHO-COVID-19-global-data.csv"
df = pd.read_csv(filename)
num = df._get_numeric_data()
num[num < 0] = 0

by_countries = df.groupby('Country')
by_regions = df.groupby('WHO_region')
by_date = df.groupby('Date_reported')

new_cases_by_region = by_regions['New_cases'].sum()
new_deaths_by_region = by_regions['New_deaths'].sum()

plt.bar(np.arange(7), new_deaths_by_region, label = "deaths")
plt.bar(np.arange(7)+0.25, new_cases_by_region/100, label="cases(in hundreds)")
plt.xticks(np.arange(7)+0.25/2,new_cases_by_region.index)
plt.legend()
plt.title("Total deaths and new cases by region")
plt.savefig("total_cases_and_deaths_by_region.png")
plt.close()

new_cases_by_country = by_countries['New_cases'].sum().sort_values()
new_deaths_by_country = by_countries['New_deaths'].sum().sort_values()

count_deaths = [0 for i in range(9)]
for x in new_deaths_by_country.values:
    if 0 <= x < 1e1:
        count_deaths[0] += 1
    elif 1e1 <= x < 1e2:
        count_deaths[1] += 1
    elif 1e2 <= x < 1e3:
        count_deaths[2] += 1
    elif 1e3 <= x < 1e4:
        count_deaths[3] += 1
    elif 1e4 <= x < 1e5:
        count_deaths[4] += 1
    elif 1e5 <= x < 1e6:
        count_deaths[5] += 1
    else:
        count_deaths[6] += 1

count_cases = [0 for i in range(9)]
for x in new_cases_by_country.values:
    if 0 <= x < 1e1:
        count_cases[0] += 1
    elif 1e1 <= x < 1e2:
        count_cases[1] += 1
    elif 1e2 <= x < 1e3:
        count_cases[2] += 1
    elif 1e3 <= x < 1e4:
        count_cases[3] += 1
    elif 1e4 <= x < 1e5:
        count_cases[4] += 1
    elif 1e5 <= x < 1e6:
        count_cases[5] += 1
    elif 1e6 <= x < 1e7:
        count_cases[6] += 1
    elif 1e7 <= x < 1e8:    
        count_cases[7] += 1
    else:
        count_cases[8] += 1

plt.figure(figsize=(10,5))
plt.bar(np.arange(len(count_deaths)),count_deaths,0.5,label="deaths")
plt.bar(np.arange(len(count_cases))+0.2,count_cases,0.5,label="cases")
plt.xticks(np.arange(len(count_deaths)),['0-1e1', '1e1-1e2', '1e2-1e3', '1e3-1e4', '1e4-1e5', '1e5-1e6', '1e6-1e7', '1e7-1e8','>1e8'])
plt.title("Total countries per log(death) and log(cases)")
plt.legend()
plt.savefig("total_countries_per_log_death_and_log_cases.png")
plt.close()


new_cases_by_date = by_date['New_cases'].sum()
new_deaths_by_date = by_date['New_deaths'].sum()
cumulative_cases_by_date = by_date['Cumulative_cases'].sum()
cumulative_deaths_by_date = by_date['Cumulative_deaths'].sum()

print("Total Number of Cases:", cumulative_cases_by_date.sort_values(ascending=False)[0])
print("Total Number of Deaths:", cumulative_deaths_by_date.sort_values(ascending=False)[0])

plt.plot(new_deaths_by_date.index, new_deaths_by_date, label="deaths")
plt.plot(new_cases_by_date.index, new_cases_by_date/100, label="cases(in hundreds)")
plt.vlines(["2021-01-01","2022-01-01"], 0,5e4, color='red')
plt.xticks(new_cases_by_date.index[::200])
plt.ylabel("New Cases and Deaths")
plt.xlabel("Date")
plt.legend()
plt.title("New deaths and new cases by date")
plt.savefig("new_cases_and_deaths_by_date.png")
plt.close()

plt.plot(new_deaths_by_date.index, new_deaths_by_date/new_cases_by_date)
plt.xticks(new_deaths_by_date.index[::200])
plt.title("Ratio of Deaths to Cases (New)")
plt.ylabel("Deaths/Cases")
plt.xlabel("Date")
plt.title("Ratio of Deaths to Cases (New)")
plt.savefig("new_ratio.png")
plt.close()


plt.plot(cumulative_deaths_by_date.index, cumulative_deaths_by_date, label="deaths")
plt.plot(cumulative_cases_by_date.index, cumulative_cases_by_date/100, label="cases(in hundreds)")
plt.vlines(["2021-01-01","2022-01-01"], 0,6e6, color='red')
plt.xticks(cumulative_cases_by_date.index[::200])
plt.ylabel("Cumulative Cases")
plt.xlabel("Date")
plt.legend()
plt.title("Cumulative deaths and cumulative cases by date")
plt.savefig("cumulative_cases_and_deaths_by_date.png")
plt.close()

plt.plot(cumulative_deaths_by_date.index, cumulative_deaths_by_date/cumulative_cases_by_date)
plt.xticks(cumulative_deaths_by_date.index[::200])
plt.title("Ratio of Deaths to Cases (Cumulative)")
plt.ylabel("Deaths/Cases")
plt.xlabel("Date")
plt.title("Ratio of Deaths to Cases (Cumulative)")
plt.savefig("cumulative_ratio.png")
plt.close()
