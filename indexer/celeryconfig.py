CELERYD_CONCURRENCY=7
CELERYD_PREFETCH_MULTIPLIER=30
CELERYD_POOL_RESTARTS = True
CELERY_ACKS_LATE = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
BROKER_TRANSPORT_OPTIONS = {'confirm_publish': True}