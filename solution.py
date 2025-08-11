import pandas as pd

# Load employee and attendance data
def load_employees(file_path):
    return pd.read_csv("C:\\Users\\Ascendion\\Desktop\\Employee_attendance_Analysis\\data\\employees.csv")

def load_attendance(file_path):
    return pd.read_csv("C:\\Users\\Ascendion\\Desktop\\Employee_attendance_Analysis\\data\\employees.csv")

# Merge employee and attendance records
def merge_employees_attendance(employees_df, attendance_df):
    merged_df = pd.merge(employees_df, attendance_df, on='EmployeeID')
    print(merged_df) 
    return merged_df

# Total hours worked per department
def total_hours_per_department(merged_df):
    return merged_df.groupby('Department')['HoursWorked'].sum().reset_index()

# Calculate attendance rate per employee
def attendance_rate(merged_df):
    merged_df['AttendanceRate'] = (merged_df['DaysPresent'] / merged_df['WorkingDays']) * 100
    return merged_df[['EmployeeID', 'Name', 'DaysPresent', 'WorkingDays', 'AttendanceRate']]

# Aggregate hours worked per employee
def hours_agg_per_employee(merged_df):
    return merged_df.groupby(['EmployeeID', 'Name'])['HoursWorked'].agg(['mean', 'max', 'min']).reset_index()

# Average age by job role
def avg_age_by_role(employees_df):
    return employees_df.groupby('JobRole')['Age'].mean().reset_index()

# Total attendance entries per employee
def total_attendance_entries(attendance_df):
    return (
        attendance_df['EmployeeID']
        .value_counts()
        .reset_index()
        .rename(columns={'index': 'EmployeeID', 'EmployeeID': 'EntryCount'})
        [['EmployeeID', 'EntryCount']]
    )

# Top performers based on hours worked
def top_performers(merged_df):
    return merged_df.groupby(['EmployeeID', 'Name'])['HoursWorked'].sum().reset_index().sort_values('HoursWorked', ascending=False).head(3)

# Average attendance rate per department
def avg_attendance_rate_per_department(merged_df):
    merged_df['AttendanceRate'] = (merged_df['DaysPresent'] / merged_df['WorkingDays']) * 100
    return merged_df.groupby('Department')['AttendanceRate'].mean().reset_index()

# Late arrival ratio per employee
def late_arrival_ratio(merged_df):
    total_days = merged_df.groupby('EmployeeID').size()
    late_days = merged_df.groupby('EmployeeID')['Late'].sum()
    return (late_days / total_days).reset_index(name='LateArrivalRatio')