from collections import Counter

LOG_FILE = "30daysPython/day10/sample_log.txt"
REPORT_FILE = "report.txt"

import os
print(os.getcwd())


def analyze_log(file_name):
    error_count = 0
    warning_count = 0
    info_count = 0

    errors = []

    try:
        with open (file_name , "r") as file:
            lines = file.readlines()

        total_logs = len(lines)

        for line in lines:
            if "ERROR" in line:
                error_count += 1
                errors.append (line.strip())

            elif "WARNING" in line:
                warning_count += 1

            elif "INFO" in line:
                info_count += 1

        print("\n======== LOG SUMMARY ========")
        print (f"Total Log Entries : {total_logs}")
        print (f"INFO Messages : {info_count}")
        print (f"WARNING Message : {warning_count}")
        print (f"ERROR Message : {error_count}")

        if errors:
            common_error = Counter(errors).most_common(1)[0]
            print("\nMost Common Error: ")
            print(f"{common_error[0]} ({common_error[1]} times)")

        else:
            common_error = ("No errors founs", 0)
            print("\nNo errors found.")

        save_report(
            total_logs,
            info_count,
            warning_count,
            error_count,
            common_error,
        )

    except FileNotFoundError:
        print("Log file not found.")

def save_report(total , info ,warning , error , common):
    with open (REPORT_FILE,"w") as report:
        report.write("========= LOG ANALYSIS REPORT ========\n\n")
        report.write(f" Total logs : {total}\n")
        report.write(f"  INFO: {info}\n")
        report.write(f" WARNING : {warning}\n")
        report.write(f" ERROR : {error}\n")
        report.write(f" Most Common Error\n")
        report.write(f"  {common[0]}\n")
        report.write(f" Occurred : {common[1]}time(s)\n")

    print (f"\nReport saved successfully as '{REPORT_FILE}'")

analyze_log(LOG_FILE)