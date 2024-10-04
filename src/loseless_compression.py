from pypdf import PdfWriter

base_dir = "base_dir"
writer = PdfWriter(clone_from=base_dir + "file.pdf")

for page in writer.pages:
    page.compress_content_streams()  # This is CPU intensive!

with open(base_dir + "file_compressed.pdf", "wb") as f:
    writer.write(f)
