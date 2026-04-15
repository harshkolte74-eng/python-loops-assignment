# Task 1: Calculate the average for each student
def process_scores(students):
    averages = {}
    for name, scores in students.items():
        # Calculate average: sum of scores divided by number of scores
        avg = sum(scores) / len(scores)
        # Round to 2 decimal places as requested
        averages[name] = round(avg, 2)
    return averages

# Task 2: Assign a letter grade based on the average
def classify_grades(averages):
    # Defining thresholds inside the function (local variables)
    top_grade = 90
    passing_upper = 75
    passing_lower = 60
    
    results = {}
    for name, avg in averages.items():
        if avg >= top_grade:
            grade = "A"
        elif avg >= passing_upper:
            grade = "B"
        elif avg >= passing_lower:
            grade = "C"
        else:
            grade = "F"
        # Store both average and grade in a tuple
        results[name] = (avg, grade)
    return results

# Task 3: Print the final report
def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    passed_count = 0
    total = len(classified)
    
    for name, (avg, grade) in classified.items():
        # Determine PASS or FAIL
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
            
        # Format the output string for clean columns
        print(f"{name:<10} | Avg: {avg:>6.2f} | Grade: {grade} | Status: {status}")
        
    print("=" * 32)
    print(f"Total Students : {total}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total - passed_count}")
    
    return passed_count

# --- Main Block: Running the Program ---
if __name__ == "__main__":
    # Example student data
    data = {
        "Alice": [85, 90, 82, 88],
        "Bob": [60, 65, 60, 65],
        "Clara": [95, 98, 92, 100]
    }

    # Step 1: Process scores
    averages_dict = process_scores(data)
    
    # Step 2: Classify into grades
    classified_dict = classify_grades(averages_dict)
    
    # Step 3: Generate the final report
    generate_report(classified_dict)