import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(string):
    pattern = r"^([0-9]+(?::| )?(?:[0-9]+)? (?:AM|PM)) to ([0-9]+(?::| )?(?:[0-9]+)? (?:AM|PM))"
    matches = re.match(pattern, string, re.IGNORECASE)
    if not matches:
        raise ValueError('invalid format nigga')

    if 'AM' in matches.group(1):
        AM_time, _ = matches.group(1).split()
        PM_time, _ = matches.group(2).split()
    else:
        PM_time, _ = matches.group(1).split()
        AM_time, _ = matches.group(2).split()
    if ':' not in AM_time:
        AM_time = f'{AM_time}:00'
    if ':' not in PM_time:
        PM_time = f'{PM_time}:00'
    AM_hours, AM_mins = AM_time.split(':')
    PM_hours, PM_mins = PM_time.split(':')

    if int(AM_hours) == 12:
        AM_hours = 0
    if int(PM_hours) > 12 or int(AM_hours) > 12 or int(AM_mins) > 59 or int(PM_mins) > 59:
        raise ValueError


    if int(PM_hours) != 12:
        PM_hours = int(PM_hours)
        PM_hours += 12
        PM_hours = str(PM_hours)

    if int(AM_hours) < 10:
        AM_hours = f'0{AM_hours}'

    if 'AM' in matches.group(1):
        return f'{AM_hours}:{AM_mins} to {PM_hours}:{PM_mins}'
    else:
        return f'{PM_hours}:{PM_mins} to {AM_hours}:{AM_mins}'

if __name__ == "__main__":
    main()
