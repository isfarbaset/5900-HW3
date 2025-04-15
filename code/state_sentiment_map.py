# state_sentiment_map.py

import pandas as pd
import plotly.express as px
import os

# Sample sentiment data by state (replace with your own)
data = {
    'state': ['Montana', 'New Mexico', 'Iowa', 'Ohio', 'Florida', 'California', 'Texas', 'New York'],
    'abbr': ['MT', 'NM', 'IA', 'OH', 'FL', 'CA', 'TX', 'NY'],
    'sentiment': [0.21, 0.19, -0.09, -0.08, -0.07, 0.05, 0.03, 0.02]
}

df = pd.DataFrame(data)

# Create the figure
fig = px.choropleth(
    df,
    locations='abbr',
    locationmode='USA-states',
    color='sentiment',
    scope='usa',
    color_continuous_scale=px.colors.diverging.RdYlGn,
    range_color=[-0.1, 0.25],
    hover_name='state',
    labels={'sentiment': 'Average Sentiment'},
    title='Average Sentiment Score by State'
)

# Customize layout
fig.update_layout(
    geo=dict(bgcolor='rgba(0,0,0,0)'),
    font=dict(size=14),
    title=dict(font=dict(size=22)),
    margin=dict(l=20, r=20, t=50, b=20),
    coloraxis_colorbar=dict(title="Sentiment Score"),
)

# Save output to HTML for embedding
output_dir = "../website-source/plots"
os.makedirs(output_dir, exist_ok=True)
fig.write_html(os.path.join(output_dir, "state_sentiment_map.html"))

print("✅ Interactive map saved to:", os.path.join(output_dir, "state_sentiment_map.html"))