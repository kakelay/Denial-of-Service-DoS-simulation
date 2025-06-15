import requests

# Replace this URL with the website you want to request
url = 'http://localhost:8080/account/api/v1/portal/get/account'

# Number of requests
num_requests = 1000

for index, _ in enumerate(range(num_requests)):
    try:
        response = requests.get(url)
        # You can add more code here to process the response, if needed
        if response.status_code == 200:
            print(f"[{index + 1}] Request successful: {response.status_code}")
        else:
            print(f"[{index + 1}] Request failed: {response.status_code}")
    except Exception as e:
        print(f"[{index + 1}] An error occurred: {e}")

print("All requests completed.")
