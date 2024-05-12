import requests
from time import sleep
from prettytable import PrettyTable

def check_status(subdomains):

    domain = "yourdomain.com"

    table = PrettyTable(["subdomain", "status"])
    
    for sdomain in subdomains:
        url = f"http://{sdomain}." + domain
        try:
            response = requests.get(url)
            if response.status_code == 200:
                status = "UP"
            else:
                status = "DOWN"
        except requests.ConnectionError:
            status = "DOWN"
        
        table.add_row([sdomain, status])
    
    print(table)

def main():
    # add list of subdomains that need to be checked.
    subdomains = ["subdomain1", "subdomain2", "subdomain3"]
    while True:
        check_status(subdomains)
        # Check status every minute. We can change according to requirements.
        sleep(60)

if __name__ == "__main__":
    main()
