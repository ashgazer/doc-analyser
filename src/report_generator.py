from collections import defaultdict
from dataclasses import dataclass, field, asdict
from typing import List
from typing import Tuple, Dict, Any
from datetime import datetime

import pandas as pd

from processing import WordProcessor, DocProcessor, WordMetaData


class UnableToCreateReportError(Exception):
    "Return Exception when creation of report fails"


@dataclass
class Report:
    count: int = 0
    docs: Tuple[str] = field(default_factory=lambda: set())
    sentence: List[str] = field(default_factory=lambda: [])


def get_report_name() -> str:
    now = datetime.now().strftime("%Y-%m-%d-%H-%M")
    return f"output/Analysis_{now}.csv"


def create_final_report(reports: List[Any]) -> None:
    temp = defaultdict(Report)
    try:
        for report in reports:
            for doc, analysis in report.items():
                for word, metadata in analysis.items():
                    temp[word].count += metadata.count
                    temp[word].docs.add(doc)
                    temp[word].sentence.append(metadata.sentence)

        df = pd.DataFrame([{**asdict(i), **{"word": k}} for k, i in temp.items()])
        df = df[["word", "count", "docs", "sentence"]]
        df.sort_values(by=["count"], inplace=True, ascending=False)
        df.to_csv(get_report_name(), index=False)
    except Exception as error:
        raise UnableToCreateReportError(f"{error}")


def create_reports(
    documents: Dict[str, str]
) -> List[Dict[str, Dict[str, WordMetaData]]]:
    reports = []
    try:
        for name, path in documents.items():
            with open(path, "r") as f:
                data = f.read()

            word_processor = WordProcessor(data)
            words = word_processor.run()

            doc_processor = DocProcessor(data, words, name)

            reports.append(doc_processor.run())
        return reports

    except Exception as error:
        raise UnableToCreateReportError(f"{error}")
