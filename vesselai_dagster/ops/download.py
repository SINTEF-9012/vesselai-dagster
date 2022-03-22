from dagster import op
import sys; sys.path.append('/Users/volkerh/Work_SINTEF/src/nwpstuff')
import nwpstuff


@op(config_schema={'date': str, 'force': bool})
def download_nwp(context):
    """
    An op definition. This example op outputs a single string.

    For more hints about writing Dagster ops, see our documentation overview on Ops:
    https://docs.dagster.io/concepts/ops-jobs-graphs/ops
    """
    basedir='/tmp'
    nwpstuff.download_nwp(context.op_config['date'], 
                          basedir, 
                          force=context.op_config['force'])
    return "Downloaded!"
