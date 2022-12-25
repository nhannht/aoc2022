#!/usr/bin/env python
# read tokei.json
#
import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns
data= json.load(open('tokei.json'))
df = pd.DataFrame(data)
#%%
# extract file name and code from data['Python']['reports']
#%%
# extract file name and code from data['Python']['reports']
reports = df['Python']['reports']
#%%
file_and_code = []
for report in reports:
    file_and_code.append([report['name'],report['stats']['code']])
#%%
file_and_code_df = pd.DataFrame(file_and_code,columns=['file','code'])

#%%
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="code", y="file", data=file_and_code_df)
#%% Save ax to file
fig = ax.get_figure()
fig.savefig('tokei.png')

#%%
