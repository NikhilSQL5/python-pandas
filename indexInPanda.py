import pandas as pd

data = [100,101,102,103,104]

series = pd.Series(data, index= ["a","b","c","d","e"])

series.name = "number"

print("---------------------------")
print("print the series")
print(series)
print("---------------------------")
#loc = location by the label
print("loaction by label (loc)")
print(series.loc["a"])
print("---------------------------")
print("change the value using iloc")
#change the series values using the iloc
series.loc["b"] = 999
print(series)
print("---------------------------")
#loc = location by the label
print("integer location (iloc)")
print(series.iloc[1])
print("---------------------------")
print("print the value smaller than 103")
print(series[series<103])
print("---------------------------")
print("print the value greater than 103")
print(series[series>103])
print("---------------------------")
