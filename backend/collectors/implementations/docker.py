import docker

from backend.collectors.base import BaseCollector
from backend.core.logger import logger
from backend.parsers.docker_parser import DockerParser


class DockerCollector(BaseCollector):

    def __init__(self):

        self.client = docker.from_env()

        self.parser = DockerParser()

    def collect(self):

        parsed_logs = []

        containers = self.client.containers.list()

        for container in containers:

            try:

                logs = container.logs(
                    tail=20
                ).decode().splitlines()

                for log in logs:

                    parsed = self.parser.parse(log)

                    if parsed:

                        parsed_logs.append(parsed)

            except Exception as error:

                logger.error(
                    "Failed collecting logs from container '%s': %s",
                    container.name,
                    error,
                )

        return parsed_logs