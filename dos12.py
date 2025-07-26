import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Target URL
url = 'https://www.thaievisa.go.th/visa/transit-visa'

# Number of total requests and number of concurrent threads
num_requests = 5000
max_workers = 20  # You can tune this (e.g., 200, 300, etc.)

def send_request(index):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"[{index + 1}] ✅ Success: {response.status_code}"
        else:
            return f"[{index + 1}] ❌ Failed: {response.status_code}"
    except Exception as e:
        return f"[{index + 1}] ⚠️ Error: {e}"

# Main execution using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = [executor.submit(send_request, i) for i in range(num_requests)]
    for future in as_completed(futures):
        print(future.result())

print("🚀 All requests completed.")
