# Personal Firewall

## Overview

Personal Firewall is a Python-based network security application designed to monitor network traffic, apply custom filtering rules, and log suspicious activities. The project demonstrates fundamental concepts of network security, packet analysis, traffic monitoring, and firewall rule management.

The firewall allows users to create and manage IP-based and port-based filtering rules while providing real-time visibility into network connections and security events.

## Objectives

* Monitor incoming and outgoing network traffic
* Detect suspicious network activities
* Block connections based on IP addresses and ports
* Maintain detailed security logs
* Provide a user-friendly interface for traffic monitoring
* Demonstrate core firewall concepts and network security principles

## Features

### Traffic Monitoring

* Real-time network connection monitoring
* Traffic analysis and inspection
* Active connection tracking

### Rule Management

* Block specific IP addresses
* Block specific ports
* Dynamic rule updates
* Persistent rule storage

### Logging and Alerts

* Security event logging
* Connection history tracking
* Suspicious activity detection
* Firewall action records

### User Interface

* Firewall status dashboard
* Traffic monitoring panel
* Rule management interface
* Log viewer

## Project Structure

```text
Personal-Firewall/
│
├── README.md
├── requirements.txt
├── LICENSE
│
├── src/
│   ├── firewall.py
│   ├── packet_monitor.py
│   ├── rule_manager.py
│   ├── logger.py
│   └── gui.py
│
├── config/
│   └── rules.json
│
├── logs/
│   └── firewall.log
│
├── screenshots/
│
├── docs/
│
└── tests/
```

## Technologies Used

* Python 3.x
* Scapy
* Psutil
* Socket Programming
* Tkinter
* JSON

## Installation

1. Clone the repository

```bash
git clone https://github.com/Shivansh-sec/Personal-Firewall.git
```

2. Navigate to the project directory

```bash
cd personal-firewall
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python src/firewall.py
```

## Testing

The firewall can be tested using:

* Localhost traffic generation
* Port scanning simulations
* IP blocking verification
* Port blocking verification
* Connection monitoring tests

## Learning Outcomes

* Network Security Fundamentals
* Packet Analysis
* Firewall Design Principles
* Traffic Monitoring
* Security Logging
* Rule-Based Access Control
* Python Security Tool Development

## Future Enhancements

* Machine Learning-Based Threat Detection
* Threat Intelligence Integration
* Advanced Packet Inspection
* Web-Based Dashboard
* Multi-Platform Support

## Author

Cybersecurity Internship Project

## Disclaimer

This project is developed for educational and cybersecurity learning purposes only.
