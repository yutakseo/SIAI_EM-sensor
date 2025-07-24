import subprocess
import numpy as np

def temperature(base_url: str):
    url = f"{base_url}/getStatus=0"
    cmd = ["curl", "--silent", "--http0.9", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    status = result.returncode
    output = result.stdout.strip()

    if status == 28:
        print("time out: connection error")
        return status, np.array([])

    if status != 0 or not output:
        return status, np.array([])

    try:
        values = np.array([
            float(line.strip())
            for line in output.splitlines()
            if line.strip()
        ])
    except ValueError as e:
        print(f"parsing error: {e}")
        return status, np.array([])

    return values
