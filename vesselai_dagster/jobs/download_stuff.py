from dagster import job
from dagster import daily_partitioned_config
from datetime import datetime

from vesselai_dagster.ops.download import download_nwp


@daily_partitioned_config(start_date=datetime(2019, 1, 1), end_offset=-1160)
def my_partitioned_config(start: datetime, _end: datetime):
    return {
        "ops": {
            "process_data_for_date": {"config": {"date": start.strftime("%Y-%m-%d")}}
        }
    }


@job(config=my_partitioned_config)
def download_stuff_job():
    """
    A job definition. This example job has a single op.

    For more hints on writing Dagster jobs, see our documentation overview on Jobs:
    https://docs.dagster.io/concepts/ops-jobs-graphs/jobs-graphs
    """
    download_nwp()
