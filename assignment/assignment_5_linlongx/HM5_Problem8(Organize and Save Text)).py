def save_text_to_file(pdf_path, output_path):
    text = extract_text(pdf_path)
    with open(output_path, 'w') as file:
        file.write(text)