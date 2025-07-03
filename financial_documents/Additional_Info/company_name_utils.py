import csv

def load_company_names(csv_path):
    """Load exact company names from the Company_Filings.csv file."""
    names = set()
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get('name')
            if name:
                names.add(name.strip())
    return sorted(names)
