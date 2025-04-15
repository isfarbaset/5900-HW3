# state_sentiment_map.py

import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

# Set default renderer for Jupyter / embedding use
pio.renderers.default = 'iframe_connected'

# Sentiment scores by state
sentiment_by_state = {
    'AL': -0.05, 'AK': 0.10, 'AZ': -0.08, 'AR': 0.00, 'CA': -0.09, 'CO': 0.18, 'CT': 0.00, 'DE': 0.02,
    'FL': -0.10, 'GA': 0.00, 'HI': 0.08, 'ID': 0.20, 'IL': 0.05, 'IN': -0.02, 'IA': -0.08, 'KS': 0.03,
    'KY': -0.01, 'LA': -0.07, 'ME': 0.15, 'MD': 0.02, 'MA': -0.09, 'MI': 0.02, 'MN': 0.01, 'MS': -0.07,
    'MO': -0.02, 'MT': 0.21, 'NE': 0.06, 'NV': 0.00, 'NH': 0.05, 'NJ': -0.04, 'NM': 0.20, 'NY': 0.08,
    'NC': 0.00, 'ND': 0.07, 'OH': -0.08, 'OK': -0.06, 'OR': 0.09, 'PA': -0.03, 'RI': 0.00, 'SC': -0.02,
    'SD': 0.06, 'TN': -0.07, 'TX': -0.06, 'UT': 0.18, 'VT': 0.14, 'VA': 0.00, 'WA': 0.08, 'WV': -0.09,
    'WI': 0.03, 'WY': 0.10
}

# Full state names
state_names = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Convert to DataFrame
df = pd.DataFrame({
    "code": list(sentiment_by_state.keys()),
    "state": [state_names[code] for code in sentiment_by_state.keys()],
    "sentiment": list(sentiment_by_state.values())
})

# Generate the map
fig = px.choropleth(
    df,
    locations="code",
    locationmode="USA-states",
    color="sentiment",
    color_continuous_scale=[
        "#d73027", "#f46d43", "#fee08b", "#d9ef8b", "#1a9850", '#0000FF'
    ],
    range_color=(-0.1, 0.2),
    scope="usa",
    hover_name="state",
    labels={"sentiment": "Sentiment"}
)

# Customize layout
fig.update_layout(
    title_text="Reddit Sentiment by U.S. State (Extracted from Map)",
    geo=dict(lakecolor='white'),
)

# Save as HTML for Quarto embedding
output_dir = "../website-source/plots"
os.makedirs(output_dir, exist_ok=True)
fig.write_html(os.path.join(output_dir, "state_sentiment_map.html"))

print("✅ Sentiment map saved to:", os.path.join(output_dir, "state_sentiment_map.html"))

# Optional: Show it during dev
fig.show()