import abc
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
    df_cardio_0 = df_cat[df_cat['cardio']==0]
    df_cardio_1 = df_cat[df_cat['cardio']==1]


    # Draw the catplot with 'sns.catplot()'
    
    fig = sns.catplot(x='variable', hue = 'value', data=df_cardio_0, kind='count',  
                order= ['active','alco','cholesterol','gluc','overweight','smoke']
                )
    
    fig = sns.catplot(x='variable', hue = 'value', data=df_cardio_1, kind='count',  
                order= ['active','alco','cholesterol','gluc','overweight','smoke']
                )


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
#def draw_heat_map():
    # Clean the data
    #df_heat = None

    # Calculate the correlation matrix
    #corr = None

    # Generate a mask for the upper triangle
    #mask = None



    # Set up the matplotlib figure
    #fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    #fig.savefig('heatmap.png')
    #return fig
