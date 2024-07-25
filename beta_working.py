import re
import sys


def main():
    convert(input("Hours: ").strip())
# 9:00 AM to 5:00 PM

def convert(string):
    pattern = "^([0-9]+(?::| )?(?:[0-9]+)? (?:AM|PM)) to ([0-9]+(?::| )?(?:[0-9]+)? (?:AM|PM))"
    matches = re.match(pattern, string)
    if not matches:
        raise ValueError('invalid format nigga')
    
    print(matches.group(1),matches.group(2), end= '\n\n\n')
    AM_time, _ = matches.group(1).split(' ') 
    print(AM_time)
    if ':' not in AM_time:
        print(f'{AM_time}:00')
    
    AM_hours, AM_mins = AM_time.split(':')
    AM_hours = int(AM_hours)
    AM_mins = int(AM_mins)
    print(AM_hours,'  AND  ',AM_mins)    
    if AM_hours < 12:
        AM_hours += 12
        print(AM_hours)

        # print('monke')

if __name__ == "__main__":
    main()
