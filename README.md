# PDFutils

This is a simple, small and offline-only Python tool created for learning purposes.
It provides two simple PDF operations:

* **Join PDFs** (`-j`)
* **Modify PDFs** by selecting specific pages (`-m`)

The program runs fully **locally** and its only dependency is **PyPDF2**, which is currently discontinued but still usable for basic tasks.

You can install PyPDF2 with the following command and start using the tool:

```bash
pip install PyPDF2
```

---

## Usage

### **1. Join multiple PDFs (`-j`)**

Merge several PDF files into a single file.

**Syntax:**

```bash
python PDFutils.py -j <file1.pdf> <file2.pdf> ... <output.pdf>
```

**Example:**

```bash
python PDFutils.py -j doc1.pdf doc2.pdf merged.pdf
```

This produces **merged.pdf** containing all pages from the input files in order.


### **2. Modify PDFs (`-m`)**

Select specific pages from multiple PDFs and build a new one.
The **structure** argument uses the format:

```
PDFindex.PageIndex,PDFindex.PageIndex,...
```

Both indices start at **1**.

**Syntax:**

```bash
python PDFutils.py -m <structure> <file1.pdf> <file2.pdf> ... <output.pdf>
```

**Example (take page 1 of the first PDF and page 2 of the second PDF):**

```bash
python PDFutils.py -m 1.1,2.2,1.3 doc1.pdf doc2.pdf result.pdf
```

This creates **result.pdf** with the selected pages in the given order.
