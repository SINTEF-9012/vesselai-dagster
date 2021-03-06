from dagster import repository

from vesselai_dagster.jobs.say_hello import say_hello_job
from vesselai_dagster.jobs.download_stuff import download_stuff_job
from vesselai_dagster.schedules.my_hourly_schedule import my_hourly_schedule
from vesselai_dagster.sensors.my_sensor import my_sensor


@repository
def vesselai_dagster():
    """
    The repository definition for this vesselai_dagster Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job,download_stuff_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
