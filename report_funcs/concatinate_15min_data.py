# Functions for concaninating  and cleaning the 15min and dayparts data

import pandas as pd
from .data_cleaning_utils import getCity

# 15min daily version 3
def concat15min(path, stationReferenceDict,geocolumnname, chartorderdict):

    try:
        spec15min = pd.read_excel(path+'\\Spectrum News - 15 Mins.xlsx',sheet_name='Live+Same Day, TV Households',header = 8,skipfooter=8).ffill()
    except Exception as e:
        print(e)
        print('There was an issue locating the spectrum 15minute file, this file is critical for the report to generate. ')
    
    try:
        bf15min = pd.read_excel(path+'\\SN Buffalo - 15 Mins.xlsx',sheet_name='Live+Same Day, TV Households',header = 8,skipfooter=8).ffill()
        min15df = pd.concat([spec15min,bf15min])
    except Exception as e: 
        print('There was an issue concatinating the buffalo 15min file and the spectrum 15min file, this is not critical for the report, but means the buffalo DMA will not be created.')
        min15df = spec15min
        
    # Check for nan values
    if ' ' in min15df['RTG % (X.X)'].unique() or min15df['RTG % (X.X)'].isnull().values.any():
        print(f'WARNING!! WARNING!!! Missing RTG found in 15min File! \nPath:\n{path}')  
    min15df['RTG % (X.X)'] = min15df['RTG % (X.X)'].fillna(0)
    min15df['RTG % (X.X)'] = min15df['RTG % (X.X)'].replace(' ', 0)

    # Strip White space
    print('Stripping white space for columns')
    min15df = min15df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


    # TEMPORRARY UNTIL SOURCE IS FIXED - Remove s1df and s1mk from all markets, re add them back where they're regions are
    dallasdf = min15df[(min15df['Viewing Source']== 'S1DF') & (min15df[geocolumnname]=='Dallas-Ft. Worth')]
    milwakdf = min15df[(min15df['Viewing Source']== 'S1MK') & (min15df[geocolumnname]=='Milwaukee')]
    min15df = min15df[(min15df['Viewing Source']!= 'S1DF') & (min15df['Viewing Source']!='S1MK')]
    min15df = pd.concat([min15df,dallasdf,milwakdf]).reset_index()
    

    dropped_dmas = ['Greensboro', 'Raleigh', 'Columbus', 'Milwaukee', 'Austin', 'San Antonio']
    min15df = min15df[~min15df[geocolumnname].isin(dropped_dmas)] 
    print(min15df[geocolumnname].unique())

    # Add station column
    min15df['Station'] = min15df['Viewing Source'].apply(lambda x: stationReferenceDict[x])

    # Add DMA specific column 
    min15df['DMA'] = min15df[geocolumnname].apply(lambda x: getCity(x))

    # REMNOVING THE ORDER COLUMN AS IT IS NEVER USED IN THE CHART, Apparentkly seaborn is smart enough to properly order the x-axis 
    # Need to properly order this dataframe for seaborn to use
    #print('Applying order...')
    min15df['Order'] = min15df['Time'].apply(lambda x: chartorderdict[x])
    # min15df = min15df.sort_values('Order', axis = 'columns')


    # Drop unneccesary columns, rename RTG column
    #print(min15df)
    min15df = min15df.drop(['Affil.','Custom Range','Daypart','Demo',geocolumnname,'index','Indicator','Indicator ','Metrics'], axis = 1, errors='ignore').rename(columns={'RTG % (X.X)':'RTG'})
    #print(min15df.columns)


    return min15df