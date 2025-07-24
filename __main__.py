from time import sleep
from current import current
from resistor import resistor
from temperature import temperature
from voltage import voltage
from utils import save_to_csv

def sensor():
    url = "http://115.145.159.149:8888"

    I = current(url)
    save_to_csv(I, columns=["Current(A)"], filename="results/current.csv")
    sleep(4)

    R = resistor(url)
    save_to_csv(R,  columns=["Current(A)", "Resistance(Ohm)"], filename="results/resistor.csv")
    sleep(4)

    T = temperature(url)
    save_to_csv(T,  columns=["Temperature(C)"], filename="results/temperature.csv")
    sleep(4)

    V = voltage(url)
    save_to_csv(V,  columns=["Input Voltage(V)", "Output Voltage(V)"], filename="results/voltage.csv")

if __name__ == "__main__":
    sensor()
