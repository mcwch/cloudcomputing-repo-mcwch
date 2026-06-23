import requests

def observe_https_cycle(url):
    """Sends a GET request and prints HTTP response details."""
    response = requests.get(url)

    if response.status_code == 200:
        print(f"HTTP Status Code: {response.status_code} (Success)")
        print(f"Headers:\n{response.headers}")

        content = response.text.strip()
        print(f"\nContent Preview:\n{content[:100]}...")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    url = "https://extension.berkeley.edu/"
    observe_https_cycle(url)