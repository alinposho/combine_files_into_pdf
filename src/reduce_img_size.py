import os

from pypdf import PdfWriter

base_folder = "base_dir"


def compress_pdf(file_name):
    writer = PdfWriter(clone_from=base_folder + file_name)

    for page in writer.pages:
        for img in page.images:
            img.replace(img.image, quality=10)

    with open(base_folder + file_name + "_img_size_reduced.pdf", "wb") as f:
        writer.write(f)


for file in os.listdir(base_folder):
    if file.endswith(".pdf"):
        print(f"Compressing: {file}")
        compress_pdf(file)

