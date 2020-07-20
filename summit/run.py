import runner


c = runner.gen_config(
    runner.with_benchmark(
        use_json=[True, False],
        batch_sizes=[1, 4, 16, 64, 256, 1024, 4096, 16384, 65536],
        db_types=["unqlite", "jsoncpp", "null"]
    ),
    runner.with_benchmark(
        use_json=[False],
        batch_sizes=[1, 4, 16, 64, 256, 1024, 4096, 16384, 65536],
        db_types=["unqlite"],
        db_path="/dev/shm/mydb",
    ),
)

runner.run(c)
