

```python
import re
import sys
import os

def extract_iocs(text):
    """
    Returns a dictionary of IOCs found in the text:
    IPs, Domains, Emails, MD5, SHA1, SHA256
    """
    patterns = {
        "IPs": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        "Domains": r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b',
        "Emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        "MD5": r'\b[a-fA-F0-9]{32}\b',
        "SHA1": r'\b[a-fA-F0-9]{40}\b',
        "SHA256": r'\b[a-fA-F0-9]{64}\b',
    }

    iocs = {}
    for name, patt in patterns.items():
        iocs[name] = re.findall(patt, text)
    return iocs

def pretty_print(results):
    print("=== Extracted IOCs ===")
    any_found = False
    for ioc_type, values in results.items():
        uniq = sorted(set(values))
        if uniq:
            any_found = True
            print(f"\n{ioc_type}:")
            for v in uniq:
                print(f"  - {v}")
    if not any_found:
        print("No IOCs found.")

if __name__ == "__main__":
    # Accept filename as optional argument
    input_path = sys.argv[1] if len(sys.argv) > 1 else "sample.txt"

    if not os.path.isfile(input_path):
        print(f"Error: الملف '{input_path}' غير موجود. تأكد من المسار أو أنشئ الملف.")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    results = extract_iocs(content)
    pretty_print(results)
