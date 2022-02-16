from abc import ABC, abstractmethod

from pmdarima.arima import auto_arima

from .time_series import TimeSeries


class Model(ABC):

    @abstractmethod
    def create_model(self):
        pass

    @abstractmethod
    def forecast(self, forecast_year):
        pass


class ArimaModel(Model):
    """The simplified arima model, uses the whole data and auto_arima

    Args:
        time_series [TimeSeries]: instance of TimeSeries

    """

    def __init__(self, time_series: TimeSeries):
        self.time_series_df = time_series.create_time_series_df()
        self.last_year = self.time_series_df.last_valid_index().year

    def __arima(self):
        # todo:Instead of using auto_arima implement in the future model mechanism for ARIMA
        pass

    def __sarimax(self):
        # todo:Instead of using auto_arima implement in the future model mechanism for ARIMA
        pass

    def create_model(self):
        """Return a model. 

        IMPORTANT: In the future it should only provides info which model really should be use

        auto_arima helps to identify the most optimal parameters for an ARIMA model and returns a fitted ARIMA model.

        """

        model = auto_arima(self.time_series_df.value,
                           max_order=None,
                           stepwise=True,
                           trace=True,
                           error_action='ignore',
                           suppress_warnings=True)

        return model

    def forecast(self, forecast_year):
        """Forecast time series data."""

        num_periods: int = forecast_year - self.last_year
        model = self.create_model()

        forecast = model.predict(n_periods=num_periods)

        return forecast


class FbProphet(Model):
    # I had a problem with installing the package on my linux and still didn't found the solution for this
    def create_model(self):
        pass

    def forecast(self, forecast_year):
        pass
