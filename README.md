# kewpie
KEyWord PIckEr with tf-idf

Work in Progress.

## Installation
```bash
pip install kewpie
```

## Basic Usage
```py
from kewpie import KwPicker

docs = [
    "I am a cat.",
    "I am a dog."
]

picker = KwPicker.build(docs, savedir='/dir/to/save/model/')

sentence = "I am a cat."
span, keyword = picker.get_keywords(sentence)

print(keyword)  # -> 'cat'
```
