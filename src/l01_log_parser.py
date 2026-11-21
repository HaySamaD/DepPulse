def parse_log_line(line: str) -> dict[str, str] | None:
    action: list = [e.strip() for e in line.split('|')]
    print(action)
    pass

def load_logs(file_path: str) -> tuple[list[dict[str, str]], int] | None:
    pass
