import os


def get_env(option):
    def redis_host():
        return os.getenv("REDIS_HOST", "-")

    def redis_port():
        return int(os.getenv("REDIS_PORT", "0"))

    def crm_service():
        return os.getenv("CRM_SERVICE", "-")

    def crm_internal_username():
        return os.getenv("CRM_INTERNAL_USERNAME", "-")

    def crm_internal_password():
        return os.getenv("CRM_INTERNAL_PASSWORD", "-")

    def account_service():
        return os.getenv("ACCOUNT_SERVICE", "-")

    def tariff_service():
        return os.getenv("TARIFF_SERVICE", "-")

    def machine_learning_gateway_username():
        return os.getenv("MACHINE_LEARNING_GATEWAY_USERNAME", "-")

    def machine_learning_gateway_password():
        return os.getenv("MACHINE_LEARNING_GATEWAY_PASSWORD", "-")

    def log_level():
        return (os.getenv("LOG_LEVEL", "-")).strip().upper()

    def celery_broker_user():
        return os.getenv("CELERY_BROKER_USER", "-")

    def celery_broker_password():
        return os.getenv("CELERY_BROKER_PASSWORD", "-")

    def celery_broker_host():
        return os.getenv("CELERY_BROKER_HOST", "-")

    def celery_broker_vhost():
        return os.getenv("CELERY_BROKER_VHOST", "-")

    def mlgw_user():
        return os.getenv("MLGW_USER", "-")

    def mlgw_pass():
        return os.getenv("MLGW_PASS", "-")

    def sensor_information_service():
        return os.getenv("SENSOR_INFO_SERVICE", "-")

    def smart_meter_service():
        return os.getenv("SMART_METER_CHARGES_SERVICE", "-")

    def voltaware_30min_cassandra_keyspace():
        return os.getenv("30MIN_VOLTAWARE_CASSANDRA_KEYSPACE")

    def cassandra_user():
        return os.getenv("CASSANDRA_USER")

    def cassandra_pass():
        return os.getenv("CASSANDRA_PASS")

    def cassandra_host():
        return os.getenv("CASSANDRA_HOST")

    def cassandra_consistency_level_delete():
        return os.getenv("CASSANDRA_CONSISTENCY_LEVEL_DELETE", "ONE").upper()

    def generate_pickles():
        return os.getenv("GENERATE_PICKLES", "FALSE").upper() == "TRUE"

    def generate_local_log():
        return os.getenv("GENERATE_LOCAL_LOG", "FALSE").upper() == "TRUE"

    def mlms_bucket_name():
        return os.getenv("MLMS_BUCKET_NAME", "-")

    def disconnection_threshold_days():
        return int(os.getenv("DISCONNECTION_THRESHOLD_DAYS", "7"))

    options = {
        "REDIS_HOST": redis_host,
        "REDIS_PORT": redis_port,
        "CRM_SERVICE": crm_service,
        "CRM_INTERNAL_USERNAME": crm_internal_username,
        "CRM_INTERNAL_PASSWORD": crm_internal_password,
        "MACHINE_LEARNING_GATEWAY_USERNAME": machine_learning_gateway_username,
        "MACHINE_LEARNING_GATEWAY_PASSWORD": machine_learning_gateway_password,
        "LOG_LEVEL": log_level,
        "CELERY_BROKER_USER": celery_broker_user,
        "CELERY_BROKER_PASSWORD": celery_broker_password,
        "CELERY_BROKER_HOST": celery_broker_host,
        "CELERY_BROKER_VHOST": celery_broker_vhost,
        "ACCOUNT_SERVICE": account_service,
        "TARIFF_SERVICE": tariff_service,
        "SMART_METER_CHARGES_SERVICE": smart_meter_service,
        "MLGW_USER": mlgw_user,
        "MLGW_PASS": mlgw_pass,
        "SENSOR_INFO_SERVICE": sensor_information_service,
        "30MIN_VOLTAWARE_CASSANDRA_KEYSPACE": voltaware_30min_cassandra_keyspace,
        "CASSANDRA_USER": cassandra_user,
        "CASSANDRA_PASS": cassandra_pass,
        "CASSANDRA_HOST": cassandra_host,
        "CASSANDRA_CONSISTENCY_LEVEL_DELETE": cassandra_consistency_level_delete,
        "GENERATE_PICKLES": generate_pickles,
        "GENERATE_LOCAL_LOG": generate_local_log,
        "MLMS_BUCKET_NAME": mlms_bucket_name,
        "DISCONNECTION_THRESHOLD_DAYS": disconnection_threshold_days,
    }
    return options[option]()
