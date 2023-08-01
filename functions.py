import requests
import socket
import whois
import re
import subprocess
import ssl
import datetime
import ipaddress
import dns.resolver
import random

RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY"
IPAPI_BASE_URL = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

def generate_random_user_agent():
    user_agents = [
        # Add a list of user-agent strings here
        # Example:
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        # ...
    ]
    return random.choice(user_agents)

def is_private_ip(ip_address):
    try:
        ip = ipaddress.IPv4Address(ip_address)
        return ip.is_private
    except ipaddress.AddressValueError:
        return False

def get_http_headers(url):
    try:
        response = requests.head(url)
        return response.headers
    except requests.exceptions.RequestException:
        return None

def is_local_port_open(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('127.0.0.1', port))
            return result == 0
    except socket.error:
        return False

def ip_to_int(ip_address):
    try:
        return int(ipaddress.IPv4Address(ip_address))
    except ipaddress.AddressValueError:
        return None

def find_subdomains(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        subdomains = [rdata.target.to_text()[:-1] for rdata in answers]
        return subdomains
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return None

def is_valid_ipv4(ip_address):
    try:
        ipaddress.IPv4Address(ip_address)
        return True
    except ipaddress.AddressValueError:
        return False

def get_ssl_certificate_expiry(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                remaining_days = (expiry_date - datetime.datetime.now()).days
                return remaining_days
    except (ssl.SSLError, socket.gaierror):
        return None

def get_external_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        if response.status_code == 200:
            return response.json()['ip']
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def my_ip():
    url = IPAPI_BASE_URL
    querystring = {"apikey": RAPIDAPI_KEY}
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
    }
    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        return data
    except requests.exceptions.RequestException:
        return None

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

def is_valid_url(url):
    url_pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/?.*$'
    return re.match(url_pattern, url) is not None

def ping_ip(ip_address):
    try:
        output = subprocess.check_output(["ping", "-c", "4", ip_address], universal_newlines=True)
        return "Success" in output
    except subprocess.CalledProcessError:
        return False

def dns_lookup(domain):
    try:
        ip_addresses = socket.gethostbyname_ex(domain)[-1]
        return ip_addresses
    except socket.gaierror as e:
        return None

def ip_address_lookup(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def print_ip_info(data):
    if data:
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        print("Error: Unable to retrieve IP information.")

def scan_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                result = s.connect_ex((ip_address, port))
                if result == 0:
                    open_ports.append(port)
        except socket.error:
            pass
    return open_ports

def reverse_dns_lookup(ip_address):
    try:
        hostnames = socket.gethostbyaddr(ip_address)
        return hostnames[0]
    except socket.herror as e:
        return None

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except whois.parser.PywhoisError as e:
        return None

def geoip_mapping(ip_address):
    url = f"https://ipapi.co/{ip_address}/json/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def print_geoip_info(data):
    if data:
        print("Geographical Information:")
        print(f"IP Address: {data['ip']}")
        print(f"City: {data['city']}")
        print(f"Region: {data['region']}")
        print(f"Country: {data['country_name']} ({data['country_code']})")
        print(f"Latitude: {data['latitude']}")
        print(f"Longitude: {data['longitude']}")
    else:
        print("Error: Unable to retrieve GeoIP information.")
