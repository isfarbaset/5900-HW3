# word_frequency_plot.py

import pandas as pd
import numpy as np
import plotly.express as px
import os

# Create directory structure if it doesn't exist
plot_dir = "../website-source/plots"
os.makedirs(plot_dir, exist_ok=True)

# Create a dataframe with the word frequency data
words = ['people', 'state', 'one', 'new', 'time', 'think', 'go', 'even', 'also', 
         'texas', 'florida', 'california', 'please', 'many', 'want']
counts = [100, 85, 75, 70, 65, 60, 55, 50, 48, 45, 42, 40, 38, 35, 33]

# Create DataFrame and sort by frequency
word_data = pd.DataFrame({'word': words, 'count': counts})
word_data = word_data.sort_values('count', ascending=False).reset_index(drop=True)

# Add a column to identify state names
word_data['is_state'] = word_data['word'].apply(lambda x: 'State' if x.lower() in ['texas', 'florida', 'california'] else 'General term')

# Create interactive bar chart
fig = px.bar(
    word_data, 
    y='word', 
    x='count',
    color='is_state',
    color_discrete_map={'State': '#f6ad55', 'General term': '#4299e1'},
    title='Most Common Words on State Posts',
    labels={'count': 'Frequency', 'word': ''},
    height=600,
    width=900
)

# Customize layout
fig.update_layout(
    font=dict(size=14),
    title=dict(font=dict(size=24)),
    xaxis=dict(title=dict(font=dict(size=16))),
    yaxis=dict(title=dict(font=dict(size=16))),
    legend_title_text='Word Type',
    margin=dict(l=20, r=20, t=60, b=20),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
)

# Add grid lines only for x-axis
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
fig.update_yaxes(showgrid=False)

# Save the interactive plot
fig.write_html(os.path.join(plot_dir, "word_frequency.html"))

print(f"Plot saved to {os.path.join(plot_dir, 'word_frequency.html')}")