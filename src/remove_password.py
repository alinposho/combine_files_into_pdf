import pikepdf


def example():
    file_path = 'filepath'
    pdf = pikepdf.open(file_path, allow_overwriting_input=True, password='password')
    pdf.save(file_path)
