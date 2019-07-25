#!/usr/bin/env python
# coding: utf-8
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
        name='kewpie',
        use_scm_version=True,
        setup_requires=['setuptools_scm'],
        description='KEyWord PIckEr with tf-idf',
        long_description=open('./README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/sobamchan/kewpie',
        author='Sotaro Takeshita',
        author_email='oh.sore.sore.soutarou@gmail.com',
        packages=[
            'kewpie'
            ],
        license='MIT',
        classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7'
            ],
        install_requires=['numpy', 'scikit-learn'],
        tests_requires=['pytest']
        )
