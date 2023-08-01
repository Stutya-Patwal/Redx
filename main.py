from functions import *

def print_banner():
    print('''
Redx Terminal v1.0.0
(C) 2023 Redx Corporation. All rights reserved.
''')

def iplookup_command(command):
    terms = command.split()
    print("")
    print(print_ip_info(ip_address_lookup(terms[1])))

def scan_command(command):
    terms = command.split()
    print("")
    if terms[1] == "-ip":
        target = terms[2]
        start = terms[3]
        end = terms[4]
        print(scan_ports(target, start, end))
    elif terms[1] == "-email":
        print("not available")

def help_this_poor_human(command):
    print('''\nWelcome to Redx - Your Ethical Hacking Ally!
If this is your first time using Redx, we highly recommend exploring our comprehensive tutorial available at https://redx.org/1.0/tutorial for a smooth start.
For assistance from our advanced AI, the Redx Chatbot, simply type (help -redx) in the prompt.
May your hacking journey be fruitful and secure! Happy hacking with Redx!

Ai chatbot help: (help -redx)
    ''')

print_banner()

while True:

    command = input("\nhackit> ")

    if "iplookup -location" in command:
        command = command.replace("iplookup","")
        command = command.replace("-location","")
        print(geoip_mapping(command))
    elif "iplookup" in command:
        iplookup_command(command)
    elif "scan" in command:
        scan_command(command)
    elif "exit" in command:
        break
    elif "help" in command:
        terms = command.split()
        try:
            if terms[1] == "-redx":
                print("We are sorry but redx (chatbot)  is not available. Fore")
            else:
                help_this_poor_human(command)
        except:
            help_this_poor_human(command)
    elif "is_valid_email" in command:
        terms = command.split()
        if len(terms) == 2:
            print(f"Is Valid Email: {is_valid_email(terms[1])}")
    elif "is_valid_url" in command:
        terms = command.split()
        if len(terms) == 2:
            print(f"Is Valid URL: {is_valid_url(terms[1])}")
    elif "ping_ip" in command:
        terms = command.split()
        if len(terms) == 2:
            print(f"Ping Result for IP {terms[1]}: {ping_ip(terms[1])}")
    elif "dns_lookup" in command:
        terms = command.split()
        if len(terms) == 2:
            print(f"DNS Lookup for Domain {terms[1]}: {dns_lookup(terms[1])}")
    elif "get_external_ip" in command:
        print(f"External IP: {get_external_ip()}")
    elif "my_ip" in command:
        ip_data = my_ip()
        print("\nCurrent IP Information:")
        print_ip_info(ip_data)
    elif "get_ssl_certificate_expiry" in command:
        terms = command.split()
        if len(terms) == 2:
            expiry_days = get_ssl_certificate_expiry(terms[1])
            if expiry_days is not None:
                print(f"SSL Certificate Expiry Days: {expiry_days}")
            else:
                print("Error: Unable to get SSL certificate expiry.")
    elif "generate_random_user_agent" in command:
        print(f"User-Agent: {generate_random_user_agent()}")
    elif "is_valid_ipv4" in command:
        terms = command.split()
        if len(terms) == 2:
            print(f"Is Valid IPv4: {is_valid_ipv4(terms[1])}")
    elif "find_subdomains" in command:
        terms = command.split()
        if len(terms) == 2:
            subdomains = find_subdomains(terms[1])
            if subdomains is not None:
                print(f"Subdomains for {terms[1]}: {', '.join(subdomains)}")
            else:
                print(f"Error: Unable to find subdomains for {terms[1]}.")
    elif "is_private_ip" in command:
        terms = command.split()
        if len(terms) == 2:
            print(f"Is Private IP: {is_private_ip(terms[1])}")
    elif "ip_to_int" in command:
        terms = command.split()
        if len(terms) == 2:
            int_ip = ip_to_int(terms[1])
            if int_ip is not None:
                print(f"IPv4 Address {terms[1]} to Integer: {int_ip}")
            else:
                print(f"Error: Unable to convert {terms[1]} to an integer IP.")
