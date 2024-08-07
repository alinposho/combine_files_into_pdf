import fpdf


def combine_files_into_pdf():
    # Create instance of FPDF class
    pdf = fpdf.FPDF()

    # Add a page for each image and include the image
    images = [
        "/path_to/file1.jpg",
        "/path_to/file2.jpg",
        "/path_to/file4.jpg"
    ]

    for image in images:
        pdf.add_page()
        pdf.image(image, x=10, y=10, w=190)

    # Save the PDF
    output_path = "/path_to/combined_document.pdf"
    pdf.output(output_path)

    output_path
