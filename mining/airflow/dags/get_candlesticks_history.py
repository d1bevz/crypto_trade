from airflow import DAG
from airflow.decorators import task
from airflow.models import variable, connection
from airflow.hooks.base import BaseHook
from airflow.utils import db
from sqlalchemy import create_engine
import logging
import pendulum, datetime, time
from utils.okx_parser import OKXParser, CANDLESTICKS_HISTORY_COLUMNS_DT

log = logging.getLogger(__name__)

parser = OKXParser()
postgres = BaseHook.get_connection('MY_PROD_DATABASE')
postgres = create_engine(postgres.get_uri())

instruments = [
    'BTC-USDT', 'ETH-USDT', 'OKB-USDT', 'OKT-USDT', 'LTC-USDT',
    'DOT-USDT', 'DOGE-USDT', 'LUNA-USDT', 'PEOPLE-USDT',
    'SHIB-USDT', 'TONCOIN-USDT', 'NEAR-USDT', 'TRX-USDT',
    'WAVES-USDT'
]


with DAG(
        dag_id='get_candlesticks_history',
        schedule_interval='0 * * * *',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        catchup=False,
        tags=['mining', 'public_data']
) as dag:

    for instrument in instruments:
        @task(task_id=f"get_{instrument}")
        def get_candlesticks_history(instrument_id, ts=None):
            ts = int(time.mktime(datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%S.%f%z').timetuple()) * 1000)
            print(instrument_id, ts)
            candlesticks_history = parser.get_candlesticks_history(instrument_id, after=ts, limit=60)
            candlesticks_history = parser.preprocess(candlesticks_history, CANDLESTICKS_HISTORY_COLUMNS_DT)
            candlesticks_history.to_sql(name='candlesticks_raw', con=postgres, schema='market_data', if_exists='append', index=False)
            return 'Success'

        get_candlesticks_history(instrument)
