import json
import copy
import sys
import os

benchmark = {
        "type" : "store-multi",
        "repetitions" : 1,
        "collection" : {
            "type" : "unqlite",
            "path" : "/local/scratch/mydb",
            "database-name" : "mydb",
            "collection-name" : "mycollection"
        },
        "records" : {
            "num" : 131072,
            "fields" : 12,
            "key-size" : [ 4, 12 ],
            "val-size" : [ 1, 32 ]
        },
        "use-json" : False,
        "batch-size" : 1
    }

content = {
    "protocol" : "ofi+gni://",
    "seed" : 1234,
    "log" : "info",
    "server" : {
        "use-progress-thread" : False,
        "rpc-thread-count" : 0
    },
    "client" : {
        "use-progress-thread" : False
    },
    "benchmarks" : []
}

variations = [
    {
        "batch-size" : [ 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536 ],
        "collection.type" : [ "unqlite", "jsoncpp", "null" ]
    },
    {
        "batch-size" : [ 1, 4, 16, 64, 256, 1024, 4096, 16384, 65536 ],
        "collection.type" : [ "unqlite" ],
        "collection.path" : [ "/dev/shm/mydb" ]
    }
]

def get_variation(d, x):
    global benchmark
    factor = 1
    for k, v in d.items():
        i = x % len(v)
        if '.' in k:
            w = k.split('.')
            benchmark[w[0]][w[1]] = v[i]
        else:
            benchmark[k] = v[i]
        x /= len(v)
    return copy.deepcopy(benchmark)

for d in variations:
    count = 1
    for k, v in d.items():
        count *= len(v)
    for i in range(0,count):
        content["benchmarks"].append(get_variation(d, i))

with open('config.json','w+') as f:
    f.write(json.dumps(content, indent=2))
