import matplotlib
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
oo=pd.read_csv(r"C:\Users\rsa3001\PycharmProjects\pythonProject\ExerciseFiles\data\olympics.csv",skiprows=4)
oo.head()
ee=oo.dropna
oo.Medal.value_counts()
sns.countplot(x='Sport',data=oo)
ee.info()
jhscja