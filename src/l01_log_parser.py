import re

_TIMESTAMP_REGEX = re.compile(
    r"^\d{4}"
    r"-(?:0[1-9]|1[0-2])"
    r"-(?:0[1-9]|[12]\d|3[01])"
    r"T(?:[01]\d|2[0-3])"
    r":[0-5]\d"
    r":[0-5]\dZ$"
)

_VALID_LEVEL = ("WARN", "INFO", "CRITICAL", "ERROR")

def parse_log_line(line: str) -> dict[str, str] | None:
    action: list = [e.strip() for e in line.split('|', 3)]
    if (
        len(action) < 4
        or len(action[0]) != 20
        or _TIMESTAMP_REGEX.match(action[0]) is None
        or action[1] not in _VALID_LEVEL
        or not action[2]
        or not action[3]
    ):
        return None

    return {
        "timestamp": action[0],
        "level": action[1],
        "service": action[2],
        "message": action[3],
    }
