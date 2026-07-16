import docker

client = docker.from_env()

containers = client.containers.list()

print(f"Found {len(containers)} running container(s)\n")

for container in containers:

    print(f"Container Name : {container.name}")
    print(f"Container ID   : {container.short_id}")

    logs = container.logs(
        stdout=True,
        stderr=True,
        timestamps=True,
        tail=20
    )

    print("\nLogs:\n")
    print(logs.decode())

    print("-" * 60)