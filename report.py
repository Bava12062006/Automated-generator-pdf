from fpdf import FPDF
import csv

# Function to read data from a CSV file
def read_csv(file_name):
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read headers
        for row in reader:
            data.append(row)
    return headers, data

# Function to generate a PDF report
def generate_pdf_report(file_name, headers, data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, "Automated Report", ln=True, align="C")
    pdf.ln(10)  # Add a line break

    # Table Header
    pdf.set_font("Arial", style="B", size=12)
    for header in headers:
        pdf.cell(40, 10, header, border=1, align="C")
    pdf.ln()

    # Table Data
    pdf.set_font("Arial", size=12)
    for row in data:
        for item in row:
            pdf.cell(40, 10, str(item), border=1, align="C")
        pdf.ln()

    # Save the PDF
    pdf.output(file_name)
    print(f"PDF report '{file_name}' generated successfully!")

# Main function
def main():
    csv_file = "data.csv"  # Input CSV file name
    pdf_file = "report.pdf"  # Output PDF file name

    # Read data from CSV
    try:
        headers, data = read_csv(csv_file)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
        return

    # Generate PDF report
    generate_pdf_report(pdf_file, headers, data)

# Run the script
if __name__ == "__main__":
    main()
