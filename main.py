"""A simple hello world Hail Batch example."""

import os
import hailtop.batch as hb

backend = hb.ServiceBackend(
    billing_project=os.getenv('HAIL_BILLING_PROJECT'), bucket=os.getenv('HAIL_BUCKET')
)

b = hb.Batch(backend=backend, name='hello world')

ref = b.read_input('gs://gcp-public-data--gnomad/release/3.1/vcf/genomes/gnomad.genomes.v3.1.sites.chrM.reduced_annotations.tsv')
j = b.new_job('Test job')
j.command(f'ls {ref}')
b.run()
