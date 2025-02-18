def grade_converter(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 50 <= score < 60:
        return 'E'
    elif 0 <= score < 50:
        return 'F'
    else:
        return 'Invalid score'

if __name__ == "__main__":
    score = int(input("Enter the score (0-100): "))
    print(f"The grade is: {grade_converter(score)}")