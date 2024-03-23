import matplotlib.pyplot as plt
import csv
import statistics

x = []
y = []

with open ('sunspot_data.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        x.append(row[0])
        y.append(float(row[1]))
plt.plot(x[:10], y[:10], color = 'r', label = 'Sunspot data')
plt.xlabel('Years')
plt.ylabel('Numbers')
plt.title('Sunspot data')
plt.grid()
plt.legend()
plt.show()

print(statistics.mean(y))
print(statistics.median_low(y))
print(statistics.harmonic_mean(y))