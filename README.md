# Phish Hunter

## 📌 Overview  
This repository contains a Python-based tool designed for **ethical security research** to simulate the automated submission of randomly generated usernames and passwords to a specified web form.  

The credentials are generated using the `Faker` library, providing **realistic but fictitious** user data. This tool can help security professionals **test phishing site resilience, analyze automated credential submission behaviors, and demonstrate credential-stuffing risks** in a controlled, ethical environment.  

## ⚡ Features  
✅ **Automated Credential Generation** – Uses the `Faker` library to generate usernames and passwords with custom parameters.  
✅ **Automated Form Submission** – Continuously submits credentials to a specified URL.  
✅ **Customizable Submission Rate** – Configure the number of login attempts per minute.  
✅ **Customizable URL** – User can Enter the Desired URL (Contains a default URL).

## 🔬 Intended Use  
This tool is intended **strictly for ethical security research and educational purposes** under the following conditions:  
✔️ You have **explicit authorization** to test the target system.  
✔️ You are conducting research within a **legal and ethical** framework.  
✔️ The tool is used **only in controlled, research-approved environments**.  

## ⚠️ Ethical & Legal Disclaimer  
By using this tool, you agree to the following:  
- **Authorization Required** – This must **only** be used on systems where you have **explicit permission**.  
- **No Illegal Use** – Unauthorized testing on third-party sites **is illegal** and against ethical hacking guidelines.  
- **Compliance** – You must comply with local and international cybersecurity laws (e.g., **CFAA**, **GDPR**, **Computer Misuse Act**).  
- **Research-Only** – This tool is for **educational demonstrations** and **security research**. Misuse can result in **legal consequences**.  

## 🛠️ Installation  

1️⃣ Clone this repository:  
```bash
git clone https://github.com/gokulkannant/phishhunter.git
cd phishhunter
```

2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```

3️⃣ Run the script:  
```bash
python main.py --url "http://example-phishing-site.com/login" --count 10
```

## 🚀 Usage Example  
```bash
python main.py --url "http://example-site.com/login" --count 10
```
- `--url` – Target phishing website URL (for research purposes **only**).  
- `--count` – Number of submissions per minute (adjustable).  

## 📜 License  
This project is licensed under the **MIT License**. See the **LICENSE** file for details.  

## 🛑 Warning  
**Misuse of this tool for unauthorized activities is illegal.** The maintainers are **not responsible** for any consequences resulting from unethical or unlawful use. **Use responsibly!**  

