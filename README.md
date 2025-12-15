# phish-Detector
# ⚡ Phish Detector ⚡

### Advanced Threat Intelligence Tool (Powered by VirusTotal API)



Phish Detector is a Python-based command-line utility designed to perform rapid and deep security analysis of any given URL or link using the vast threat intelligence database of VirusTotal. It goes beyond simple "clean" or "malicious" verdicts by providing crucial details on which specific security engines flagged the link, its redirection path, and its categorization. 

---

## ✨ Features

* **Deep Scan:** Utilizes over 70+ security engines available through the VirusTotal API for comprehensive URL scanning.
* **Detailed Verdict:** Provides clear counts for Malicious, Suspicious, and Harmless detections.
* **Threat Intelligence Table:** Lists the specific security vendors (e.g., Google Safe Browsing, Kaspersky) that identified the link as phishing or malware, along with the detection method.
* **Site Intelligence:** Displays key website metadata including the Page Title, the Final Redirect URL (crucial for detecting URL masking), and the site's official category.
* **Neon Hacker Theme:** Leverages the `rich` library to deliver an attractive, stylish, and easily readable output in the terminal.
* **Cross-Platform:** Designed to run smoothly on Linux, Windows, macOS, and Termux environments.

---

## 🛠️ Setup and Configuration

git clone [https://github.com/mrtan-official/phish-Detector.git](https://github.com/mrtan-official/phish-Detector.git)
cd phish-Detector
python phish-Detector [url]

## 👨‍💻 Developed By

Mr Tan
GitHub Profile: [https://www.google.com/search?q=https://github.com/mrtan-official/] <-- Insert Your GitHub Profile Link Here
<!-- end list -->


Install the necessary Python libraries using the following command:

```bash
pip install requests rich


