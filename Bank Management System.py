# Title         : Bank Management System
# Purpose       : A program that will manage and display individual
#                 banking information, including names, account numbers,
#                 and total amounts, through various options
#                 such as reading files, searching records.
# Programmer    : Ashish
# Date          : 2023-12-03
# Reference     :

# Pseudocode:
#1. Read and display content from the first file.
#2. Read and display content from the second file line by line.
#3. User can search details for individual
#4. Deposit amount individually in the second file.
#5. Create a third file by combining data from the first and second files.
#6. Display content of the third file.
#7. Repeat the program until user choice is 7.


# Constants for menu choices
READ_1ST_FILE = 1
READ_2ND_FILE = 2
SEARCH = 3
DEPOSITE = 4
CREATE_3RD_FILE = 5
DISPLAY = 6
END = 7
FIRST_FILE = 'data.txt'
SECOND_FILE = 'weekly_pay.txt'

# _________________________________________________________________________#

def read_first_file():
    file = open(FIRST_FILE, 'r')
    file_contents = file.read()

    # Check if the file is empty or not
    if file_contents:
        print()
        print('-'*72)
        print(f'\t{"Name":<15}{"Account Number":<25}{"Amount"}')
        print('-'*72)

        for line in file_contents.split('\n'):
            values = line.strip().split(', ')
            if len(values) == 3:
                name, acc_number, amount = values
                try:
                    amount = float(amount)
                    print(f'\t{name:<15}{acc_number:<25}{amount:10,.2f}')
                except:
                    print(f'\t{name:<15}{acc_number:<25}{"Invalid amount"}')

        print('-'*72)
    else:
        print('File "data.txt" is empty.')

    file.close()
# _________________________________________________________________________#

def read_second_file_line_by_line():
    file = open(SECOND_FILE, 'r')
    
    print('-'*45)
    print(f'\t{"Name":<15}{"Amount"}')
    print('-'*45)

    # Read each line of the file
    for line in file:
        values = line.strip().split(', ')
        if len(values) == 2:
            name, amount = values
            try:
                amount = float(amount)
                print(f'\t{name:<15}{amount:10,.2f}')
            except ValueError:
                print(f'\t{name:<15}{"Invalid amount"}')

    print('-'*45)
    file.close()
# _________________________________________________________________________#

def search_record(find, file):
    for line in file:
        # Split the line into name, account_number, and amount
        name, account_number, amount = line.strip().split(', ')

        # Check if the user input name is in the file or not
        if find.strip() == name.strip():
            print('\nRecord found:')
            print('-'*45)
            print(f'Name           : {name}')
            print(f'Account Number : {account_number}')
            print(f'Amount         : ${float(amount):,.2f}')
            print('-'*45)
            return
        
    print('-'*45)        
    print('█▀▀ █▀█ █▀█ █▀█ █▀█')
    print('██▄ █▀▄ █▀▄ █▄█ █▀▄')
    print('*** No record found ***')
    print('-'*45)
# _________________________________________________________________________#

def search():
    find = input('Enter the name to search: ')

    try:
        file_output = open('output.txt', 'r')
        search_record(find, file_output)
        file_output.close()
    except:
        file_data = open(FIRST_FILE, 'r')
        search_record(find, file_data)
        file_data.close()
# _________________________________________________________________________#

def deposit_individually():
    infile = open(SECOND_FILE, 'r')
    lines = infile.readlines()
    infile.close()

    name = input('Enter the name for deposit: ')

    modified_lines = []
    name_not_found_message = ('█▀▀ █▀█ █▀█ █▀█ █▀█\n'
                              '██▄ █▀▄ █▀▄ █▄█ █▀▄\n'
                              '*** No record found ***')

    for line in lines:
        # Split the line into components
        values = line.strip().split(', ')

        if len(values) >= 2:
            old_name, old_amount = values[0], values[1]

            # Check if the input name matches the current line's name
            if name == old_name:
                amount = float(input('Enter the amount to deposit: '))
                # Reset the not found message if the name is found
                name_not_found_message = ''  
                old_amount = float(old_amount) + amount

            # Update the line with the new amount
            line = f'{old_name}, {old_amount}\n'

        else:
            print(f'ERROR: Invalid line format - {line}')

        modified_lines.append(line)
    print('-'*45)
    print(name_not_found_message)
    print('-'*45)

    outfile = open(SECOND_FILE, 'w')
    outfile.writelines(modified_lines)
    outfile.close()
# _________________________________________________________________________#

def create_third_file():
    infile1 = open(FIRST_FILE, 'r')
    first_file_data = infile1.readlines()

    infile2 = open(SECOND_FILE, 'r')
    second_file_data = infile2.readlines()

    outfile = open('output.txt', 'w')

    # Create a dictionary to store data from the first file
    first_file_dict = {}
    for line in first_file_data:
        name, acc_num, amt = line.strip().split(', ')
        first_file_dict[name] = {'Account Number': acc_num, 'Amount': float(amt)}

    # Write combined data to the third file
    for name, record in first_file_dict.items():
        acc_num = record['Account Number']
        total_amt = record['Amount']

        # Check if the record is in the second file
        for line in second_file_data:
            sec_name, weekly_pay = line.strip().split(', ')
            if name == sec_name:
                total_amt += float(weekly_pay)

        # Write to the output file in the required format
        outfile.write(f'{name}, {acc_num}, {total_amt:.2f}\n')

    infile1.close()
    infile2.close()
    outfile.close()
    print('Third file creation completed.')
# _________________________________________________________________________#

def display_third_file():
    # Display data from output.txt (after weekly_pay)
    print('\nData from output.txt (after weekly_pay):\n')
    print('-'*75)
    print(f'\t{"Name":<15}{"Account Number":<25}{"Amount"}')
    print('-'*75)

    file = open('output.txt', 'r')
    for line in file:
        values = line.strip().split(',')
        name = values[0].strip()
        acc_number = values[1].strip()
        amount = float(values[2].strip())
        print(f'\t{name:<15}{acc_number:<25}{amount:10.2f}')

    file.close()
    print('-'*75)
# _________________________________________________________________________#

def display_menu():
    print()
    print('*'*75)
    print('\n\tENTER A NUMBER TO CHOOSE YOUR OPTIONS:')
    print('\t1. Read first file and display its content')
    print('\t2. Read second file and display its content')
    print('\t3. Search by name [Find details]')
    print('\t4. Deposit/ Add amount in second file')
    print('\t5. Create third file')
    print('\t6. Display content of the third file')
    print('\t7. End program')
    print('*'*75)

# _________________________________________________________________________#

def main():
    print('\n'+'✿'*43)
    print('✿\t\t\t  Bank Management System\t\t\t  ✿')
    print('✿\t\t\t      Programmed by:\t\t\t\t  ✿')
    print('✿'*43)
    
    choice = 0

    while choice != 7:
        display_menu()
        choice = int(input('Enter your choice: '))
        print('*'*75)

        if choice == READ_1ST_FILE:
            read_first_file()
        elif choice == READ_2ND_FILE:
            read_second_file_line_by_line()
        elif choice == SEARCH:
            search()
        elif choice == DEPOSITE:
            deposit_individually()
        elif choice == CREATE_3RD_FILE:
            create_third_file()
        elif choice == DISPLAY:
            display_third_file()
        elif choice == END :
            print('THANK YOU!!!')
        else:
            print('ERROR: ***Invalid choice***')

    print('Exiting the program...')
    print('*'*75)

# _________________________________________________________________________#

main()
