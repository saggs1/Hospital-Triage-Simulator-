FILE_NAME = "queue.txt"

def read_queue():
    patients = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, category, wait_time = line.strip().split(",")
                patients.append([name, category, int(wait_time)])
    except FileNotFoundError:
        open(FILE_NAME, "w").close()
    return patients


def write_queue(patients):
    with open(FILE_NAME, "w") as file:
        for p in patients:
            line = f"{p[0]},{p[1]},{p[2]}\n"
            file.write(line)
