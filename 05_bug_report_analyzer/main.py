bug_reports = [
    "login page error after submitting empty password",
    "robot task timeout when network is unstable",
    "admin page shows incorrect order status",
]


def count_keyword(reports: list[str], keyword: str) -> int:
    return sum(keyword in report for report in reports)


def main() -> None:
    keyword = "error"
    count = count_keyword(bug_reports, keyword)
    print(f"Keyword '{keyword}' appears in {count} report(s).")


if __name__ == "__main__":
    main()
