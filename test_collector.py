from backend.collectors.implementations.docker import DockerCollector

collector = DockerCollector()

logs = collector.collect()

print(f"Collected {len(logs)} logs\n")

for log in logs:
    print(log)