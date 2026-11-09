
# ==========================================
# SMART GRADE CALCULATOR
# Python Project
# ==========================================

def get_number(message, minimum=0, maximum=None):
    """Accept and validate numeric input."""
    while True:
        try:
            value = float(input(message))

            if value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value cannot exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_grade(percentage):
    """Convert percentage into grade."""

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_percentage(total_marks, max_marks):
    """Calculate overall percentage."""

    if max_marks == 0:
        return 0

    return (total_marks / max_marks) * 100


def calculate_cgpa(percentage, divisor=9.5):
    """Convert percentage into approximate CGPA."""

    return min(10, percentage / divisor)


def calculate_percentile(student_percentage, peer_scores):
    """
    Calculate percentile rank based on comparison scores.
    Percentile = (Below + 0.5 * Equal) / Total * 100
    """

    if not peer_scores:
        return None

    below = sum(
        1 for score in peer_scores
        if score < student_percentage
    )

    equal = sum(
        1 for score in peer_scores
        if score == student_percentage
    )

    return ((below + 0.5 * equal) / len(peer_scores)) * 100


def display_subject_performance(subjects):
    """Display individual subject performance."""

    print("\n========== SUBJECT PERFORMANCE ==========")

    for subject in subjects:
        percentage = calculate_percentage(
            subject["marks"],
            subject["maximum"]
        )

        grade = get_grade(percentage)

        print(f"\nSubject: {subject['name']}")
        print(f"Marks: {subject['marks']}/{subject['maximum']}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")

        if percentage >= 80:
            print("Performance: Excellent")
        elif percentage >= 60:
            print("Performance: Good")
        elif percentage >= 50:
            print("Performance: Average")
        else:
            print("Performance: Needs Improvement")


def display_overall_result(name, total, maximum, percentage):
    """Display overall student result."""

    print("\n========== OVERALL RESULT ==========")

    print("Student Name:", name)
    print(f"Total Marks: {total:.2f}/{maximum:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", get_grade(percentage))


def main():

    print("=" * 45)
    print("       SMART GRADE CALCULATOR")
    print("=" * 45)

    # Student information
    name = input("\nEnter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    number_of_subjects = int(
        get_number("Enter number of subjects: ", 1)
    )

    subjects = []

    total_marks = 0
    maximum_marks = 0

    # Subject information
    for i in range(number_of_subjects):

        print(f"\nEnter details for Subject {i + 1}")

        subject_name = input("Subject name: ").strip()

        while not subject_name:
            subject_name = input(
                "Subject name cannot be empty. Enter again: "
            ).strip()

        max_marks = get_number(
            "Enter maximum marks: ", 0.01
        )

        marks = get_number(
            "Enter obtained marks: ",
            0,
            max_marks
        )

        subjects.append({
            "name": subject_name,
            "marks": marks,
            "maximum": max_marks
        })

        total_marks += marks
        maximum_marks += max_marks

    # Calculate overall percentage
    percentage = calculate_percentage(
        total_marks,
        maximum_marks
    )

    # Menu
    while True:

        print("\n" + "=" * 45)
        print("              MAIN MENU")
        print("=" * 45)

        print("1. Calculate Percentage")
        print("2. Calculate Grade")
        print("3. Calculate CGPA")
        print("4. Calculate Percentile")
        print("5. View Subject-wise Performance")
        print("6. View Complete Result")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":

            print("\nYour Percentage:",
                  f"{percentage:.2f}%")

        elif choice == "2":

            print("\nYour Grade:", get_grade(percentage))

        elif choice == "3":

            divisor = get_number(
                "\nEnter CGPA conversion divisor "
                "(default CBSE approximation = 9.5): ",
                0.01
            )

            cgpa = calculate_cgpa(percentage, divisor)

            print(f"\nYour CGPA: {cgpa:.2f}/10")

        elif choice == "4":

            print("\nEnter comparison students' percentages.")
            print("Enter their scores one by one.")

            count = int(
                get_number(
                    "Number of comparison students: ", 1
                )
            )

            peer_scores = []

            for i in range(count):

                score = get_number(
                    f"Enter percentage of student {i + 1}: ",
                    0,
                    100
                )

                peer_scores.append(score)

            percentile = calculate_percentile(
                percentage,
                peer_scores
            )

            print(
                f"\nYour Percentile: {percentile:.2f}"
            )

        elif choice == "5":

            display_subject_performance(subjects)

            # Identify best and weakest subjects
            percentages = [
                calculate_percentage(
                    subject["marks"],
                    subject["maximum"]
                )
                for subject in subjects
            ]

            best_index = percentages.index(max(percentages))
            weakest_index = percentages.index(min(percentages))

            print("\nBest Subject:",
                  subjects[best_index]["name"])

            print("Needs Most Improvement:",
                  subjects[weakest_index]["name"])

        elif choice == "6":

            display_overall_result(
                name,
                total_marks,
                maximum_marks,
                percentage
            )

            print("\nCGPA (9.5 conversion):",
                  f"{calculate_cgpa(percentage):.2f}")

            display_subject_performance(subjects)

        elif choice == "7":

            print("\nThank you for using Smart Grade Calculator!")
            break

        else:

            print("\nInvalid choice. Please select 1 to 7.")


# Run the application
if __name__ == "__main__":
    main()
    