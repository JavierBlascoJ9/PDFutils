import sys
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def join_pdfs(files, output="result.pdf"):
    try:
        merger = PdfMerger()
        for file in files:
            merger.append(file)
        merger.write(output)
        merger.close()
        print(f"PDFs successfully joined. Saved as: {output}")
    except Exception as e:
        print(f"Error joining PDFs: {e}")

def modify_pdfs(structure, files, output="result.pdf"):
    try:
        writer = PdfWriter()
        pdfs = [PdfReader(file) for file in files]
        
        for item in structure.split(","):
            pdf_idx, page_idx = map(int, item.split("."))
            pdf_idx -= 1
            page_idx -= 1
            
            if 0 <= pdf_idx < len(pdfs) and 0 <= page_idx < len(pdfs[pdf_idx].pages):
                writer.add_page(pdfs[pdf_idx].pages[page_idx])
            else:
                print(f"Warning: Index out of range {item}, is omitted.")
        
        with open(output, "wb") as output_pdf:
            writer.write(output_pdf)
        print(f"PDFs successfully modified. Saved as: {output}")
    except Exception as e:
        print(f"Error modifying PDFs: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Use: python PDFutils.py -j <file1.pdf> <file2.pdf> ... <output.pdf>")
        print("       python PDFutils.py -m <structure> <file1.pdf> <file2.pdf> ... <output.pdf>")
    else:
        option = sys.argv[1]
        if option == "-j":
            files = sys.argv[2:-1]
            output_file = sys.argv[-1]
            join_pdfs(files, output_file)
        elif option == "-m":
            structure = sys.argv[2]
            files = sys.argv[3:-1]
            output_file = sys.argv[-1]
            modify_pdfs(structure, files, output_file)
        else:
            print("Invalid option. Use -j to join or -m to modify PDFs.")
