# state_mentions_race.py

import pandas as pd
import plotly.express as px
import os

# Simulated dataset (replace with real time-series mention data if available)
data = {
    'state': ['Texas', 'Florida', 'California', 'New York', 'Ohio', 'Montana'] * 3,
    'date': ['2024-01', '2024-01', '2024-01', '2024-01', '2024-01', '2024-01',
             '2024-02', '2024-02', '2024-02', '2024-02', '2024-02', '2024-02',
             '2024-03', '2024-03', '2024-03', '2024-03', '2024-03', '2024-03'],
    'mentions': [100, 80, 90, 60, 40, 30, 120, 95, 100, 70, 50, 40, 140, 105, 120, 80, 60, 45]
}

df = pd.DataFrame(data)

# Bar chart race using animation_frame
fig = px.bar(
    df,
    x='mentions',
    y='state',
    color='state',
    orientation='h',
    animation_frame='date',
    range_x=[0, 160],
    title='📈 State Mentions Over Time (Bar Chart Race)',
    labels={'mentions': 'Mentions', 'state': 'State'},
    height=600
)

# Clean up layout
fig.update_layout(
    font=dict(size=14),
    title=dict(font=dict(size=24)),
    margin=dict(l=20, r=20, t=60, b=20),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    showlegend=False
)

# Save interactive animation
output_dir = "../website-source/plots"
os.makedirs(output_dir, exist_ok=True)
fig.write_html(os.path.join(output_dir, "state_mentions_race.html"))

print("✅ Animation saved to:", os.path.join(output_dir, "state_mentions_race.html"))