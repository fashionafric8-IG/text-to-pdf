import os
from flask import Flask, render_template, request, Response, jsonify
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    data = request.get_json()
    if not data or 'text_input' not in data:
        return jsonify({'error': 'No text provided'}), 400
        
    text = data.get('text_input', '').strip()
    
    if not text:
        return jsonify({'error': 'Please enter some text to generate a PDF.'}), 400
    
    try:
        # Create instance of FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", size=12)
        
        # Replace unsupported characters to prevent UnicodeEncodeError
        safe_text = text.encode('latin-1', 'replace').decode('latin-1')
        
        # Multi_cell handles text wrapping and newlines automatically
        # Passing the entire text block prevents cursor placement issues
        pdf.multi_cell(w=0, h=8, text=safe_text)
        
        # In fpdf2, calling output() with no arguments returns a bytearray
        # We wrap it in bytes() because Flask/Werkzeug expects strictly bytes
        pdf_bytes = bytes(pdf.output())
        
        # Return the raw PDF bytes
        return Response(
            pdf_bytes,
            mimetype='application/pdf',
            headers={
                'Content-Disposition': 'inline; filename="document.pdf"'
            }
        )
        
    except Exception as e:
        return jsonify({'error': f'An error occurred while generating the PDF: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
