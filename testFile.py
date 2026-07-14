from backend.collectors.implementations.dummy import DummyCollector

collector = DummyCollector()

logs = collector.collect()

print(logs)