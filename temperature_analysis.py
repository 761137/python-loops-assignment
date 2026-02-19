# Name: Suvedha
# Roll Number: [Your Roll Number]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
max_temp=temperatures[0]
min_temp=temperatures[0]
for temp in temperatures:
    if temp>max_temp:
        max_temp=temp
    if temp<min_temp:
        min_temp=temp
print(f"Highest Temperature: {max_temp}°C")
print(f"Lowest Temperature: {min_temp}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
count=0
for temp in temperatures:
    if temp>30:
        count=count+1
    else:
        continue
print("Hot Days (>30°C): ",count)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
count=0
day=0
for i,temp in enumerate(temperatures):
    if temp>30 and temp<40:
        count=count+1   
    if temp>=40:
            break;
print("Hot Days before alert: ",count)
print(f"Alert! Extreme temperature 40°C detected on Day {i+1}")
    