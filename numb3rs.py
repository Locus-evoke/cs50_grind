import re
import sys

def main():
    print(validate(input('IPv4 Address: ')))

    
def validate(ip: str):
    pattern = r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$"
    matches = re.search(pattern, ip)

    if not matches:
        return False

    nums: list[str] = []
    for i in range(4):
        nums.append(matches.group(i+1))
    for i in range(4):
        if not( 0 <= int(nums[i]) <= 255):
            return False

    return True
    
if __name__ == "__main__":
    main()
