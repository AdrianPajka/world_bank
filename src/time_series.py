import pandas as pd

from .world_bank import WorldBank


class TimeSeries:
    """Preprare time series object for world bank api data.

    world_bank [WorldBank] - world bank object can contain different formats

    IMPORTANT: For now, the class handles only xml format in bytes, but can be easily extended to others
    
    """

    def __init__(self, world_bank: WorldBank) -> None:
        self.df: pd.DataFrame = pd.read_xml(world_bank.data_xml)

    def create_time_series_df(self) -> pd.DataFrame:
        """Clean data - drop NaN - and return dataframe with date as indexes."""

        self.df.date = self.df.date.apply(lambda date: str(date))
        self.df.date = pd.to_datetime(self.df.date)
        # I understand there is a lot of methods for missing data, but I will simplify it :)
        self.df = self.df[self.df['value'].notnull()]

        ts_df = self.df[['date', 'value']]
        ts_df.set_index('date', inplace=True)
        ts_df = ts_df.sort_values(by='date')

        return ts_df

    def __check_stationarity(self, data):
        """Can be implemented in the future."""
        pass
