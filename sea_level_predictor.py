import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.figure(figsize=(14,8))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.xticks(range(1850,2100,25))

    # Create first line of best fit
    [slope, intercept, rvalue, pvalue, stderr] = linregress(df['Year'],
                                                            df['CSIRO Adjusted Sea Level'])
    df_predicted = pd.DataFrame()
    df_predicted['Year'] = range(1880,2051)
    df_predicted['Predicted Sea Levels'] = (slope*df_predicted['Year']) + intercept
    plt.plot(df_predicted['Year'],df_predicted['Predicted Sea Levels'])

    # Create second line of best fit
    [slope_2k,intercept_2k,
     rvalue_2k, pvalue_2k, stderr_2k] = linregress(df.loc[df['Year']>1999, 'Year'],
                 df.loc[df['Year']>1999, 'CSIRO Adjusted Sea Level'])
    df_predicted_2k = pd.DataFrame()
    df_predicted_2k['Year'] = range(2000,2051)
    df_predicted_2k['Predicted Sea Levels'] = (slope_2k*df_predicted_2k['Year']) + intercept_2k
    plt.plot(df_predicted_2k['Year'],df_predicted_2k['Predicted Sea Levels'])
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()