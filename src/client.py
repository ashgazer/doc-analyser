import logging
from data_extractor import get_documents
from report_generator import create_reports, create_final_report


def main() -> None:
    try:
        documents = get_documents()

        reports = create_reports(documents)
        create_final_report(reports)
    except Exception as error:
        logging.warning("The following error was raised %s", error)

        raise error


if __name__ == "__main__":
    main()
