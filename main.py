from src import parse_log_line


def main() -> None:
    path: str = "/home/aryahi/Desktop/projects/my_project/sandbox_data/sample.log"
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            parse_log_line(line.strip())
            print("\n")
    pass


if __name__ == "__main__":
    main()
