# bankmanagmentsystem
Bank Management System using python


# Bank User Payment Merger

This Python program merges two text files to update bank user information with payment details.

## Files

- `main_program.py`: The main script that reads from `file1.txt` and `file2.txt` and generates `output.txt`.
- `file1.txt`: Contains bank user details in the format: `Name, Account Number, Amount`.
- `file2.txt`: Contains payment details in the format: `Name, Amount`.

## Usage

1. Place your `file1.txt` and `file2.txt` in the same directory as `main_program.py`.
2. Run the script with Python: `python main_program.py`.
3. The script will generate a new file `output.txt` with the updated user information.

## Customizing the Input

You can replace the contents of `file1.txt` and `file2.txt` with your own data. Make sure they follow the specified formats.

## Example

- `file1.txt`:
Alice, 12345, 1000
Bob, 67890, 1500


- `file2.txt`:
Alice, 200


After running the script, `output.txt` will contain:
Alice, 12345, 1200
Bob, 67890, 1500


## Note

Ensure that `file1.txt` and `file2.txt` are properly formatted as described.
