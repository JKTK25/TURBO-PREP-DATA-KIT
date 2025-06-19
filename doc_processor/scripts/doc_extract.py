#!/usr/bin/env python3
import argparse
from doc_processor.extractor import EnhancedDocumentExtractor

def main():
    parser = argparse.ArgumentParser(description='Extract text from PDF/DOCX files')
    parser.add_argument('--input_dir', required=True, help='Input directory with documents')
    parser.add_argument('--output_file', required=True, help='Output JSONL file')
    parser.add_argument('--max_tokens', type=int, default=512, help='Max tokens per chunk')
    parser.add_argument('--min_chunk_size', type=int, default=100, help='Min chunk character length')
    parser.add_argument('--overlap', type=int, default=50, help='Chunk overlap size')
    parser.add_argument('--target_language', default='en', help='Target language code')
    parser.add_argument('--min_text_quality', type=float, default=0.65, help='Min text quality score')
    parser.add_argument('--disable_ocr', action='store_false', dest='enable_ocr', help='Disable OCR')
    parser.add_argument('--num_workers', type=int, default=None, help='Number of worker threads')
    
    args = parser.parse_args()
    
    extractor = EnhancedDocumentExtractor(
        input_dir=args.input_dir,
        output_file=args.output_file,
        max_tokens=args.max_tokens,
        min_chunk_size=args.min_chunk_size,
        overlap=args.overlap,
        target_language=args.target_language,
        min_text_quality=args.min_text_quality,
        enable_ocr=args.enable_ocr,
        num_workers=args.num_workers
    )
    extractor.process_documents()

if __name__ == "__main__":
    main()