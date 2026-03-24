import numpy as np
from sklearn.linear_model import LinearRegression
import sys

# ==========================================================
# 1. MACHINE LEARNING MODULE: GPA PREDICTION (REGRESSION)
# ==========================================================
# Training data: [Study Hours per day, Attendance %]
# Target: GPA (on a 10-point scale for VIT standards)
X = np.array([[5, 90], [2, 70], [8, 95], [1, 60], [4, 85], [6, 80], [7, 88]])
y = np.array([8.5, 7.0, 9.5, 6.0, 8.0, 7.8, 8.9])

model = LinearRegression()
model.fit(X, y)

def predict_gpa():
    print("\n--- [ML Module] Academic Performance Predictor ---")
    try:
        hours = float(input("Enter average daily study hours: "))
        attendance = float(input("Enter current attendance percentage: "))
        
        if not (0 <= attendance <= 100):
            print("Error: Attendance must be between 0 and 100.")
            return

        prediction = model.predict([[hours, attendance]])
        # Ensuring the prediction stays within the 0-10 scale
        final_gpa = max(0, min(10, prediction[0]))
        
        print(f"Predicted GPA: {round(final_gpa, 2)} / 10.0")
        print("Insight: Based on historical data, this is your projected score.")
    except ValueError:
        print("Error: Please enter numeric values for hours and attendance.")

# ==========================================================
# 2. LOGIC MODULE: ACADEMIC & CAREER REASONING (PROLOG SIM)
# ==========================================================
def check_enrollment():
    print("\n--- [Logic Module] Course Enrollment Checker ---")
    name = input("Enter student name: ").lower()
    course = input("Enter target course (e.g., machine_learning): ").lower()
    
    # Simulating the 'can_enroll' rule from knowledge.pl
    # Based on our facts: Drishya has completed math and python.
    if name == "drishya" and course == "machine_learning":
        print(f"Result: SUCCESS! {name.capitalize()} is ELIGIBLE for {course}.")
        print("Reason: Prerequisites (Programming_Python) are met in Knowledge Base.")
    else:
        print(f"Result: PENDING. Prerequisites not yet verified for {course}.")

def suggest_career():
    print("\n--- [Logic Module] Career Roadmap Agent ---")
    name = input("Enter student name: ").lower()
    
    # Simulating the 'suggest_path' rule from knowledge.pl
    if name == "drishya":
        print(f"Hello, {name.capitalize()}! Based on your academic milestones:")
        print(">> Suggested Path: AI Engineer / Digital Product Visualizer (VFX)")
        print(">> Next Logical Goal: Complete 'ai_fundamentals' to unlock advanced paths.")
    else:
        print("User profile not found. Please update knowledge.pl with user facts.")

# ==========================================================
# 3. MAIN INTERFACE: INTELLI-SCHOLAR MENU
# ==========================================================
def main():
    while True:
        print("\n" + "="*40)
        print("       INTELLI-SCHOLAR: AI ADVISOR")
        print("="*40)
        print("1. Predict Academic Performance (ML)")
        print("2. Check Course Enrollment Eligibility")
        print("3. Suggest Career Roadmap (Goal-Based)")
        print("4. Exit Program")
        print("="*40)
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            predict_gpa()
        elif choice == '2':
            check_enrollment()
        elif choice == '3':
            suggest_career()
        elif choice == '4':
            print("\nExiting Intelli-Scholar. Best of luck with your studies, Drishya!")
            sys.exit()
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()