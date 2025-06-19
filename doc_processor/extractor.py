import json
import re
import hashlib
import os
import logging
import concurrent.futures
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from tqdm import tqdm
from PIL import Image
import fitz
import pytesseract
import langdetect
from langdetect import DetectorFactory
from docx import Document

DetectorFactory.seed = 0
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class EnhancedDocumentExtractor:
    def __init__(
        self,
        input_dir: str,
        output_file: str,
        max_tokens: Optional[int] = 512,
        min_chunk_size: int = 100,
        overlap: int = 50,
        target_language: Optional[str] = "en",
        min_text_quality: float = 0.7,
        enable_ocr: bool = True,
        num_workers: int = None
    ):
        self.input_dir = Path(input_dir)
        if not self.input_dir.exists():
            raise ValueError(f"Input directory {self.input_dir} does not exist")
        
        self.output_file = Path(output_file)
        self.output_file.parent.mkdir(parents=True, exist_ok=True)
        
        self.max_tokens = max_tokens
        self.min_chunk_size = min_chunk_size
        self.overlap = overlap
        self.target_language = target_language
        self.min_text_quality = min_text_quality
        self.enable_ocr = enable_ocr
        self.num_workers = num_workers or os.cpu_count() // 2 or 1
        self.seen_hashes = self._load_existing_hashes()
        self._setup_encoder()
        
        # Precompile regex patterns
        self.clean_patterns = {
            'whitespace': re.compile(r'\s+'),
            'hyphen_newline': re.compile(r'-\n'),
            'newline': re.compile(r'\n'),
            'control_chars': re.compile(r'[\x00-\x1f\x7f-\x9f]'),
            'form_feed': re.compile(r'\x0c'),
            'header_footer': re.compile(r'^\d+\s+\w+\s+\d+$', flags=re.MULTILINE)
        }

    def _setup_encoder(self):
        if self.max_tokens:
            import tiktoken
            self.encoder = tiktoken.get_encoding("cl100k_base")
        else:
            self.encoder = None

    def _load_existing_hashes(self) -> set:
        seen = set()
        if self.output_file.exists():
            with open(self.output_file, 'r', encoding='utf-8') as f:
                for line in f:
                    try:
                        record = json.loads(line)
                        text = record.get("text", "")
                        hash_ = self.generate_content_hash(text)
                        seen.add(hash_)
                    except Exception:
                        continue
        return seen

    # ... (rest of the extractor class methods unchanged) ...