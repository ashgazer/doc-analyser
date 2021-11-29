from report_generator import create_reports, create_final_report
from tempfile import NamedTemporaryFile
from unittest import mock

from freezegun import freeze_time
from processing import WordMetaData


class TestCreateReports:
    def test_create_reports(self):
        with NamedTemporaryFile(delete=False) as fp:
            fp.write(b"hello there earth")
            file_name = fp.name

        with NamedTemporaryFile(delete=False) as fp:
            fp.write(b"hello there mars")
            file_name2 = fp.name

        result = create_reports({"file1.txt": file_name, "file2.txt": file_name2})

        assert result == [
            {
                "file1.txt": {
                    "earth": WordMetaData(count=1, sentence=["hello there earth"])
                }
            },
            {
                "file2.txt": {
                    "mars": WordMetaData(count=1, sentence=["hello there mars"])
                }
            },
        ]


class TestCreateFinalReport:
    @freeze_time("2020-01-01 12:00")
    @mock.patch("report_generator.pd")
    def test_create_final_reports(self, mock_pd):

        reports = [
            {
                "file1.txt": {
                    "earth": WordMetaData(count=1, sentence=["hello there earth"])
                }
            },
            {
                "file2.txt": {
                    "mars": WordMetaData(count=1, sentence=["hello there mars"])
                }
            },
        ]
        result = create_final_report(reports)

        mock_pd.DataFrame.assert_called_with(
            [
                {
                    "count": 1,
                    "docs": {"file1.txt"},
                    "sentence": [["hello there earth"]],
                    "word": "earth",
                },
                {
                    "count": 1,
                    "docs": {"file2.txt"},
                    "sentence": [["hello there mars"]],
                    "word": "mars",
                },
            ]
        )

        mock_pd.DataFrame()[3].to_csv.assert_called_with(
            "output/Analysis_2020-01-01-12-00.csv", index=False
        )

        assert result is None
