
import matplotlib.pyplot as plt
import numpy as np

cant_productos = [100, 150, 200, 300, 500]
precio = [4000, 7000, 9000, 12000, 15000]

plt.plot(cant_productos)
plt.show()

# personalisar graficas
plt.plot(cant_productos, precio, color="green", marker="o", linestyle="dashed", linewidth=2, markersize=12)
plt.title("ventas de walmart")
plt.xlabel("cantidad productos")
plt.xlabel("precio")
plt.show()
