#MapPlot.py
#Name:
#Date:
#Assignment:
import importlib.util
import sys
import pandas as pd
import matplotlib.pyplot as plt

spec = importlib.util.spec_from_file_location("billionaires", "billionaires.py")
billionaires = importlib.util.module_from_spec(spec)
sys.modules["billionaires"] = billionaires
spec.loader.exec_module(billionaires)

data = billionaires.get_billionaire()

year_and_worth = []

for person in data:
    year = person["year"]
    worth = person["wealth"]["worth in billions"]
    year_and_worth.append({"year": year, "worth": worth})

df = pd.DataFrame(year_and_worth)

average_by_year = df.groupby("year")["worth"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(average_by_year["year"], average_by_year["worth"], marker='o')
plt.title("Average Billionaire Net Worth Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Worth (in billions)")
plt.grid(True)
plt.show()