import requests
import sys

# Check if the command-line argument for the base domain is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <base_domain>")
    sys.exit(1)

base_domain = sys.argv[1]

sub_list = open("subdomains.txt").read()
subdoms = sub_list.splitlines()

for sub in subdoms:
    sub_domains = f"http://{sub}.{base_domain}"

    try:
        response = requests.get(sub_domains)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    except (requests.ConnectionError, requests.HTTPError):
        pass
    else:
        print("Valid domain:", sub_domains)
