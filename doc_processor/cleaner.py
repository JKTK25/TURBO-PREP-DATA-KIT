import json
import re
import time
import os
import threading
import hashlib
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import spacy
from language_tool_python import LanguageTool

thread_local = threading.local()

class TextCleaner:
    def __init__(self, enable_grammar=False):
        self.enable_grammar = enable_grammar
        self.nlp = None
        self.tool = None
        self.patterns = {
            'non_ascii': re.compile(r'[^\x00-\x7F]+'),
            'zero_width': re.compile(r'[\u200b-\u200d\uFEFF]'),
            'control_chars': re.compile(r'[\x00-\x1f\x7f-\x9f]'),
            'quotes': re.compile(r'[‘’]'),
            'double_quotes': re.compile(r'[“”]'),
            'symbols': re.compile(r"[^a-zA-Z0-9\s.,!?;:'\"-]"),
            'whitespace': re.compile(r'\s+'),
            'repeated_words': re.compile(r'\b(\w+)\s+\1\b', re.I),
            'sentence_end': re.compile(r'[.!?]$'),
            'sentence_start': re.compile(r'^\s*[a-z]')
        }

    # ... (rest of the cleaner class methods unchanged) ...