# 🛡️ IOC Extractor

A **Python-based IOC Extractor** designed for SOC analysts and Digital Forensics investigations.  
Automates the detection of **IPs, domains, emails, and file hashes** from log or text files.

---

## 🚀 Features
- Extracts:
  - IPv4 addresses
  - Domains
  - Emails
  - MD5 / SHA1 / SHA256 hashes
- Reads input from a text file
- Clean and structured output for easier analysis
- Can be extended to export results to CSV/JSON

---


## 📂 Project Structure
```markdown
ioc-extractor/
├── extractor.py   # Main Python script
├── sample.txt     # Example input file
├── README.md      # Project documentation
├── LICENSE        # MIT License
└── DISCLAIMER.md  # Disclaimer fil
```

## ⚙️ Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ioc-extractor.git
   cd ioc-extractor
   
```bash
python extractor.py
python extractor.py mylog.txt
```

## 🔮 Future Improvements
- Export results to CSV or JSON
- Read `.log` or `.pdf` files directly
- CLI options to select specific IOC types
- Integration with Threat Intelligence feeds

---

## ⚠️ Disclaimer
This project is for educational purposes only and is not intended for malicious use.
Use it only with files you are authorized to access. The author is not responsible for misuse.

---

---

## Author
Created by **wijdan** - Cybersecurity & Digital Forensics enthusiast.
