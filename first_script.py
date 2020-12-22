SALARY_RAISE_FACTOR = 0.05
STATE_CODE_MAP = {"NEWYORK": "NY", "Los Angeles": "LA"}

def update_employee_record(rec):
    old_sal = rec["salary"]
    new_sal = old_sal * (1 + SALARY_RAISE_FACTOR) 
    rec["salary"] = new_sal
    state_code = rec["state_code"]
    rec["state_name"] = STATE_CODE_MAP[state_code]

input_data = [
    {"employee_name" : "Ryan", "salary": 100000.0, state_code: "LA"},
    {"employee_name" : "Apeach", "salary": 44000.0, state_code: "NT"}
]

for rec in input_data:
    update_employee_record(rec)
    name = rec["employee_name"]
    salary = rec["salary"]
    state = rec["state_name"]
    print(name + 'now employee lives in' + state)
    print('     and make $' + str(salary))
