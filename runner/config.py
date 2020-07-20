import collections
import itertools


def with_protocol(protocol):
    def delegate(config):
        config["protocol"] = protocol + "://"
        return config
    return delegate


def with_log_level(level):
    def delegate(config):
        config["log"] = level
        return config
    return delegate


def with_server_progress_thread(yes):
    def delegate(config):
        config["server"]["use-progress-thread"] = yes
        return config
    return delegate


def with_client_progress_thread(yes):
    def delegate(config):
        config["client"]["use-progress-thread"] = yes
        return config
    return delegate


def with_server_rpc_thread_count(count):
    def delegate(config):
        config["server"]["rpc-thread-count"] = count
        return config
    return delegate


def with_seed(seed):
    def delegate(config):
        config["seed"] = seed
        return config
    return delegate


def iterablize(val):
    if isinstance(val, str) or not isinstance(val, collections.Iterable):
        return [val]
    return val


def with_benchmark(use_json=True, repetitions=1, db_path="/mnt/bb/pmatri/mydb", db_types="unqlite",
                   db_name="mydb", collection_name="mycollection", record_fields=12, record_num=131072,
                   key_sizes=(4, 12), val_sizes=(1, 32), batch_sizes=(1), type="store-multi"):
    use_json = iterablize(use_json)
    db_types = iterablize(db_types)
    batch_sizes = iterablize(batch_sizes)
    record_fields = iterablize(record_fields)
    record_num = iterablize(record_num)

    def delegate(config):
        combinations = itertools.product(
            use_json, db_types, batch_sizes, record_fields, record_num)
        for b_use_json, db_type, batch_size, fields, num in combinations:
            benchmark = {
                "use-json": b_use_json,
                "repetitions": repetitions,
                "collection": {
                    "path": db_path,
                    "type": db_type,
                    "database-name": db_name,
                    "collection-name": collection_name,
                },
                "records": {
                    "fields": fields,
                    "num": num,
                    "key-size": key_sizes,
                    "val-size": val_sizes,
                },
                "batch-size": batch_size,
                "type": type,
            }
            config["benchmarks"].append(benchmark)
        return config
    return delegate


def gen_config(*delegates):
    config = {
        "protocol": "verbs://",
        "log": "info",
        "server": {
            "rpc-thread-count": 0,
            "use-progress-thread": False
        },
        "client": {
            "use-progress-thread": False
        },
        "seed": 1234,
        "benchmarks": [],
    }
    for delegate in delegates:
        config = delegate(config)
    return config
