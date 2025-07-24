import subprocess
import numpy as np

def resistor(base_url: str):
    url = f"{base_url}/getResistor=0"
    cmd = ["curl", "--silent", "--http0.9", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    status = result.returncode
    output = result.stdout.strip()

    if status == 28:
        print("time out: connection error")
        return status, np.empty((0, 2))
    if status != 0 or not output:
        return status, np.empty((0, 2))

    try:
        data = np.array([
            list(map(float, line.strip().split()))
            for line in output.splitlines()
            if line.strip()
        ])
    except ValueError as e:
        print(f"parsing error: {e}")
        return status, np.empty((0, 2))

    return data
