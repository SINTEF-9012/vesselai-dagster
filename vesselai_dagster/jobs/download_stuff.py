from dagster import job

from vesselai_dagster.ops.download import download_nwp


def download_stuff_job():
    """
    A job definition. This example job has a single op.

    For more hints on writing Dagster jobs, see our documentation overview on Jobs:
    https://docs.dagster.io/concepts/ops-jobs-graphs/jobs-graphs
    """
    download_nwp()
