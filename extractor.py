import re

def extract_iocs(text):
    iocs = {
        "IPs": re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text),
        "Domains": re.findall(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', text),
        "Emails": re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text),
        "MD5": re.findall(r'\b[a-fA-F0-9]{32}\b', text),
        "SHA1": re.findall(r'\b[a-fA-F0-9]{40}\b', text),
        "SHA256": re.findall(r'\b[a-fA-F0-9]{64}\b', text),
    }
    return iocs

if __name__ == "__main__":
    try:
        with open("sample.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: sample.txt not found. أضف ملف sample.txt في نفس المجلد ثم شغّل السكربت.")
        exit(1)

    results = extract_iocs(content)

    print("=== Extracted IOCs ===")
    for ioc_type, values in results.items():
        if values:
            print(f"\n{ioc_type}:")
            for v in sorted(set(values)):
                print(f"  - {v}")
