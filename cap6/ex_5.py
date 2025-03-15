str = 'X-DSPAM-Confidence: 0.8475'
found = str.find(':')
number_found = str[found+2:]
f_number = float(number_found)
print(f"{number_found} Number after ': ' ")
print(f"{found} Position of ':' ")
print(f"String of reference '{str}'")
print(f_number)
