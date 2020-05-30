import pandas as pd
from google.colab import files
uploaded = files.upload()
import matplotlib.pyplot as plt
import csv

a=[]
b=[]

with open('a01_3.csv', 'r') as csvfile:
plots= csv.reader(csvfile, delimiter=',')
for row in plots:
        a.append((row[0]))
        b.append((row[1]))


plt.plot(x,y, marker='o')

plt.title('ECG Signal')

plt.xlabel('Time')
plt.ylabel('Raw_ECG')
plt.xlim(500,520)
plt.ylim(20,400)

plt.show()