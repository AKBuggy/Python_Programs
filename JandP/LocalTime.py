from datetime import datetime


def difference_in_days(date1, date2):
    return abs((date2 - date1).days)


def main():
    # Get input from the user
    date1_str = input("Enter the first date (YYYY-MM-DD): ")
    date2_str = input("Enter the second date (YYYY-MM-DD): ")

    # Convert input strings to datetime objects
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")

    # Calculate the difference in days
    days_difference = difference_in_days(date1, date2)

    # Print results
    print("First date:", date1)
    print("Second date:", date2)
    print("Difference in days:", days_difference)


# Execute the main function
if __name__ == "__main__":
    main()
