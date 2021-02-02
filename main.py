"""A simple hello world Hail Batch example."""

import os
import hailtop.batch as hb

backend = hb.ServiceBackend(
    billing_project=os.getenv('HAIL_BILLING_PROJECT'), bucket=os.getenv('HAIL_BUCKET')
)

batch = hb.Batch(backend=backend, name='hello world')

job = batch.new_job(name='hello')
job.image('australia-southeast1-docker.pkg.dev/analysis-runner/images/ubuntu:20.04')
job.command('echo "hello world"')

batch.run()
