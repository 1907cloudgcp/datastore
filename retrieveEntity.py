from google.cloud import datastore

client = datastore.Client()

key = client.key('batch', 'gcp', 'associate', 'Mouad')
task = client.get(key)
print(f'{task}')