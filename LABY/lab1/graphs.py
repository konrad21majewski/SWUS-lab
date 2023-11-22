import os
import matplotlib.pyplot as plt
from data import get_data

# Function to extract phi and buffer values from file name
def extract_values(file_name):
    buffer_value = int(file_name[1:-2])
    phi_value = 0.01 * int(file_name[-2:])
    return buffer_value, phi_value


def make_plot_pls(origin, type):
    file_data = get_data(origin, type)
    # Extracting and plotting minIPDT values only from cbr files
    for buff_type, data in file_data.items():
        buffer_values = []
        phi_values = []
        minIPDT_values = []

        for buffer, minIPDT in data:
            buffer_values.append(buffer)
            phi_values.append(0.01 * (buffer % 100))
            minIPDT_values.append(minIPDT)

        # Plotting
        plt.plot(phi_values, minIPDT_values, marker='o', label=f'{buff_type}')

    # Adding labels and legend
    plt.xlabel('Rho')
    plt.ylabel(type)
    plt.legend()

    # Annotating each point with its corresponding x value (phi) under the X-axis
    for buff_type, data in file_data.items():
        for i, txt in enumerate(phi_values):
            plt.annotate(f'{txt:.2f}', (phi_values[i], 0), textcoords=None, xytext=(0, -15), ha='center', va='bottom')

    # Set x-axis ticks to include missing value 0.95
    plt.xticks(list(plt.xticks()[0]) + [0.95])

    if type == iplr:
        plt.ylim(0, 0.0155)
    elif type == minn or type == avg:
        plt.ylim(0, 0.0009)
    elif type == ipdv:
        plt.ylim(0, 0.0021)

    plt.title(f'{type} od Phi dla różnych Bufforów (pliki: {origin})')
    save_dir = 'my_plots'
    os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist

    plt.savefig(os.path.join(save_dir, f'{origin}-{type}.png'))
    plt.show()

if __name__ == "__main__":

    cbr = "cbr"
    pois = "pois"
    avg = "avgIPDT"
    minn = "minIPDT"
    iplr = "IPLR"
    ipdv = "IPDV95"
    
    # make_plot_pls(cbr, avg)
    # make_plot_pls(cbr, minn)
    # make_plot_pls(cbr, iplr)
    # make_plot_pls(cbr, ipdv)


    # make_plot_pls(pois, avg)
    # make_plot_pls(pois, minn)
    # make_plot_pls(pois, iplr)
    # make_plot_pls(pois, ipdv)