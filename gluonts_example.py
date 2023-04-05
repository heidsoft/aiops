import pandas as pd
import matplotlib.pyplot as plt
from gluonts.dataset.pandas import PandasDataset
from gluonts.dataset.split import split
from gluonts.mx import DeepAREstimator, Trainer

# Load data from a CSV file into a PandasDataset
df = pd.read_csv(
    "https://raw.githubusercontent.com/AileenNielsen/"
    "TimeSeriesAnalysisWithPython/master/data/AirPassengers.csv",
    index_col=0,
    parse_dates=True,
)
dataset = PandasDataset(df, target="#Passengers")

# Train a DeepAR model on all data but the last 36 months
training_data, test_gen = split(dataset, offset=-36)
model = DeepAREstimator(
    prediction_length=12, freq="M", trainer=Trainer(epochs=5)
).train(training_data)

# Generate test instances and predictions for them
test_data = test_gen.generate_instances(prediction_length=12, windows=3)
forecasts = list(model.predict(test_data.input))

# Plot predictions
df["#Passengers"].plot(color="black")
for forecast, color in zip(forecasts, ["green", "blue", "purple"]):
    forecast.plot(color=f"tab:{color}")
plt.legend(["True values"], loc="upper left", fontsize="xx-large")
plt.show()