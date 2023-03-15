import os
from pdf2image import pdfinfo_from_path, convert_from_path

def convert_pdf_to_images(pdf_file_path, output_folder_path, batch_size=5, backend='imagemagick'):
    """
    Converts a PDF file to a series of JPEG images and saves them in the specified output folder.

    Parameters:
    pdf_file_path (str): The path of the PDF file to be converted.
    output_folder_path (str): The path of the folder where the images will be saved. If the folder doesn't exist, it will be created.
    batch_size (int): The number of pages to convert at a time. Lower values will use less memory but take longer to process.
    backend (str): The backend to use for converting the PDF to images. Options are 'imagemagick' and 'poppler'. 'poppler' is generally faster and produces higher quality images.

    Returns:
    None
    """

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.mkdir(output_folder_path)
        print(f"Directory {output_folder_path} created.")

    # Get information about the PDF file
    pdf_info = pdfinfo_from_path(pdf_file_path)
    num_pages = pdf_info['Pages']

    # Loop through the PDF pages in batches of batch_size
    for i in range(0, num_pages, batch_size):
        start_page = i + 1
        end_page = min(i + batch_size, num_pages + 1)

        # Convert the current batch of pages to images
        images = convert_from_path(pdf_file_path, dpi=300, first_page=start_page, last_page=end_page, poppler_path=backend=='poppler', backend=backend)

        # Save each image in the output folder
        for j, image in enumerate(images):
            page_number = i + j + 1
            file_name = f"page_{page_number}.jpg"
            file_path = os.path.join(output_folder_path, file_name)
            image.save(file_path, "JPEG")
            print(f"Page {page_number} saved as {file_path}.")

    # Remove any remaining PPM files
    _remove_ppm(output_folder_path)

def _remove_ppm(output_folder_path):
    """
    Removes any PPM files in the specified folder.

    Parameters:
    output_folder_path (str): The path of the folder where the PPM files are located.

    Returns:
    None
    """

    for file_name in os.listdir(output_folder_path):
        if file_name.endswith(".ppm"):
            file_path = os.path.join(output_folder_path, file_name)
            os.remove(file_path)
            print(f"Removed {file_path}.")

if __name__ == "__main__":
    # Example usage
    pdf_file_path = "example.pdf"
    output_folder_path = "output_images"
    batch_size = 5
    backend = "poppler"
    convert_pdf_to_images(pdf_file_path, output_folder_path, batch_size, backend)
