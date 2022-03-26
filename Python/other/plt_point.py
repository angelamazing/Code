import matplotlib.pyplot as plt

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values,c='red' ,edgecolor='none' , s=100)
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
