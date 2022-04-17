import requests
import pandas as pd
import numpy as np
from typing import List

INSTRUMENT_TYPES = ['SPOT', 'MARGIN', 'SWAP']
INSTRUMENTS_COLUMNS = dict(
    instType=str,
    instId=str,
    uly=str,
    category=int,
    baseCcy=str,
    quoteCcy=str,
    settleCcy=str,
    ctVal=float,
    ctMult=float,
    ctValCcy=str,
    optType=str,
    stk=float,
    listTime=pd.datetime,
    expTime=pd.datetime,
    lever=float,
    tickSz=float,
    lotSz=float,
    minSz=float,
    ctType=str,
    alias=str,
    state=str
)

class OKXParser:

    headers = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }

    def __init__(self, url='https://www.okx.com'):
        """
        Class for parsing OKX data via REST API v5
        :param url: REST API URL
        """
        self.url = url

    def get_instruments(self, instType, uly=None, instId=None) -> pd.DataFrame:
        """
        Get all the instruments by instrument type

        `GET /api/v5/public/instruments`

        :param instType: Instrument type. Currently supported: [SPOT, SWAP, MARGIN]
        :param uly: Underlying, only applicable to FUTURES/SWAP/OPTION
        :param instId: Instrument ID (not required)
        :return: pd.DataFrame
        """
        if instType not in INSTRUMENT_TYPES:
            raise ValueError(f'{instType} is not a type of an instrument. Please use one of {INSTRUMENT_TYPES}')
        command = '/api/v5/public/instruments'
        params = dict(
            instType=instType,
            uly=uly,
            instId=instId
        )
        result = requests.get(self.url + command, params=params, headers=self.headers)
        result = pd.DataFrame(result.json()['data'])
        if set(result.columns) != set(INSTRUMENTS_COLUMNS.keys()):
            raise ValueError('Please fill underlying asset as uly parameter')
        # Pre-processing data
        result = result.replace('', np.nan)
        result['category'] = result['category'].astype(int)
        float_cols = ['ctVal', 'ctMult', 'stk', 'lever', 'tickSz', 'lotSz', 'minSz']
        result[float_cols] = result[float_cols].astype(float)
        result['listTime'] = pd.to_datetime(result['listTime'], unit='ms')
        result['expTime'] = pd.to_datetime(result['expTime'], unit='ms')
        return result[INSTRUMENTS_COLUMNS.keys()]

    def preprocess(self, df, cols):
        result = df.replace('', np.nan)
        for col in df.columns:
            if type(cols[col]) == pd.datetime:
                result[col] = pd.to_datetime(result[col], unit='ms')
            else:
                result[col] = result[col].astype(cols[col])
        return result
