import pandas as pd
import numpy as np
df = pd.read_csv('world_happiness_report_alter.csv')
# print(df['Regional indicator'].unique()), wanted each one on a new line so used code below instead
print(df['Regional_Indicator'].value_counts())
print('--'*30)

def RegCalc(column):
        return(df.groupby('Regional_Indicator', as_index=False).agg({column:['min','max','mean']}).round(3))
print('--'*30)
#not sure if its bad practice to use spaces between apostrophes eg ' while ' or to use + ' ' +
#struggled with this one to figure out how to return a single value and its corresponding country 
#ended up with with code below
def CountryCalc(column):
        var=df.iloc[df[column].idxmax()]
        var1=df.iloc[df[column].idxmin()]
        return(var[0] +' scored highest in '+ column +' while '+ var1[0] +' scored lowest in '+ column)
print('--'*30)
print(RegCalc('Ladder_Score'))
print('--'*30)
print(RegCalc('E_Log_GDPper_Capita'))
print('--'*30)
print(CountryCalc('Ladder_Score'))
print(CountryCalc('Social_Support'))

# Want to print correlation between Ladder_Score and the rest of the relevant columns
#Method one: 
        #df.corr(method='pearson')
        #the whole dataframe against each other, but i only want Ladder_score against the selected columns
#Method two: 
        #corr_df2 = df.iloc[:,6:]
        #corr_df = df['Ladder_Score']
        #correlation=corr_df.corrwith(corr_df2, axis = 1) tried axis=0 also
        #print(correlation)
        #AttributeError: 'Series' object has no attribute 'corrwith'
#Method 3
        #correlation=df['Ladder_Score'].corr(df[6:], method='pearson') 
        #ValueError: operands could not be broadcast together with shapes (143,) (143,20)
#Method 4
        #df_for_corr = df.iloc[:,6:] + df.iloc[:,13:] 
        #print(df_for_corr.corrwith(df['Ladder_Score']))
        #returned everything as NaN in .corrwith calc
print('--'*30)
df_for_corr = df.iloc[:,6:]
pearson_scores_nan = df_for_corr.corrwith(df['Ladder_Score'])
pearson_scores=pearson_scores_nan.dropna()
print('Correlation coefficient of Ladder Score with columns below:\n', pearson_scores)