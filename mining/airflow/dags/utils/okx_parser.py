import requests
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List
from collections import OrderedDict

INSTRUMENT_TYPES = ['SPOT', 'MARGIN', 'SWAP']
INSTRUMENTS_COLUMNS = OrderedDict(
    inst_type=str,
    inst_id=str,
    uly=str,
    category=int,
    base_ccy=str,
    quote_ccy=str,
    settle_ccy=str,
    ct_val=float,
    ct_mult=float,
    ct_val_ccy=str,
    opt_type=str,
    stk=float,
    list_time=datetime,
    exp_time=datetime,
    lever=float,
    tick_sz=float,
    lot_sz=float,
    min_sz=float,
    ct_type=str,
    alias=str,
    state=str
)

INSTRUMENTS_COLUMNS_MAPPER = dict(
    instType='inst_type',
    instId='inst_id',
    uly='uly',
    category='category',
    baseCcy='base_ccy',
    quoteCcy='quote_ccy',
    settleCcy='settle_ccy',
    ctVal='ct_val',
    ctMult='ct_mult',
    ctValCcy='ct_val_ccy',
    optType='opt_type',
    stk='stk',
    listTime='list_time',
    expTime='exp_time',
    lever='lever',
    tickSz='tick_sz',
    lotSz='lot_sz',
    minSz='min_sz',
    ctType='ct_type',
    alias='alias',
    state='state'
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
        if set(result.columns) != set(INSTRUMENTS_COLUMNS_MAPPER.keys()):
            raise ValueError('Please fill underlying asset as uly parameter')
        result = result.rename(mapper=INSTRUMENTS_COLUMNS_MAPPER, axis='columns')
        return result[INSTRUMENTS_COLUMNS.keys()]

    def preprocess(self, df, cols):
        result = df.replace('', np.nan)
        for col in df.columns:
            if cols[col] == datetime:
                result[col] = pd.to_datetime(result[col], unit='ms')
            else:
                result[col] = result[col].astype(cols[col])
        return result
