# Add line border to all pages of a pdf file
import fitz  # PyMuPDF

def add_border_to_pdf(input_pdf_path, output_pdf_path, border_margin=20, border_width=1):
    """
    Add a rectangular line border to all pages of a PDF.
    
    Args:
        input_pdf_path: Path to input PDF
        output_pdf_path: Path to save output PDF
        border_margin: Distance from page edge to the border line (in points)
        border_width: Thickness of the border line (in points)
    """
    doc = fitz.open(input_pdf_path)
    
    for page in doc:
        rect = page.rect
        # Create a rectangle inside the page with the specified margin
        border_rect = fitz.Rect(
            border_margin,
            border_margin,
            rect.width - border_margin,
            rect.height - border_margin
        )
        # Draw the rectangle border (black color)
        page.draw_rect(border_rect, color=(0, 0, 0), width=border_width)
    
    doc.save(output_pdf_path)
    doc.close()

add_border_to_pdf('input.pdf', 'output.pdf')
