from backend.collectors.manager import CollectorManager

manager = CollectorManager()

logs = manager.collect_all_logs()

print(logs)