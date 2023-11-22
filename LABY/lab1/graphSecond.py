import matplotlib.pyplot as plt
from data import file_data
import os


def extract_data(file_data, origin, buffor, metric):
    data = file_data.get(origin, {}).get(metric, {}).get(buffor, [])
    return data

def draw_chart(file_data, origin, buffor):
    minIPDT_data = extract_data(file_data, origin, buffor, "minIPDT")
    avgIPDT_data = extract_data(file_data, origin, buffor, "avgIPDT")

    x_minIPDT = [int(str(value[0])[-2:]) * 0.01 for value in minIPDT_data]
    y_minIPDT = [value[1] for value in minIPDT_data]

    x_avgIPDT = [int(str(value[0])[-2:]) * 0.01 for value in avgIPDT_data]
    y_avgIPDT = [value[1] for value in avgIPDT_data]

    plt.plot(x_minIPDT, y_minIPDT, marker='o', linestyle='-', label=f"{origin}_{buffor}_minIPDT")
    plt.plot(x_avgIPDT, y_avgIPDT, marker='o', linestyle='-', label=f"{origin}_{buffor}_avgIPDT")

# Draw charts for each combination of origin and buffor
origins = ["cbr", "pois"]
buffors = ["B10", "B30", "B100"]

plt.figure(figsize=(15, 10))  # Set the figure size for better visibility

for origin in origins:
    for buffor in buffors:
        plt.subplot(2, 3, buffors.index(buffor) + 1 + origins.index(origin) * 3)  # Adjust subplot index
        draw_chart(file_data, origin, buffor)

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'MinIPDT and AvgIPDT for {origin}_{buffor}')
        plt.xticks([0.5, 0.8, 0.95])  # Set x-axis ticks
        plt.legend()


save_dir = 'my_plots'
os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist
plt.savefig(os.path.join(save_dir, f'ALLSIX.png'))
plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()
