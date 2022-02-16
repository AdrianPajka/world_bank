from typing import ClassVar, Optional

import requests
import pydantic


class BadCountryCodeError(Exception):
    """Raise error when provided country code is invalid."""
    pass


class WorldBank(pydantic.BaseModel):
    """This class is like mini-package for worldbank api, it downloads data and validates them.
    
    time_series_code [str] - e.g. NY.GDP.MKTP.CN
    country          [str] - country code e.g. AFG
    
    """

    API_URL: ClassVar[str] = 'https://api.worldbank.org/v2/country'
    time_series_code: str
    country: Optional[str] = 'all'

    @pydantic.validator("country")
    @classmethod
    def is_country_valid(cls, value):
        country_codes = ['all', 'AFG', 'BDI', 'BFA', 'CAF', 'COD', 'ERI', 'ETH', 'GIN', 'GMB', 'GNB', 'LBR', 'MDG',
                         'MLI', 'MOZ', 'MWI', 'NER', 'PRK', 'RWA', 'SDN', 'SLE', 'SOM', 'SSD', 'SYR', 'TCD', 'TGO', 'UGA', 'YEM']
        if value.upper() not in country_codes:
            raise BadCountryCodeError(
                f'Country code does not match codes in the list {country_codes}')
        return value

    @property
    def data_xml(self):
        return self.get_data_from_api()

    def get_data_from_api(self) -> bytes:
        """Get data in xml format."""
        payload = {'frequency': 'Y', 'format': 'xml'}

        try:
            r = requests.get(
                f'{self.API_URL}/{self.country}/indicator/{self.time_series_code}', params=payload)

        except requests.exceptions.Timeout:
            print('Timeout, please check firewalls')

        except requests.exceptions.TooManyRedirects:
            print(
                'The provided url API could has been changed or something is wrong with the url')

        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        else:
            return r.content
