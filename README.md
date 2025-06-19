
# Data Extraction Pipeline

This Jupyter Notebook provides a structured approach to extract data from PDF documents using advanced preprocessing, layout analysis, and parsing techniques. It primarily leverages tools like `PyMuPDF`, `pdf2image`, and `pytesseract` to handle PDFs and extract structured data from scanned or embedded content.

## Features

- Convert PDFs to images (per page) for OCR processing.
- Extract tabular and textual data using Tesseract OCR.
- Analyze and visualize page layouts.
- Save processed data to structured formats (e.g., DataFrames).
- Modular design for page-wise and bulk processing.

## Project Structure

- **Load and Setup**: Import all dependencies, configure paths, and initialize the processing environment.
- **PDF Preprocessing**: Convert PDF pages into images and preprocess for better OCR accuracy.
- **Data Extraction**: Use `pytesseract` to extract both text and layout information.
- **Visualization**: Visualize bounding boxes of detected text on page images.
- **Data Structuring**: Format extracted data into structured representations for downstream tasks.

## Dependencies

Install the required Python packages:

```bash
pip install PyMuPDF pdf2image pytesseract matplotlib pandas opencv-python
```

### System Requirements

- **Tesseract OCR** must be installed separately on your machine.
  - On Ubuntu: `sudo apt install tesseract-ocr`
  - On macOS: `brew install tesseract`
  - On Windows: [Tesseract Installer](https://github.com/tesseract-ocr/tesseract)

Ensure that the Tesseract executable is in your system path.

## Usage

1. **Clone or Download the Repository**  
   Place your target PDFs into the working directory or adjust the path in the notebook.

2. **Run the Notebook**  
   Open `DATA_PDF_PROCESSING_EXTRACTION.ipynb` in Jupyter Lab/Notebook and execute the cells in order.

3. **Output**  
   - Extracted tables and text as Pandas DataFrames.
   - Visual layout maps (text bounding boxes).
   - Preprocessed images for manual inspection.

## Customization

- You can modify the DPI in `pdf2image.convert_from_path()` to improve image quality.
- Add custom Tesseract configuration options (e.g., `--psm`, `--oem`) depending on document complexity.
- Layout segmentation can be refined using heuristics or by integrating `pdfplumber` or `layoutparser`.

## Sample Code Snippet

```python
from pdf2image import convert_from_path
import pytesseract

images = convert_from_path("sample.pdf", dpi=300)
for img in images:
    text = pytesseract.image_to_string(img)
    print(text)
```

## License

This project is licensed under the MIT License.

## Author
James Kariuki (Jamexkarix583@gmai.com)
Created and maintained by [Turbo organization]
