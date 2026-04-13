import fitz
doc = fitz.open(r'c:\Users\kj anand\Downloads\Data analysis.pdf')
for n, page in enumerate(doc):
    for i, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        with open(f"pdf_img_{n}_{i}.{base_image['ext']}", "wb") as f:
            f.write(base_image["image"])
