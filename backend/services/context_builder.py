def build_analysis_context(
    total_logs: int,
    info_logs: int,
    warning_logs: int,
    error_logs: int,
    logs_by_source: dict[str, int],
    most_common_level: str | None,
    anomalies: list[str],
) -> str:
    """
    Builds a structured text report that can later
    be sent to an LLM.
    """

    report = []

    report.append("=== Intelligent Log Analysis Report ===")
    report.append("")

    report.append(f"Total Logs: {total_logs}")
    report.append(f"INFO Logs: {info_logs}")
    report.append(f"WARNING Logs: {warning_logs}")
    report.append(f"ERROR Logs: {error_logs}")
    report.append("")

    report.append("Logs By Source:")

    for source, count in logs_by_source.items():
        report.append(f"- {source}: {count}")

    report.append("")

    report.append(
        f"Most Common Log Level: {most_common_level}"
    )

    report.append("")

    report.append("Detected Anomalies:")

    if anomalies:

        for anomaly in anomalies:

            report.append(f"- {anomaly}")

    else:

        report.append("- None")

    return "\n".join(report)