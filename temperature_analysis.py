# Name: [Harsh_Kolte ]
# Roll Number: [IITP_AIMLH_2602288]
# Assignment: Python Loops & Automation

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]


highest = temperatures[0]
lowest = temperatures[0]

# Iterate through each temperature to compare
for temp in temperatures:
    # Check if current temperature is higher than the stored highest
    if temp > highest:
        highest = temp
    
    # Check if current temperature is lower than the stored lowest
    if temp < lowest:
        lowest = temp

print("Highest Temperature:", highest, "°C")
print("Lowest Temperature:", lowest, "°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Initialize counter for hot days
hot_days_count = 0

for temp in temperatures:
    # Skip the iteration if temperature is 30 or below (not hot)
    if temp <= 30:
        continue
    
    # Increment count if temperature is above 30
    hot_days_count = hot_days_count + 1

print("Hot Days (>30°C):", hot_days_count)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

# Initialize counters
hot_days_before_alert = 0
day_counter = 0

for temp in temperatures:
    # Increment day counter (Day 1, Day 2, etc.)
    day_counter = day_counter + 1
    
    # Check for extreme temperature
    if temp >= 40:
        print("Alert! Extreme temperature", temp, "°C detected on Day", day_counter)
        # Stop the loop immediately
        break
    
    # Count as a hot day if above 30 (only runs if break didn't happen)
    if temp > 30:
        hot_days_before_alert = hot_days_before_alert + 1

print("Hot Days before alert:", hot_days_before_alert)