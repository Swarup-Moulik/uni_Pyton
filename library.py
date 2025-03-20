late_days = int(input("Enter the number of days late :- "))
book_num = int(input("Enter the number of books :- "))
if late_days <= 5:
    fine = 0.50*book_num*late_days
    print("Fine incurred :- ",fine)
elif 6 <= late_days <= 10:
    fine = 1 * book_num * late_days
    print("Fine incurred :- ", fine)
elif 10 < late_days <= 30:
    fine = 5 * book_num * late_days
    print("Fine incurred :- ", fine)
else:
    print("Membership is cancelled")
