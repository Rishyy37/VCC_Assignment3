import psutil
import time
import requests

THRESHOLD = 75  # percentage
CHECK_INTERVAL = 5  # seconds

# Replace with your cloud VM public IP
CLOUD_API_URL = "http://<CLOUD_VM_IP>:5000/start-instance"


def get_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu, memory


def trigger_cloud():
    try:
        print("🚀 Threshold exceeded! Triggering cloud instance...")
        response = requests.post(CLOUD_API_URL, timeout=5)
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error triggering cloud: {e}")


def monitor():
    print("📊 Monitoring started...")
    while True:
        cpu, memory = get_usage()
        print(f"CPU: {cpu}% | Memory: {memory}%")

        if cpu > THRESHOLD or memory > THRESHOLD:
            trigger_cloud()
            break

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    monitor()