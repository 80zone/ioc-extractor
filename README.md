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

ioc-extractor/
│── extractor.py   # Main Python script
│── sample.txt     # Example input file
│── README.md      # Project documentation
│── LICENSE        # MIT License
│── DISCLAIMER.md  # Disclaimer file
---

## ⚙️ Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ioc-extractor.git
   cd ioc-extractor
   
python extractor.py

python extractor.py mylog.txt

User login from 192.168.1.10
Suspicious domain: evil-site.com
Contact: hacker@mail.com
Malware hash (MD5): 44d88612fea8a8f36de82e1278abb02f
Another IP: 8.8.8.8
Sample sha1: da39a3ee5e6b4b0d3255bfef95601890afd80709
Sample sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

=== Extracted IOCs ===

IPs:
  - 192.168.1.10
  - 8.8.8.8

Domains:
  - evil-site.com

Emails:
  - hacker@mail.com

MD5:
  - 44d88612fea8a8f36de82e1278abb02f

SHA1:
  - da39a3ee5e6b4b0d3255bfef95601890afd80709

SHA256:
  - e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

🔮 Future Improvements
	•	Export results to CSV or JSON
	•	Read .log or .pdf files directly
	•	CLI options to select specific IOC types
	•	Integration with Threat Intelligence feeds

⚠️ Disclaimer

This project is for educational purposes only and is not intended for malicious use.
Use it only with files you are authorized to access. The author is not responsible for misuse.

Author

Created by wijdan - Cybersecurity & Digital Forensics enthusiast.
