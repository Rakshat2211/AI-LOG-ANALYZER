import docker

from backend.collectors.base import BaseCollector
from backend.core.logger import logger
from backend.parsers.docker_parser import DockerParser


class DockerCollector(BaseCollector):

    def __init__(self):
        self.parser = DockerParser()

    def collect(self):

        parsed_logs = []

        try:

            client = docker.from_env()

            containers = client.containers.list()

        except Exception as error:

            logger.error(
                "Unable to connect to Docker Engine: {}",
                error,
            )

            return []

        for container in containers:

            try:

                logs = (
                    container.logs(tail=20)
                    .decode()
                    .splitlines()
                )

                for log in logs:

                    parsed = self.parser.parse(log)

                    if parsed:
                        parsed_logs.append(parsed)

            except Exception as error:

                logger.error(
                    "Failed collecting logs from container '{}': {}",
                    container.name,
                    error,
                )

        return parsed_logs