import requests
from datetime import datetime

# List of URLs to monitor
urls = [
    "https://example.com",
    "https://api.example.com/health"
]

def check_application(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            status = "UP"
        else:
            status = f"DOWN (HTTP {response.status_code})"
    except requests.RequestException as e:
        status = f"DOWN (Exception: {e})"
    return status

def main():
    print(f"Application Health Check - {datetime.now()}")
    for url in urls:
        status = check_application(url)
        print(f"{url} -> {status}")

if __name__ == "__main__":
    main()
