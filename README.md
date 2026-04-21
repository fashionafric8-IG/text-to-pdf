# Beginner-Friendly Text to PDF Generator

A clean, modern, and production-ready web application built with Python (Flask) and Tailwind CSS that allows users to instantly convert plain text into nicely formatted PDF documents.

## Features
- **Frontend**: Clean, responsive 2-column UI using Tailwind CSS with real-time PDF preview.
- **Backend**: Lightweight, stateless Python backend using Flask.
- **PDF Engine**: Uses `fpdf2` for reliable PDF generation.
- **UX Improvements**: AJAX/Fetch for seamless updates, live word count, custom filename input, loading states, and embedded preview via iframe.

## Prerequisites
- Python 3.7 or higher installed on your system.

## Setup Instructions

1. **Navigate to the project directory** (if you aren't already there):
   ```bash
   cd text-to-pdf
   ```

2. **Create a Virtual Environment (Recommended but optional)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Open in Browser**:
   Open your web browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How to Use
1. Paste or type your text into the text area.
2. (Optional) Provide a custom filename.
3. Click "Generate Preview". The PDF will be rendered in the right pane without reloading the page.
4. If you need changes, edit your text and click "Update Preview".
5. When satisfied, click the "Download PDF" button to save it to your computer.

## Project Structure
- `app.py`: The main Flask server and routes.
- `requirements.txt`: List of Python dependencies.
- `templates/index.html`: The frontend HTML UI styled with Tailwind CSS.
