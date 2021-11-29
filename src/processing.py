import re
from typing import List, Set, Union, Dict

import spacy

from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class WordMetaData:
    count: int = 0

    sentence: List[str] = field(default_factory=lambda: [])


class WordProcessor:
    def __init__(self, data):
        self.data = data
        self.nlp = spacy.load("en_core_web_md")
        spacy.util.fix_random_seed(42)

    def _get_unique_words(self, text: str) -> List[str]:
        return list(map(lambda x: x.lower(), set(re.findall(r"[\w']+", text))))

    def _filter_out_stop_words(self, data: Set[str]):
        sw_spacy = self.nlp.Defaults.stop_words
        return [word for word in data if word not in sw_spacy]

    def _filter_nouns(self, data: Union[List[str], Set[str]]) -> List[str]:
        doc = self.nlp(" ".join(data))

        return [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]

    def run(self):
        unique_words = self._get_unique_words(self.data)
        return self._filter_nouns(unique_words)


class DocProcessor:
    def __init__(self, data: str, words, name: str):

        self.nlp = spacy.load("en_core_web_md")
        spacy.util.fix_random_seed(42)

        self.doc = self.nlp(data)
        self.words = words
        self.dummy = defaultdict(WordMetaData)
        self.name = name

    def get_word_count_in_sentence(self, sentence, word: List[str]) -> int:
        words = re.findall(r"[\w']+", str(sentence))
        return words.count(word)

    def run(self) -> Dict[str, Dict[str, WordMetaData]]:
        for word in self.words:
            for line in self.doc.sents:
                if word in str(line):
                    count = self.get_word_count_in_sentence(line, word)
                    self.dummy[word].count += count
                    self.dummy[word].sentence.append(str(line))

        return {self.name: self.dummy}
