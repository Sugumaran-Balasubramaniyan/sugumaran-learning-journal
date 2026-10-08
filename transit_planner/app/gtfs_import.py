"""GTFS schedule import and parsing helpers."""


def parse_gtfs_time(value: str) -> int:
    hours, minutes, seconds = (int(part) for part in value.split(":"))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds
