import os

def get_file_data():
    # Data from the provided text files
    file_data = {
        "B10": [],
        "B30": [],
        "B100": [],
    }

    # Read data from text files
    for buff_type in file_data.keys():
        file_name = f'LABY\lab1\{buff_type}.txt'
        if not os.path.exists(file_name):
            continue


        with open(file_name, 'r') as f:
            lines = f.readlines()

            for line in lines:
                if line.startswith('./calc-mgen'):
                    file_command = line.split()[-1]
                    if file_command.endswith('.txt'):
                        buffer_value, phi_value = extract_values(file_command)

                elif "minIPTD" in line:
                    values = line.split()
                    minIPDT_value = float(values[-2]) if values[-2].replace(".", "").isdigit() else None

                    if buffer_value is not None and phi_value is not None and minIPDT_value is not None:
                        file_data[buff_type].append((buffer_value, phi_value, minIPDT_value))

    return file_data

def extract_values(file_name):
    buffer_value = int(file_name[3:-4])
    phi_value = 0.01 * int(file_name[-6:-4])
    return buffer_value, phi_value

# Example usage:
data = get_file_data()
print(data)
