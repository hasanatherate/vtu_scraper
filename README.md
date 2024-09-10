Here’s a draft for your **README** file that includes both the **PDF Downloader Scraper** and the **PDF to Excel Sheet** script. It explains the purpose, installation steps, and usage for each script.

---

# VTU Results Scraper & PDF to Excel Converter

This repository contains two Python-based scripts:
1. **VTU Results PDF Downloader**: Automatically fetches and downloads VTU student result PDFs from the VTU results website.
2. **PDF to Excel Converter**: Extracts data from downloaded PDFs and converts them into an Excel sheet for easier analysis.

## Table of Contents
- [VTU Results PDF Downloader](#vtu-results-pdf-downloader)
    - [Features](#features)
    - [Installation](#installation)
    - [Usage](#usage)
- [PDF to Excel Converter](#pdf-to-excel-converter)
    - [Installation](#installation-1)
    - [Usage](#usage-1)
- [License](#license)

## VTU Results PDF Downloader

### Features
- Automates fetching student result PDFs from the VTU results page.
- Bypasses CAPTCHA through manual user input, allowing the user to enter CAPTCHA on the website.
- Iterates through multiple USN numbers and saves result PDFs in a specified folder.
- Downloads PDFs without triggering the print dialog box.
- Saves files with the format `result_[USN].pdf` in a designated folder.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/repo-name.git
    cd repo-name
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.9+ installed. Then install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Google Chrome Installation**:
   Ensure that Google Chrome is installed, as this script uses the Chrome WebDriver.

4. **Configure the WebDriver**:
   Ensure the appropriate version of ChromeDriver is installed to match your Chrome version:
   ```bash
   pip install webdriver-manager
   ```

5. **CAPTCHA Solving Service (Optional)**:
   You may integrate a CAPTCHA solving service like CapSolver for automation, but the script currently allows manual CAPTCHA input.

### Usage

1. **Update USN Range**:
    In the `main()` function, modify the `roll_numbers` list to include the USN range you want to iterate through:
    ```python
    def main():
        for i in range(1, 26):
            usn_number = f'1BI22VL0{str(i).zfill(2)}'
            fetch_results(usn_number)
    ```

2. **Run the Script**:
   To start downloading result PDFs:
    ```bash
    python pdf_downloader.py
    ```

   The PDFs will be saved in `/Users/abdul/Downloads/automated_pdfs/` with the filenames `result_[USN].pdf`.

---

## PDF to Excel Converter

### Features
- Extracts tabular data from multiple result PDFs.
- Saves extracted data into a structured CSV or Excel file for further processing.

### Installation

1. **Install Required Libraries**:
    The script uses `pdfplumber` for PDF extraction and `pandas` for data manipulation:
    ```bash
    pip install pdfplumber pandas openpyxl
    ```

### Usage

1. **Ensure PDFs are Stored**:
   Ensure that all the downloaded result PDFs are stored in `/Users/abdul/Downloads/automated_pdfs/`.

2. **Run the Script**:
   To extract data from the PDFs and save it to an Excel file:
    ```bash
    python pdf_to_excel.py
    ```

3. **Output**:
   The script will create an Excel file with the extracted data from the PDFs at the specified location.

---

## License
This project is licensed under the MIT License.

---

Let me know if you need any more adjustments or details in the README!
