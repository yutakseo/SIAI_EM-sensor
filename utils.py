import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



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



def plot_base(data, xlabel="samples", ylabel="value"):
    plt.figure(figsize=(12, 6))
    for i in range(data.shape[1]):
        plt.plot(data.index, data.iloc[:, i], label=data.columns[i], alpha=0.7)
    
    plt.xlabel(xlabel, fontsize=12)
    plt.xlim(data.index.min(), data.index.max())
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()


def plot(title, data, xlabel="samples", ylabel="value"):
    plot_base(data, xlabel=xlabel, ylabel=ylabel)
    plt.title(title, fontsize=16)
    
    plt.show()
    return None


def plot_with_local(title, data, xlabel="samples", ylabel="value", threshold=100):
    plot_base(data, xlabel=xlabel, ylabel=ylabel)
    plt.title(title, fontsize=16)
    
    from scipy.signal import argrelextrema

    for i in range(data.shape[1]):
        y = data.iloc[:, i].values
        x = data.index.values
        label = data.columns[i]

        max_idx = argrelextrema(y, np.greater, order=threshold)[0]
        min_idx = argrelextrema(y, np.less, order=threshold)[0]

        plt.plot(x[max_idx], y[max_idx], 'ro', label=f"{label} max" if i == 0 else None)
        plt.plot(x[min_idx], y[min_idx], 'bo', label=f"{label} min" if i == 0 else None)

        for idx in max_idx:
            plt.text(x[idx], y[idx], f'{y[idx]:.2f}', fontsize=8, color='red')
        for idx in min_idx:
            plt.text(x[idx], y[idx], f'{y[idx]:.2f}', fontsize=8, color='blue')
    
    plt.show()
    return None