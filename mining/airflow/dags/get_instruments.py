from airflow import DAG
from airflow.decorators import task
from airflow.models import variable, connection
import logging
import pendulum
from utils.okx_parser import OKXParser, INSTRUMENTS_COLUMNS

postgres = connection.Connection(conn_id='MY_PROD_DATABASE')

log = logging.getLogger(__name__)

parser = OKXParser()

with DAG(
        dag_id='get_instruments',
        schedule_interval='0 0 * * *',
        start_date=pendulum.datetime(2022, 4, 17, tz="UTC"),
        catchup=False,
        tags=['mining'],
) as dag:
    @task(task_id="get_SPOT")
    def get_spot():
        instruments = parser.get_instruments('SPOT')
        instruments = parser.preprocess(instruments, INSTRUMENTS_COLUMNS)
        instruments.to_sql(name='instruments_spot', con=postgres, schema='crypto_trade', if_exists='append')
        return 'Success'

    get_spot()



# {
#     'conf': <***.configuration.AirflowConfigParser object at 0xffff84769950>,
#     'dag': <DAG: example_python_operator>,
#     'dag_run': <DagRun example_python_operator @ 2022-04-17 20:21:57.629598+00:00: manual__2022-04-17T20:21:57.629598+00:00, externally triggered: True>,
#     'data_interval_end': DateTime(2022, 4, 17, 20, 21, 57, 629598, tzinfo=Timezone('UTC')),
#     'data_interval_start': DateTime(2022, 4, 17, 20, 21, 57, 629598, tzinfo=Timezone('UTC')),
#     'ds_nodash': '20220417',
#     'execution_date': <Proxy at 0xffff8226d050 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'execution_date', DateTime(2022, 4, 17, 20, 21, 57, 629598, tzinfo=Timezone('UTC')))>,
#     'inlets': [],
#     'logical_date': DateTime(2022, 4, 17, 20, 21, 57, 629598, tzinfo=Timezone('UTC')),
#     'macros': <module '***.macros' from '/home/***/.local/lib/python3.7/site-packages/***/macros/__init__.py'>,
#     'next_ds': <Proxy at 0xffff82214e10 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'next_ds', '2022-04-17')>,
#     'next_ds_nodash': <Proxy at 0xffff82214f50 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'next_ds_nodash', '20220417')>,
#     'next_execution_date': <Proxy at 0xffff8221e320 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'next_execution_date', DateTime(2022, 4, 17, 20, 21, 57, 629598, tzinfo=Timezone('UTC')))>,
#     'outlets': [],
#     'params': {},
#     'prev_data_interval_start_success': None,
#     'prev_data_interval_end_success': None,
#     'prev_ds': <Proxy at 0xffff8221ed70 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'prev_ds', '2022-04-17')>,
#     'prev_ds_nodash': <Proxy at 0xffff8221eeb0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'prev_ds_nodash', '20220417')>,
#     'prev_execution_date': <Proxy at 0xffff8221ee60 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'prev_execution_date', DateTime(2022, 4, 17, 20, 21, 57, 629598, tzinfo=Timezone('UTC')))>, 'prev_execution_date_success': <Proxy at 0xffff8221eb40 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'prev_execution_date_success', None)>,
#     'prev_start_date_success': None,
#     'run_id': 'manual__2022-04-17T20:21:57.629598+00:00',
#     'task': <Task(_PythonDecoratedOperator): print_the_context>,
#     'task_instance': <TaskInstance: example_python_operator.print_the_context manual__2022-04-17T20:21:57.629598+00:00 [running]>,
#     'task_instance_key_str': 'example_python_operator__print_the_context__20220417',
#     'test_mode': False,
#     'ti': <TaskInstance: example_python_operator.print_the_context manual__2022-04-17T20:21:57.629598+00:00 [running]>,
#     'tomorrow_ds': <Proxy at 0xffff8221ea50 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'tomorrow_ds', '2022-04-18')>,
#     'tomorrow_ds_nodash': <Proxy at 0xffff8221ebe0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'tomorrow_ds_nodash', '20220418')>,
#     'ts': '2022-04-17T20:21:57.629598+00:00',
#     'ts_nodash': '20220417T202157',
#     'ts_nodash_with_tz': '20220417T202157.629598+0000',
#     'var': {'json': None, 'value': None},
#     'conn': None,
#     'yesterday_ds': <Proxy at 0xffff8221ec30 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'yesterday_ds', '2022-04-16')>,
#     'yesterday_ds_nodash': <Proxy at 0xffff8221e0f0 with factory functools.partial(<function lazy_mapping_from_context.<locals>._deprecated_proxy_factory at 0xffff82204830>, 'yesterday_ds_nodash', '20220416')>,
#     'templates_dict': None
# }