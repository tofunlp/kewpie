import os
import tempfile
import shutil
from unittest import TestCase

from kewpie import KwPicker


docs = [
        "I am a cat.",
        "I am a dog."
        ]


class KwPickerBuildCase(TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_build(self):
        KwPicker.build(
                docs,
                savedir=self.tempdir,
                tokenizer=None
                )

        self.assertTrue(os.path.exists(os.path.join(self.tempdir, 'vectorizer.pth')))


class KwPickerLoadCase(TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        KwPicker.build(
                docs,
                savedir=self.tempdir,
                tokenizer=None
                )

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_load(self):
        KwPicker.load(os.path.join(self.tempdir, 'vectorizer.pth'))


class KwPickerCase(TestCase):

    def setUp(self):
        self.picker = KwPicker.build(
                docs,
                savedir=None,
                tokenizer=None
                )

    def tearDown(self):
        pass

    def test_get_keyword(self):
        sentence = docs[0]
        gt_span = (7, 10)
        gt_keyword = 'cat'
        span, keyword = self.picker.get_keyword(sentence)

        self.assertEqual(span, gt_span)
        self.assertEqual(keyword, gt_keyword)
        self.assertEqual(sentence[span[0]:span[1]], keyword)
