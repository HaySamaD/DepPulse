from src import parse_log_line


def main() -> None:
    path: str = "sandbox_data/sample.log"
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            print(parse_log_line(line.strip()))


if __name__ == "__main__":
    main()
