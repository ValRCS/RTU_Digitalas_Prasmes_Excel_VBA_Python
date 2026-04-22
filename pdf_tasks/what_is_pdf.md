# What Is a PDF?

## Big picture

PDF stands for **Portable Document Format**. It is a file format designed to preserve the visual appearance of a document so that it looks similar on different computers, operating systems, printers, and screens.

That goal is important for publishing and sharing, but it also explains why PDFs can be difficult to analyze with code:

- a PDF is built to **display pages**, not to expose clean structured data;
- text may be positioned by coordinates instead of stored as logical paragraphs;
- tables may look obvious to a human even when the file does not contain a real table structure;
- some PDFs contain real digital text, while others are only page images.

In other words, a PDF is excellent for presentation, but often awkward for data extraction.

## Why PDFs are common

PDF is widely used because it is good at:

- preserving layout, fonts, and page breaks;
- combining text, images, charts, and vector graphics;
- printing consistently;
- sharing forms, reports, invoices, articles, and scanned documents;
- working across platforms without changing the visual result.

For business and education, this makes PDF a standard exchange format. For programming and analysis, it means the file may look simple while hiding a lot of complexity.

## What is inside a PDF

At a high level, a PDF document usually contains:

- pages;
- text objects;
- font information;
- images;
- drawing instructions for lines, boxes, and shapes;
- metadata such as title, author, or creation date;
- optional interactive elements such as links, form fields, or annotations.

The key detail is that many PDFs store content as **drawing instructions**. A page may effectively say:

- draw this line here;
- place this word at these coordinates;
- place this image in this rectangle;
- use this font with this size.

That is very different from a Word document or HTML page, where paragraphs, headings, and tables are often represented more explicitly.

## PDF is not always "text"

There are two broad document types you will meet in this folder:

- **Digital PDF**: the file contains selectable text. Tools such as `PyPDF2` or `pdfplumber` can often extract that text directly.
- **Scanned PDF**: the page is mostly an image of paper. The text is visible to a person, but not directly readable as text by normal PDF extraction tools. This is where [OCR](what_is_ocr.md) is needed.

Examples in `pdf_tasks`:

- `digital_text.pdf` is a digital-text example;
- `table_report.pdf` is useful for table extraction practice;
- `scanned_document.pdf` is a scanned example where direct text extraction is limited or empty.

## Why PDF extraction is challenging

### 1. Visual layout is not logical structure

Humans read a PDF as sentences, paragraphs, and sections. A program often sees separate text fragments placed at exact coordinates.

This causes problems such as:

- words extracted in the wrong order;
- missing spaces or extra spaces;
- broken lines in the middle of sentences;
- columns merged together;
- headers and footers mixed into body text.

### 2. Reading order is not guaranteed

A page with two columns may visually read from left column to right column. Internally, the objects may be stored in a different order. A parser may output:

- title text first;
- part of column two next;
- footer text after that;
- the rest of column one later.

The result can look confusing even when the PDF is valid.

### 3. Tables are often only an illusion

A table in a PDF may be nothing more than:

- text aligned in rows;
- a few drawn lines;
- empty spaces used for visual separation.

This means a library has to guess:

- where rows begin and end;
- which cells belong to which column;
- whether a drawn box is a table border or just decoration.

That is why table extraction can fail even when the table looks easy to a human reader.

### 4. Fonts and encodings can be unusual

Some PDFs use embedded fonts, custom character maps, ligatures, or unusual encodings. This can lead to:

- incorrect symbols;
- missing accented letters;
- words joined or split unexpectedly;
- copied text that looks different from the visible text.

This issue matters when working with multilingual documents or domain-specific symbols.

### 5. Pages can mix text, graphics, and images

A single page may contain:

- selectable text;
- logos and diagrams;
- scanned signatures;
- raster images;
- vector drawings;
- annotations.

The extraction tool must decide what to keep, what to ignore, and how to combine results from different content types.

### 6. Scanned PDFs behave very differently

If a page is just an image, direct PDF text extraction may return:

- nothing;
- very little text;
- garbage characters from hidden OCR layers.

In that case, you need OCR, which introduces its own error sources such as blur, low contrast, skew, and recognition mistakes.

### 7. Real-world PDFs are inconsistent

Two files that both end with `.pdf` may behave completely differently:

- one may be clean digital text;
- one may be a photograph of paper pages;
- one may contain a perfect table;
- one may contain a complex report with floating labels and charts;
- one may be encrypted, damaged, rotated, or poorly generated.

This is why PDF processing pipelines need testing, validation, and fallback strategies.

## Common challenges in Python workflows

When students work with PDFs in Python, the most common difficulties are:

- `extract_text()` returns empty output for scanned files;
- paragraph text loses formatting;
- table columns shift or merge;
- repeated headers appear on every page;
- page numbers get mixed into the main content;
- line breaks create noisy text for later analysis;
- OCR is needed for some pages but not others;
- different libraries produce different results for the same file.

Typical tools in this topic:

- `PyPDF2` for simple page access and text extraction;
- `pdfplumber` for layout inspection and table-oriented work;
- `pandas` for cleaning extracted tabular results;
- OCR tools for image-based pages.

## A practical mindset for PDF work

When processing a PDF, do not start with the assumption that the file is clean text. Start with questions:

1. Is this a digital PDF or a scanned PDF?
2. Do I need plain text, tables, metadata, or all of them?
3. Is the document single-column, multi-column, or highly visual?
4. Do I need OCR for all pages or only some pages?
5. How will I verify that the extracted output is correct?

That mindset is more important than any single library.

## Recommended workflow

For this course topic, a sensible workflow is:

1. Open the file and inspect page count and metadata.
2. Try direct text extraction first.
3. Check whether the output is readable and complete.
4. If the document contains tables, test a table-focused tool.
5. If the file is scanned, switch to OCR.
6. Clean and validate the extracted result before analysis.

## Summary

PDF is a presentation-first format. It is excellent for preserving how a document looks, but that same design often makes automatic extraction difficult.

The main lesson is simple:

- **good visual appearance does not guarantee easy machine reading**.

That is why PDF analysis often combines inspection, extraction, cleaning, validation, and sometimes OCR.
