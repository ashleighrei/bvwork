import streamlit as st
import os
import fitz  # PyMuPDF
from io import BytesIO
import tempfile

# Custom CSS and Streamlit setup
# ... (same as in your previous code)

# Function to combine PDFs using PyMuPDF
def combine_pdfs(input_files, output_file):
    pdf_pages = []
    try:
        for input_file in input_files:
            pdf_document = fitz.open(input_file)
            pdf_pages.extend(pdf_document)

        # Create a BytesIO buffer to store the combined PDF
        pdf_buffer = BytesIO()
        pdf_document = fitz.open(pdf_buffer)
        pdf_document.insertPDF(pdf_pages)

        # Save the combined PDF with the specified output file name and PDF extension
        pdf_document.save(output_file)

        return True
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return False

# Streamlit app (remaining code remains the same as in your previous code)

# ...

# Display a "Combine" button to combine the PDFs
if st.button("Combine") and input_files:
    # Output file where the combined PDF will be saved
    output_file_path = os.path.join(tempfile.gettempdir(), output_file_name)

    # Call the function to combine the PDFs using PyMuPDF
    if combine_pdfs(input_files, output_file_path):
        st.success("PDFs successfully combined.")
        
        # Display a "Download" button for the combined PDF
        with open(output_file_path, "rb") as file:
            st.download_button(
                label="Download",
                data=file.read(),
                file_name=output_file_name,
            )
else:
    st.warning("Please upload at least one PDF file :)")
