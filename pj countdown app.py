from datetime import datetime

date_today = datetime.today()


def calc_deadline():
    deadline_date = date_deadline_dict["date"]
    goal = date_deadline_dict["goal"]
    deadline = datetime.strptime(deadline_date, "%d.%m.%Y")

    if deadline > date_today:
        days_to_deadline = deadline - date_today
        print(f"{days_to_deadline.days} days remaining to accomplish goal:{goal}")
    else:
        print("U fucked up")


input_value = input("Enter goal and deadline\n")
input_list = input_value.split(":")
date_deadline_dict = {"goal": input_list[0], "date": input_list[1]}
calc_deadline()