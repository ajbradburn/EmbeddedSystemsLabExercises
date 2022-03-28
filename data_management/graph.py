import matplotlib.pyplot as plt
import matplotlib.dates as mpdates
import pandas

file_name = "log.csv"
data = pandas.read_csv(file_name)
print(data[:5])
