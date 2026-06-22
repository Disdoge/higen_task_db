def check_status_code(actual_status: int, expected_status: int = 200) -> bool:
    return actual_status == expected_status


def main() -> None:
    status_code = 200
    if check_status_code(status_code):
        print("API status check passed.")
    else:
        print("API status check failed.")


if __name__ == "__main__":
    main()
