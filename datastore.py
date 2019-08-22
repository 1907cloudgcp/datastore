from google.cloud import datastore
client = datastore.Client()

entity = datastore.Entity(client.key('Task', 'teach datastore'))

entity.update({
    'show Client Lib': True,
    'done': False,
    'priority': 'pretty high'
})
client.put(entity)