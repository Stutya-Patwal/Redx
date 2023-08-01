# Redx Ethical Hacking Tool Documentation

Redx is an ethical hacking tool designed to assist security professionals and ethical hackers in performing various tasks related to network reconnaissance, IP address lookup, port scanning, and more. This terminal-based tool provides a range of functionalities for security analysis and information gathering.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Available Commands](#available-commands)
- [Redx Chatbot (beta)](#Redx-Chatbot-Beta)

## Introduction 

Redx is a Python-based ethical hacking tool that facilitates the process of gathering information about targets, conducting IP address lookups, scanning ports, and more. It is designed for ethical purposes only and should not be used for malicious activities. Redx can be run from the terminal and provides a user-friendly interface for interacting with its functionalities.

## Getting Started 
1. Clone the Redx repository from [GitHub](https://github.com/Stutya-Patwal/Redx).
2. Install the required dependencies using `pip` by running `pip install -r requirements.txt`.
3. Run the Redx tool by executing the `main.py` file.

## Available Commands

Here are some of the available commands you can use with Redx:

- `iplookup -location <IP>`: Performs a geolocation lookup for the specified IP address.
- `iplookup <IP>`: Retrieves information about the specified IP address.
- `scan -ip <target> <start_port> <end_port>`: Scans ports within the specified range for the target IP.
- `exit`: Exits the Redx tool.
- `help`: Displays the Redx help message.
- `is_valid_email <email>`: Checks if the given email address is valid.
- `is_valid_url <url>`: Checks if the given URL is valid.
- `ping_ip <IP>`: Pings the specified IP address and displays the result.
- `dns_lookup <domain>`: Performs a DNS lookup for the specified domain.
- `get_external_ip`: Retrieves the external/public IP address of the current system.
- `my_ip`: Displays information about the current IP address of the system.
- `get_ssl_certificate_expiry <domain>`: Retrieves the SSL certificate expiry days for the specified domain.
- `generate_random_user_agent`: Generates a random User-Agent for HTTP requests.
- `is_valid_ipv4 <IP>`: Checks if the given IP address is a valid IPv4 address.
- `find_subdomains <domain>`: Finds subdomains for the specified domain.
- `is_private_ip <IP>`: Checks if the given IP address is a private IP.
- `ip_to_int <IP>`: Converts the given IPv4 address to an integer representation.

## Redx Chatbot Beta

The Redx Chatbot Beta is an AI-powered assistant integrated into the Redx Ethical Hacking Tool, offering real-time support for ethical hacking tasks. To access the chatbot, type (help -redx) in the Redx terminal. It understands user queries using NLP and delivers relevant responses, continuously learning from user feedback. Empowering users with personalized recommendations, the chatbot enhances security assessments while adhering to ethical guidelines.

**Note:** The Redx Chatbot Beta is currently available to select users for testing and improvement.

**Note:** Ensure you use these commands responsibly and solely for ethical hacking and security assessment purposes.

May your journey with Redx be fruitful and secure! Happy ethical hacking with Redx!

**Disclaimer:** The Redx tool is intended for ethical hacking purposes only. The developers and contributors are not responsible for any misuse or illegal activities carried out using this tool. Always ensure that you have appropriate authorization to perform security assessments on any target systems.
