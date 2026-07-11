from datetime import datetime

from backend.collectors.base import BaseCollector


class DummyCollector(BaseCollector):

    def collect(self):

        return [

            {
                "timestamp": datetime.now(),

                "source": "Dummy",

                "level": "INFO",

                "message": "Application Started",

            },

            {
                "timestamp": datetime.now(),

                "source": "Dummy",

                "level": "ERROR",

                "message": "Payment Service Crashed",

            },

            {
                "timestamp": datetime.now(),

                "source": "Dummy",

                "level": "WARNING",

                "message": "CPU Usage High",

            },

        ]