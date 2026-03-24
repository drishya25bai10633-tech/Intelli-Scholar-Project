% --- Facts ---
prerequisite(mathematics, ai_fundamentals).
prerequisite(programming_python, ai_fundamentals).
prerequisite(ai_fundamentals, machine_learning).

% --- Updated Student Progress ---
completed(drishya, mathematics).
completed(drishya, programming_python).

% --- Rules ---
can_enroll(Student, Course) :- 
    prerequisite(Pre, Course), 
    completed(Student, Pre).

% Rule: Career path suggestions (Logic Representation)
suggest_path(Student, ai_engineer) :- 
    completed(Student, ai_fundamentals).