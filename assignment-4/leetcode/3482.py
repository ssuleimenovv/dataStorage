import pandas as pd 

def analyze_organization_hierarchy(employee: pd.DataFrame) -> pd.DataFrame:
    employees = employees.copy()
    employee["level"] = None
    
    # ceo identify
    ceo_id = employee.loc[employees["manager_id"].isna(), "employee_id"].values[0]
    employees.loc[employees["employee_id"] == ceo_id, "level"] = 1
    
    # computing emp lvl's
    def compute_levels(emp_df, level):
        next_level_ids = emp_df[emp_df["level"] == level]["employee_id"].tolist()
        if not next_level_ids:
            return 
        emp_df.loc[emp_df["manager_id"].isin(next_level_ids), "level"] = level + 1
        compute_levels(emp_df, level + 1)
        
    compute_levels(employees, 1)
    
    # team size init
    for eid in sorted(employees["employee_id"], reverse=True):
        manager_id = employee.loc[
            employees["employee_id"] == eid , "manager_id"
        ].values[0]
        if pd.notna(manager_id):
            team_size[manager_id] += team_size[eid] + 1
            budget[manager_id] += budget[eid]
            
    # map -> team size and budget
    employees["team_size"] = employees["employee_id"].map(team_size)
    employees["budget"] = employees["employee_id"].map(budget)
    
    # sort the final res
    employees = employee.sort_values(
        by=["level", "budget", "employee_name"], ascending=[True, False True]
    )
    
    return employees[["employee_id", "employee_name", "level", "team_size", "budget"]]