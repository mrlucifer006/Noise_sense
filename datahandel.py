import pandas as pd

def check_admin(user_name, pas):
    # Authenticate admin credentials using author.csv
    try:
        df = pd.read_csv("author.csv", index_col=0)  # Load admin credentials CSV
    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the developer....")
        return None  # Return None if CSV file is missing
    for ind in df.index:
        # Check if username and password match
        if df.loc[ind, "admin_id"] == user_name:
            if df.loc[ind, "admin_pass"] == pas:
                return "verified"  # Return "verified" for successful authentication
    return None  # Return None for failed authentication

def check_student(user_name, pas):
    # Authenticate student credentials using student.csv
    try:
        df = pd.read_csv("student.csv", index_col=0)  # Load student credentials CSV
    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the developer....")
        return None  # Return None if CSV file is missing
    for ind in df.index:
        # Check if username and password match
        if df.loc[ind, "student_name"] == user_name:
            if df.loc[ind, "student_pass"] == pas:
                return "verified"  # Return "verified" for successful authentication
    return None  # Return None for failed authentication