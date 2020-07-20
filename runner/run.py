import json
import os
import tempfile


def run_with_config(config_file, executable="sonata-benchmark"):
    command = "{0} {1}".format(executable, config_file)
    stream = os.popen(command)
    output = stream.read()
    print(output)


def run(config):
    config = json.dumps(config, indent=2)
    print("config: {0}".format(config))
    with tempfile.NamedTemporaryFile() as fp:
        fp.write(config.encode("utf-8"))
        fp.flush()
        print("wrote config: {0}".format(fp.name))
        run_with_config(fp.name)
