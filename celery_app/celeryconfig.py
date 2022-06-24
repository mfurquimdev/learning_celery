import parameter
from redis_connection import redis_backend

# Configure the broker URI
broker_url = "amqp://{}:{}@{}:5672/{}".format(
    parameter.get_env("CELERY_BROKER_USER"),
    parameter.get_env("CELERY_BROKER_PASSWORD"),
    parameter.get_env("CELERY_BROKER_HOST"),
    parameter.get_env("CELERY_BROKER_VHOST"),
)

# Configure result backend
result_backend = "redis://{}:{}/{}".format(
    parameter.get_env("REDIS_HOST"),
    parameter.get_env("REDIS_PORT"),
    redis_backend.connection_pool.connection_kwargs.get("db"),
)
# result_backend = 'cassandra'
# cassandra_servers = ['localhost']
# cassandra_auth_kwargs = {
#    'username': parameter.get_env('CASSANDRA_USER'),
#    'password': parameter.get_env('CASSANDRA_PASS')
# }
# cassandra_keyspace = 'celery'
# cassandra_table = 'tasks'
# cassandra_read_consistency = 'ONE'
# cassandra_write_consistency = 'ONE'
# cassandra_entry_ttl = 86400

# Force celery to just acknowledge the task after it is executed
task_acks_late = True

accept_content = ["json", "pickle"]

task_serializer = "pickle"

result_serializer = "pickle"

worker_prefetch_multiplier = 1

worker_log_format = "%(asctime)s - %(levelname)s %(processName)s: %(message)s"
worker_task_log_format = "%(asctime)s - %(levelname)s %(processName)s: %(task_name)s[%(task_id)s]: %(message)s"

task_send_sent_event = True
