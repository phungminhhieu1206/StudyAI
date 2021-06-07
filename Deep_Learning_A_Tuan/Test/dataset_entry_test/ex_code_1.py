import pandas as pd
import matplotlib.pyplot as plt

# 1. Load file csv bằng pandas
df = pd.read_csv('C:\\Users\\phung\\Desktop\\dataset_entry_test\\data_linear.csv')
print(df)

# 2. Vẽ đồ thị quan hệ diện tích, giá nhà bằng matplotlib
plt.plot(df['Diện tích'], df['Giá'], 'ro')
plt.xlabel("Diện tích")
plt.ylabel("Giá")
plt.show()
