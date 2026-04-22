# What Is OCR?

## Big picture

OCR stands for **Optical Character Recognition**. It is the process of turning text that appears inside an image into machine-readable text.

If you can see letters on the screen but a program cannot copy them as text, OCR is often the missing step.

In PDF work, OCR becomes necessary when the document is a scan rather than a true digital-text PDF. A scanned page may look like a normal document, but technically it is often just a picture of paper. OCR tries to recover the characters from that picture.

## Why OCR matters

OCR is important because many real documents arrive as:

- scanned contracts;
- photographed notes;
- printed forms saved as PDFs;
- old archives;
- receipts and invoices;
- reports exported from scanners or multifunction printers.

Without OCR, these files are hard to search, analyze, summarize, or convert into structured data.

## OCR compared with normal PDF text extraction

Direct PDF text extraction and OCR solve different problems:

- **Direct extraction** reads text that is already stored in the PDF.
- **OCR** tries to recognize text from page images.

If `PyPDF2` or similar tools can already extract clean text, OCR may be unnecessary. If extraction returns empty or poor output because the page is image-based, OCR is the correct next step.

In this folder:

- `digital_text.pdf` is mainly a direct-extraction task;
- `scanned_document.pdf` and `scanned_document_page1.png` are OCR-oriented examples.

## How OCR works at a high level

OCR usually follows a pipeline like this:

1. Load an image or convert PDF pages into images.
2. Improve the image quality if needed.
3. Detect where text exists on the page.
4. Recognize letters, words, and numbers.
5. Reconstruct lines or blocks of text.
6. Optionally apply language rules or post-processing.

In Python, a common workflow is:

- use `pdf2image` to convert PDF pages to images;
- use `Pillow` for basic image handling;
- use `pytesseract` to run OCR with Tesseract.

## OCR is recognition, not recovery of original structure

OCR can often recover the visible text, but it usually does not recover the original document structure perfectly.

For example, OCR may not fully understand:

- heading hierarchy;
- table boundaries;
- reading order in complex multi-column layouts;
- whether a number belongs to one column or another;
- whether a line is a footer, caption, or body text.

This is one reason OCR output usually needs validation and cleanup.

## Main OCR challenges

### 1. Image quality

OCR quality depends heavily on the quality of the input image. Common problems include:

- blur;
- low resolution;
- shadows;
- low contrast;
- compression artifacts;
- scanner streaks or dust;
- overexposed or dark pages.

If the letters are unclear to the model, recognition errors increase quickly.

### 2. Rotation and skew

Scanned pages are often slightly tilted. Even a small angle can make line detection and character recognition worse.

Typical issues:

- text lines drift upward or downward;
- columns are misread;
- word segmentation becomes unstable.

Preprocessing such as deskewing or rotation correction can improve results significantly.

### 3. Noise and background texture

OCR works best when text stands out clearly from the background. It struggles with:

- gray paper texture;
- stamps;
- handwritten marks;
- folds and shadows;
- ruled notebook lines;
- noisy photocopies.

The OCR engine may mistake these patterns for characters or merge them with nearby text.

### 4. Fonts, symbols, and languages

OCR is not equally strong on every writing style. Accuracy can drop with:

- decorative fonts;
- tiny text;
- unusual symbols;
- mixed alphabets;
- mathematical notation;
- accented characters;
- domain-specific abbreviations.

Language configuration matters. If the OCR engine expects English but the document contains Latvian names or other accented text, the output may degrade.

### 5. Tables are difficult for OCR

OCR can recognize the text inside a table, but that does not mean it understands the table structure.

Common failures:

- rows merged together;
- columns shifted;
- numbers attached to the wrong headers;
- cell boundaries ignored;
- multi-line cells flattened into messy text.

This is why OCR alone is often not enough for high-quality table extraction.

### 6. Mixed-content pages

Real pages often combine:

- paragraphs;
- logos;
- stamps;
- signatures;
- charts;
- tables;
- page numbers.

OCR may capture all visible text but still mix unrelated pieces together. A header, a caption, and a footer may appear in the middle of the extracted paragraph flow.

### 7. Similar-looking characters

OCR commonly confuses characters that look alike, such as:

- `O` and `0`;
- `I`, `l`, and `1`;
- `S` and `5`;
- `B` and `8`.

These small errors matter a lot in names, IDs, invoice numbers, dates, and financial data.

### 8. Handwriting is a separate difficulty

Standard OCR works best on printed text. Handwriting is much harder because:

- letters are inconsistent;
- words overlap;
- line spacing varies;
- individual writing styles differ greatly.

Some handwriting can be partly recognized, but expectations should be lower than for printed documents.

## Why OCR output needs post-processing

Raw OCR text often contains:

- broken line endings;
- missing or extra spaces;
- incorrect punctuation;
- merged columns;
- repeated headers and footers;
- character substitutions.

Post-processing may include:

- whitespace cleanup;
- confidence filtering;
- dictionary or keyword checks;
- regex validation for dates, codes, or IDs;
- manual review of critical fields.

For serious workflows, OCR should be treated as an estimate that needs checking.

## Practical OCR workflow for students

When working in `pdf_tasks`, a practical workflow is:

1. Test whether direct PDF extraction already works.
2. If not, convert the page to an image.
3. Run OCR on the image.
4. Compare OCR output with the visible document.
5. Note recurring recognition mistakes.
6. Clean the result before analysis or export.

That comparison step is essential. OCR quality should be measured, not assumed.

## When OCR is the right tool

Use OCR when:

- the PDF contains scanned page images;
- text is visible but cannot be selected reliably;
- copied text is empty or clearly broken;
- documents come from a scanner, camera, or archive image source.

Do not use OCR by default when the document already contains clean digital text. In that case, direct extraction is usually faster, simpler, and more accurate.

## Summary

OCR converts visible text in images into machine-readable text. It is extremely useful, but it is not magic.

The main lesson is:

- **OCR helps computers read images of text, but the result is always shaped by image quality, layout complexity, and recognition errors**.

In PDF analysis, OCR is best seen as a fallback or companion technique for scanned and image-based documents.
