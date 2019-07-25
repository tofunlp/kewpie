import os
from typing import List, Callable
import pickle

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


class KwPicker(object):

    def __init__(self, vectorizer: TfidfVectorizer):
        self.vectorizer = vectorizer
        self.vocab = vectorizer.get_feature_names()
        self.tokenizer = vectorizer.build_tokenizer()

    def get_keyword(self, sentence: str) -> (str, int):
        vocab = np.array(self.vocab)

        docs = [sentence]
        x = self.vectorizer.transform(docs).todense().reshape(-1)

        vocab_idx = np.argmax(x, axis=1).tolist()
        keyword = vocab[tuple(vocab_idx)].tolist()[0]

        sent_idx = sentence.find(keyword)
        span = (sent_idx, sent_idx + len(keyword))

        return span, keyword

    @classmethod
    def build(cls, docs: List[str], savedir: str = None, tokenizer: Callable = None):
        vectorizer = TfidfVectorizer(
                docs,
                tokenizer=tokenizer
                )
        vectorizer.fit(docs)

        if savedir:
            with open(os.path.join(savedir, 'vectorizer.pth'), 'wb') as f:
                pickle.dump(vectorizer, f)

        return cls(vectorizer)

    @classmethod
    def load(cls, vectorizer_path: str):
        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)
        return cls(vectorizer)
