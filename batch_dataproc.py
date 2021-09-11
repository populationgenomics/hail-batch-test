#!/usr/bin/env python3

"""
Test submitting a Dataproc job from Batch
"""

import os
from os.path import join, abspath, dirname
import hailtop.batch as hb
from analysis_runner import dataproc
from package import utils


os.environ['DATASET'] = 'fewgenomes'
os.environ['DATASET_GCP_PROJECT'] = 'fewgenomes'
os.environ['OUTPUT'] = 'hail/tmp'
os.environ['ACCESS_LEVEL'] = 'test'


def main():  # pylint: disable=missing-function-docstring
    billing_project = 'vladislavsavelyev-trial'
    hail_bucket = 'playground-au/hail/tmp'
    backend = hb.ServiceBackend(
        billing_project=billing_project,
        bucket=hail_bucket.replace('gs://', ''),
    )
    b = hb.Batch(
        'test',
        backend=backend,
    )

    utils.say_hello('batch dataproc.py')

    # Scripts path to pass to dataproc when submitting scripts
    scripts_dir = abspath(join(dirname(__file__), 'scripts'))
    package_dir = abspath(join(dirname(__file__), 'package'))

    dataproc.hail_dataproc_job(
        b,
        f'{scripts_dir}/myscript.py',
        pyfiles=[f'{package_dir}/{fp}' for fp in os.listdir(package_dir)],
        job_name='test myscript',
        max_age=1,
    )

    b.run(wait=False)


if __name__ == '__main__':
    main()  # pylint: disable=E1120
