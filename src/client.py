from data_extractor import get_documents
from report_generator import create_reports, create_final_report


def main() -> None:
    documents = get_documents()

    reports = create_reports(documents)
    create_final_report(reports)


if __name__ == "__main__":
    main()
