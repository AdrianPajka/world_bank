import pytest 

from src.world_bank import WorldBank, BadCountryCodeError

def test_ivalid_country_code():
    with pytest.raises(BadCountryCodeError):
        assert WorldBank(time_series_code='test', country='test')
        
        
