import matplotlib.pyplot as plt
import mysql.connector

# Welcome!
input = [1, 2, 3, 4, 5, 6]
numbers = [1, 4, 9, 16, 25, 36]

plt.style.use("bmh")
fig, axs = plt.subplots()
axs.plot(input, numbers, linewidth=5)
axs.set_title("calculations of squares", fontsize=14)
axs.set_xlabel("Numbers", fontsize=14)
axs.set_ylabel("Squares", fontsize=14)
axs.tick_params(axis="both", labelsize=16)
plt.show()
