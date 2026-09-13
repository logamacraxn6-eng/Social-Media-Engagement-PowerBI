
# Social Media Engagement Analysis

import pandas as pd
df=pd.read_csv('social_media_engagement.csv',parse_dates=['Post_Date'])
df.head()
df.groupby('Platform')['Engagement_Rate'].mean().sort_values(ascending=False)

df.groupby('Content_Type')['Engagement_Rate'].mean().sort_values(ascending=False)

df.groupby('Time_Slot',observed=True)['Engagement_Rate'].mean().sort_values(ascending=False)
