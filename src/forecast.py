from datetime import datetime
import pandas as pd

from .models import Model


class Forecast:
    """Takes model any e.g arima, fbprophet and forecast data."""

    def __init__(self, ts_model: Model, forecast_end_year: int = 2030) -> None:
        self.model: Model = ts_model
        self.forecast_end_year: int = forecast_end_year

    @property
    def historical_data(self) -> pd.DataFrame:
        """Return historical data in pandas dataframe format."""
        return self.model.time_series_df

    @property
    def predicted_data(self) -> pd.DataFrame:
        """Return forecasted data."""
        forecast = self.model.forecast(self.forecast_end_year)
        forecast_end: pd.Timestamp = pd.Timestamp(
            datetime.strptime(str(self.forecast_end_year+1), '%Y'))
        future_years = pd.date_range(
            start=self.model.time_series_df.index[-1], end=forecast_end, freq='Y')
        predicted_df = pd.DataFrame(index=future_years[1:], data={
                                    'value': list(forecast)})
        return predicted_df

    @property
    def combined_df(self) -> pd.DataFrame:
        """Return historical+forecasted data as one dataframe."""
        return pd.concat([self.historical_data, self.predicted_data], axis=0, join="inner")
