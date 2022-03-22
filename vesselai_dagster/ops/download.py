from dagster import op
import sys; sys.path.append('/Users/volkerh/Work_SINTEF/src/nwpstuff')
import nwpstuff


def download_nwp():
    """
    An op definition. This example op outputs a single string.

    For more hints about writing Dagster ops, see our documentation overview on Ops:
    https://docs.dagster.io/concepts/ops-jobs-graphs/ops
    """
    date='2019-01-01'
    basedir='/tmp'
    nwpstuff.download_nwp(date, basedir, force=True)
    return "Downloaded!"
