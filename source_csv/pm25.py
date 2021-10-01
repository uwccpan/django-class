import pandas as pd

url = '/Users/jonpan/Downloads/aqx_p_322_20210930105441.csv'

def get_pm25():
    df = pd.read_csv(url).dropna()
    columns = ['SiteName', 'County', 'Concentration']
    datas = sorted(df[columns].values.tolist(), key=lambda x:x[-1], reverse = True)
    return columns, datas

