def compareStrings(garland, flower):
    count = 0
    for char in flower:
        if char in garland:
            count += 1
    return count



2
def get_letter_grade(score):
    if score >= 80:
        return 'A', 4.0
    elif score >= 75:
        return 'B+', 3.5
    elif score >= 70:
        return 'B', 3.2
    elif score >= 65:
        return 'C+', 2.5
    elif score >= 60:
        return 'C', 2.0
    elif score >= 55:
        return 'D+', 1.5
    elif score >= 50:
        return 'D', 1.0
    else:
        return 'F', 0.0


def get_honors_category(cumulative_gpa):
    if cumulative_gpa >= 3.85:
        return 'Summa Cum Laude'
    elif cumulative_gpa >= 3.70:
        return 'Magna Cum Laude'
    elif cumulative_gpa >= 3.50:
        return 'Cum Laude'
    else:
        return 'None'


def calculate_gpa():
    num_courses = int(input("Enter the number of courses: "))
    total_credits = 0
    total_grade_points = 0
    grade_counts = {'A': 0, 'B+': 0, 'B': 0, 'C+': 0, 'C': 0, 'D+': 0, 'D': 0, 'F': 0}

    for _ in range(num_courses):
        numerical_grade = float(input("Enter the numerical grade (out of 100): "))
        credit_weight = float(input("Enter the credit weighting for the course: "))

        letter_grade, grade_point = get_letter_grade(numerical_grade)
        total_credits += credit_weight
        total_grade_points += grade_point * credit_weight
        grade_counts[letter_grade] += 1

        print(f"Course Grade: {letter_grade}, Grade Point: {grade_point}")

    cumulative_gpa = total_grade_points / total_credits
    honors_category = get_honors_category(cumulative_gpa)

    print("\nGrade Counts:")
    for grade, count in grade_counts.items():
        print(f"{grade}: {count}")

    print(f"\nCumulative GPA: {cumulative_gpa:.2f}")
    print(f"Honors Category: {honors_category}")



calculate_gpa()






def calculate_sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

num = int(input("Enter a number: "))

total_sum = calculate_sum(num)

print(f"The sum is {total_sum}.")





def customLen(string):
    count = 0
    for char in string:
        count += 1
    return count


my_string = "Hello, World!"
length = customLen(my_string)
print(length)  

5
for i in range(12):
    for j in range(12):
        print(i*j)


7
def is_vowel(character):
    vowels = ['a', 'e', 'i', 'o', 'u']
    character = character.lower()
    if character in vowels:
        return True
    else:
        return False
    
character1 = 'e'
result1 = is_vowel(character1)
print(result1) 

character2 = 'p'
result2 = is_vowel(character2)
print(result2) 

character3 = 'A'
result3 = is_vowel(character3)
print(result3) 

