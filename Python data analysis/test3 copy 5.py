import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import plotly.express as px

# Load your Excel file
df = pd.read_excel('C:\\Data\\2025-06-04\\Raster Scan time.xlsx')
df.columns = ['Time_s', 'Captures', 'IntTime_ms', 'DarkSub', 'Average', 'TimeBetween_ms']

# Convert to seconds
df['IntTime_s'] = df['IntTime_ms'] / 1000
df['TimeBetween_s'] = df['TimeBetween_ms'] / 1000
df['TimePerCapture'] = df['Time_s'] / df['Captures']

# Define features and target
X = df[['IntTime_s', 'DarkSub', 'Average', 'TimeBetween_s']]
y = df['TimePerCapture']

# Fit regression model with interaction terms
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
model = make_pipeline(poly, LinearRegression())
model.fit(X, y)

# Predict
df['Predicted_TimePerCapture'] = model.predict(X)

# Interactive scatter plot
fig = px.scatter(
    df,
    x='TimePerCapture',
    y='Predicted_TimePerCapture',
    hover_data={
        'IntTime_s': True,
        'DarkSub': True,
        'Average': True,
        'TimeBetween_s': True,
        'TimePerCapture': ':.4f',
        'Predicted_TimePerCapture': ':.4f'
    },
    labels={
        'TimePerCapture': 'Actual Time per Capture (s)',
        'Predicted_TimePerCapture': 'Predicted Time per Capture (s)'
    },
    title="Actual vs Predicted Time per Capture"
)

# Add 1:1 line
fig.add_shape(
    type="line",
    x0=df['TimePerCapture'].min(), y0=df['TimePerCapture'].min(),
    x1=df['TimePerCapture'].max(), y1=df['TimePerCapture'].max(),
    line=dict(color="red", dash="dash")
)

fig.update_layout(width=700, height=600)
fig.show()