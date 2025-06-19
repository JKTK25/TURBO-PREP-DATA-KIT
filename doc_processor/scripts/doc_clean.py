#!/usr/bin/env python3
import argparse
from doc_processor.cleaner import clean_jsonl

def main():
    parser = argparse.ArgumentParser(description='Clean extracted JSONL data')
    parser.add_argument('--input', required=True, help='Input JSONL file')
    parser.add_argument('--output', required=True, help='Output JSONL file')
    parser.add_argument('--enable_grammar', action='store_true', help='Enable grammar correction')
    parser.add_argument('--num_workers', type=int, default=4, help='Number of worker threads')
    
    args = parser.parse_args()
    
    processed, skipped = clean_jsonl(
        args.input,
        args.output,
        enable_grammar=args.enable_grammar,
        num_workers=args.num_workers
    )
    
    print(f"✅ Cleaning complete! Processed: {processed}, Skipped: {skipped}")

if __name__ == "__main__":
    main()