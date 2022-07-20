import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

filename = "mcdonalds_data.csv"
df = pd.read_csv(filename)

size = df.shape[0]
fields = []
rows = []

row_num = 1
by_likes = df.groupby('Like')
by_ages = df.groupby('Age')
by_visit_frequencies = df.groupby('VisitFrequency')
by_gender = df.groupby("Gender")

def f(A):
    B = []
    for n in A:
        if n == "I love it!+5":
            B.append(5)
        elif n == "I hate it!-5":
            B.append(-5)
        else:
            B.append(int(n)) 
    return B

# print(by_likes.size())
plt.pie(by_likes.size(), labels=by_likes.size().index, autopct='%1.0f%%')
plt.title("Pie of Likes")
plt.savefig("Pie_of_likes.png")
plt.close()
df["Like"] = f(df["Like"])
print(5 + statistics.mean(df["Like"]), "out of 10 rating.")

df["Age"] = f(df["Age"])
print(statistics.mean(df["Age"]), ": average age.")
print(statistics.stdev(df["Age"]), ": standard deviation of age.")

# print(by_ages.size())
plt.plot(by_ages.size().index, by_ages.size())
plt.bar(by_ages["Like"].sum().index, 5*(5 + (by_ages["Like"].sum())/by_ages.size()), color='red')
plt.title("Plot of age")
plt.savefig("Plot_of_ages.png")
plt.close()


# print(by_visit_frequencies.size())
plt.pie(by_visit_frequencies.size(), labels=by_visit_frequencies.size().index, autopct='%1.0f%%', explode=(0,0.2,0,0,0,0))
plt.savefig("Pie_of_frequencies.png")
plt.close()

x = by_visit_frequencies["Like"].sum().sort_values()
print("Average ratings by visit frequency:", 5 + (x)/by_visit_frequencies.size())
plt.figure(figsize=(12,5))
plt.plot((5 + (x)/by_visit_frequencies.size()).sort_values())
plt.title("Plot of rating given w.r.t visit frequencies")
plt.savefig("Plot_of_avg_rating_wrt_frequencies.png")
plt.close()

# print(by_gender.size())
ax1 = plt.subplot2grid((1,2), (0,0))
plt.pie(by_gender.size(), labels=by_gender.size().index, autopct='%1.0f%%')
plt.title("Pie of customer gender")
ax1 = plt.subplot2grid((1,2), (0,1))
print("Average ratings by gender:", 5 + (by_gender["Like"].sum())/by_gender.size())
plt.pie(5 + (by_gender["Like"].sum())/by_gender.size(), labels=by_gender["Like"].sum().index, autopct='%1.0f%%')
plt.title("Pie of rating given w.r.t gender")
plt.savefig("Pie_of_genders.png")
plt.close()