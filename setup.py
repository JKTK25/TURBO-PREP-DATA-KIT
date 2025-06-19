from setuptools import setup, find_packages

setup(
    name='doc-processor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'tiktoken',
        'pytesseract',
        'Pillow',
        'langdetect',
        'pymupdf',
        'python-docx',
        'tqdm',
        'spacy',
        'language-tool-python'
    ],
    entry_points={
        'console_scripts': [
            'doc-extract=doc_processor.scripts.doc_extract:main',
            'doc-clean=doc_processor.scripts.doc_clean:main',
        ],
    },
    extras_require={
        'ocr': ['pytesseract'],
        'grammar': ['language-tool-python']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)