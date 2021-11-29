import spacy
from processing import WordProcessor, DocProcessor, WordMetaData


class TestWordProcessor:
    def setup_method(self):
        spacy.util.fix_random_seed(42)

    def test_get_unique_words_where_duplicates_are_present(self):
        data = "Hi world Hi, to the world"
        word_processor = WordProcessor(data)
        assert word_processor.run() == ["world"]

    def test_get_unique_words_where_duplicates_no_nouns(self):
        data = "Hi Hi, to the"
        word_processor = WordProcessor(data)
        assert len(word_processor._get_unique_words(data)) == 3
        assert word_processor.run() == []

    def test_no_stop_words_are_present(self):
        data = "its, the, for, and that"
        word_processor = WordProcessor(data)

        assert word_processor.run() == []

    def test_no_stop_words_are_present_and_noun_is_found(self):
        data = "Hi its, the, for, and that, Pyramid"
        word_processor = WordProcessor(data)
        assert word_processor.run() == ["pyramid"]


class TestDocProcessor:
    def setup_method(self):
        spacy.util.fix_random_seed(42)

    def test_doc_processor_returns_two_word_entries(self):
        doc_processor = DocProcessor(
            "Hello and welcome to earth, this is a blue sea",
            ["earth", "sea", "mars"],
            "test-doc",
        )
        assert doc_processor.run() == {
            "test-doc": {
                "earth": WordMetaData(
                    count=1, sentence=["Hello and welcome to earth, this is a blue sea"]
                ),
                "sea": WordMetaData(
                    count=1, sentence=["Hello and welcome to earth, this is a blue sea"]
                ),
            }
        }

    def test_doc_processor_returns_empty_dict_when_no_words_found(self):
        doc_processor = DocProcessor(
            "Hello and welcome to and this is a blue", ["earth", "sea"], "test-doc",
        )
        assert doc_processor.run() == {"test-doc": {}}
