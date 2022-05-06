with open("/Users/celestegeorge/Downloads/vs/w11/hr_system.txt") as system:
    for info in system:
        info = info.strip()
        details = info.split()

        name = details[0]
        id_number = int(details[1])
        job_title = details[2]
        salary = float(details[3])

        if job_title == "Engineer":
            paycheck = (salary / 24) + 1000
        else:
            paycheck = (salary / 24)

        print(f"{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}")