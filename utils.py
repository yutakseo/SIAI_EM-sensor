import pandas as pd
import numpy as np


import pandas as pd
import numpy as np

def save_to_csv(data, columns: list[str], filename: str) -> bool:
    if data is None or not isinstance(data, np.ndarray) or data.size == 0:
        print(f"[Warning] Failed to save {filename}: empty or invalid data.")
        return False

    try:
        if data.ndim == 1:
            data = data.reshape(-1, 1)

        if data.shape[1] != len(columns):
            print(f"[Warning] Failed to save {filename}: shape mismatch.")
            return False

        df = pd.DataFrame(data, columns=columns)
        df.to_csv(filename, index=False)
        print(f"[Info] Saved data to {filename}.")
        return True
    except Exception as e:
        print(f"[Error] Failed to save {filename}: {e}")
        return False

