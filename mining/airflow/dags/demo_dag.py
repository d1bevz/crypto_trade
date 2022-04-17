from airflow.decorators import dag, task
from airflow.utils.dates import days_ago


@dag(default_args={'owner': 'airflow'}, schedule_interval=None,
     start_date=days_ago(2))
def demo_dag():
    @task
    def extract():
        return {"1001": 301.27, "1002": 433.21, "1003": 502.22}

    @task
    def transform(order_data_dict: dict) -> dict:
        total_order_value = 0

        for value in order_data_dict.values():
            total_order_value += value

        return {"total_order_value": total_order_value}

    @task()
    def load(total_order_value: dict):
        print("Total order value is: ", total_order_value["total_order_value"])

    order_data = extract()
    order_summary = transform(order_data)
    load(order_summary)


demo_dag = demo_dag()
