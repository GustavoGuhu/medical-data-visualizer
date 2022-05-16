import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight'] /( (df['height']/100) * (df['height']/100))
df['overweight'] = 0
df.loc[df['BMI'] >25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

#df['active'] =  df['active'].map({False:1, True:0})

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.drop(columns=['id','age','sex','height','weight','ap_hi','ap_lo', 'BMI'])
    df_cat = df_cat.melt(id_vars='cardio') #id_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.sort_values(by='cardio')

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x='variable', hue = 'value', data=df_cat, kind='count', col = 'cardio',  
                order= ['active','alco','cholesterol','gluc','overweight','smoke'])

    fig.set_ylabels("total")

    fig = fig.figure

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

#print(df.shape)

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df
    df_heat = df_heat.drop(df_heat[df_heat['ap_lo'] >= df_heat['ap_hi']].index)
    df_heat = df_heat.drop(df_heat[(df_heat['height'] <= df_heat['height'].quantile(0.025))].index)
    df_heat = df_heat.drop(df_heat[(df_heat['height'] >= df_heat['height'].quantile(0.975))].index)
    df_heat = df_heat.drop(df_heat[(df_heat['weight'] <= df_heat['weight'].quantile(0.025))].index)
    df_heat = df_heat.drop(df_heat[(df_heat['weight'] >= df_heat['weight'].quantile(0.975))].index)


    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(8, 8))

    sns.set(font_scale=0.6)

    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, mask = mask, annot=True, fmt='.1f', center = 0.08, vmax = 0.3, cbar = True, square=True)

    
    fig = fig.figure

    # Do not modify the next two lines
    fig.figure.savefig('heatmap.png')
    return fig
