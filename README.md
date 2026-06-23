# 🛡️ Personal Firewall 

A Python-based Personal Firewall Security Dashboard designed to monitor active network connections, manage firewall rules, generate security alerts, and maintain activity logs through an interactive graphical interface.

---

## 📌 Overview

The Personal Firewall Security Dashboard is a cybersecurity-focused application developed using Python. The project demonstrates fundamental firewall management and network monitoring concepts while providing a simple and user-friendly interface for managing security rules.

The application allows users to:

* Monitor active network connections in real time
* Manage blocked IP addresses and ports
* Generate security alerts based on configured rules
* Record and review firewall activity logs
* View network activity statistics through a graphical dashboard

---

## 🚀 Features

### Real-Time Connection Monitoring

* Displays active network connections
* Shows local and remote endpoints
* Displays connection status information

### Firewall Rule Management

* Add blocked IP addresses
* Remove blocked IP addresses
* Add blocked ports
* Remove blocked ports

### Security Alerts

* Detect blocked IP activity
* Detect blocked port activity
* Display alerts in real time

### Logging System

* Record application events
* Store security-related alerts
* Maintain firewall activity logs

### Dashboard Statistics

* Active Connections
* Firewall Rules
* Alert Count
* Application Uptime

---

## 🛠️ Technologies Used

* Python
* Tkinter
* Psutil
* JSON
* Git
* GitHub

---

## 📂 Project Structure

```text
Personal-Firewall/
│
├── src/
│   ├── firewall.py
│   ├── gui.py
│   ├── logger.py
│   ├── packet_monitor.py
│   ├── rule_manager.py
│   └── __init__.py
│
├── config/
│   └── rules.json
│
├── logs/
│   └── firewall.log
│
├── tests/
│   ├── test_logger.py
│   ├── test_monitor.py
│   └── test_rules.py
│
├── docs/
│   ├── Project_Report.pdf
│   ├── User_Manual.pdf
│   └── Architecture_Diagram.png
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Shivansh-sec/Personal-Firewall.git
```

Navigate to the project directory:

```bash
cd Personal-Firewall
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the firewall dashboard:

```bash
python -m src.firewall
```

---

## 🔒 Security Capabilities

The current implementation includes:

* Real-time connection monitoring
* Firewall rule management
* Blocked IP detection
* Blocked port detection
* Event logging
* Dashboard-based monitoring

---

## 📚 Documentation

Additional documentation is available in the `docs/` directory:

* Project Report
* User Manual
* Architecture Diagram

---

## 📈 Future Improvements

Potential enhancements include:

* Enhanced traffic analysis
* Improved alert classification
* Advanced reporting features
* Additional monitoring capabilities
* Extended logging functionality

---

## 👨‍💻 Author

**Shivansh**

B.Tech Computer Science Engineering Student
Cyber Security Enthusiast

---

## 📄 License

This project is licensed under the MIT License.
