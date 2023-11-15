import matplotlib.pyplot as plt

# Function to extract phi and buffer values from file name
def extract_values(file_name):
    buffer_value = int(file_name[1:-2])
    phi_value = 0.01 * int(file_name[-2:])
    return buffer_value, phi_value

# Data from the provided text files
file_data = {
    "B10": [
        (1050, 0.000206803),
        (1080, 0.000185114),
        (1095, 0.000207183),
    ],
    "B30": [
        (3050, 0.00020668),
        (3080, 0.000185977),
        (3095, 0.000170091),
    ],
    "B100": [
        (10050, 0.000204663),
        (10080, 0.000203402),
        (10095, 0.000172319),
    ],
}

# Extracting and plotting minIPDT values only from cbr files
for buff_type, data in file_data.items():
    buffer_values = []
    phi_values = []
    minIPDT_values = []

    for buffer, minIPDT in data:
        file_name = f'cbr{buffer}.txt'
        buffer_values.append(buffer)
        phi_values.append(0.01 * (buffer % 100))
        minIPDT_values.append(minIPDT)

    # Plotting
    plt.plot(phi_values, minIPDT_values, marker='o', label=f'{buff_type}')

# Adding labels and legend
plt.xlabel('Phi')
plt.ylabel('minIPDT')
plt.legend()

# Annotating each point with its corresponding x value (phi) under the X-axis
for buff_type, data in file_data.items():
    for i, txt in enumerate(phi_values):
        plt.annotate(f'{txt:.2f}', (phi_values[i], 0), textcoords="offset points", xytext=(0, -15), ha='center', va='bottom')

# Set x-axis ticks to include missing value 0.95
plt.xticks(list(plt.xticks()[0]) + [0.95])

plt.title('minIPDT vs Phi for Different Buffers (from cbr files only)')
plt.show()
