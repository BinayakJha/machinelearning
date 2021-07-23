import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\user\Desktop\Python-2\data-analysis\covid\covid.csv")
print(data)

plt.plot(data['Date'], data['New Cases'],label='New Cases')
pl2 = plt.plot(data['Date'], data['Death'],label='Death',color="red")
plt.xlabel('Date')

plt.legend()
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(data[['Date']], data[['New Cases']])
# resl = data.data([[11]],[[1249]])
predict = model.predict([[22]])
print(int(predict)," New Cases")
p2 = model.fit(data[['Date']], data[['Death']])
predict_death = model.predict([[22]])
print(int(predict_death)," New Deaths")