from datetime import date

from src.forecast import Forecast
from src.models import ArimaModel
from src.save_time_series import save_data
from src.time_series import TimeSeries
from src.world_bank import WorldBank


def forecast_and_save(country: str, time_series_code: str, forecast_year):
    """Forecast tiem series from World bank API and save data to csv."""
    filename:str = date.today().strftime("%b-%d-%Y")
    
    wb = WorldBank(time_series_code=time_series_code, country = country)
    ts = TimeSeries(wb)
    arima = ArimaModel(ts) # you can change it to PbprophetModel if it's implemented with schema
    f = Forecast(arima)
    
    stages = ('historical', 'predicted', 'combined')
    for stage, df in zip(stages,(f.historical_data, f.predicted_data, f.combined_df)):
        print('Saving', stage,f' as {stage+filename}.csv')
        save_data(df, stage+filename)
        


if __name__ == '__main__':
    forecast_and_save('afg', 'NY.GDP.MKTP.CN', 2030)