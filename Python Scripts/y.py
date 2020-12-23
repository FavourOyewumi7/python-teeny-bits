file = r'C:\Users\user\Downloads\numbers.txt'

with open(file, 'r') as f:
    notes = f.readlines()
    for line in notes:
        print(line)
    
