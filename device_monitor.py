"Simulated Device Monitoring and Alert System for CPP102 Week 17."


def get_initial_readings():
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def add_reading(readings, lowest, highest):
    text = input("Enter new reading: ")
    print()
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    elif int(text) < lowest or int(text) > highest:
        print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
    else:
        readings.append(int(text))
        print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def compute_percentage(count, total_count):
    return count / total_count * 100


def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_menu():
    print()
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()


def display_readings(readings):
    print()
    print("CURRENT READINGS")
    print("----------------")
    position = 1
    for reading in readings:
        print(f"Reading {position}: {reading} °C")
        position = position + 1


def display_classifications(readings, warning_limit, critical_limit):
    print()
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(f"{reading} °C -> {category}")


def display_summary(readings, warning_limit, critical_limit):
    count = len(readings)
    normal_count = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning_count = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical_count = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    print()
    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {count}")
    print(f"Total of readings   : {compute_total(readings)}")
    print(f"Average temperature : {compute_average(readings):.2f} °C")
    print(f"Minimum temperature : {find_minimum(readings)} °C")
    print(f"Maximum temperature : {find_maximum(readings)} °C")
    print()
    print(f"NORMAL   : {normal_count} ({compute_percentage(normal_count, count):.2f}%)")
    print(f"WARNING  : {warning_count} ({compute_percentage(warning_count, count):.2f}%)")
    print(f"CRITICAL : {critical_count} ({compute_percentage(critical_count, count):.2f}%)")
    print()
    print(f"Overall Status: {determine_overall_status(warning_count, critical_count)}")


def main():
    "Run the menu and connect the device-monitoring functions."
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
