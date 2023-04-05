import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv"
df = pd.read_csv(url, header=0, index_col=0)

df[:200].plot(figsize=(12, 5), linewidth=2)
plt.grid()
plt.legend(["observations"])
plt.show()

