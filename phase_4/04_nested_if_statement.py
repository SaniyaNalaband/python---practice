citizen = True
age = 20 
if age>=20:
    if citizen:
        print("You are citizen")



age = 15
citizen = True
if age >=18:
    if citizen:
        print('You can vote')



age = 5
citizen = True
if age>=18:
    if citizen:
        print('you can vote')
    else:
        print('Citizen required')
else:
    print('Age must be 18 or above ')





username = 'San'
password = 'Python123'
if username == 'San':
    if password == 'Python123':
        print('Login successfull')
    else:
        print('password is incorrect')
else:
    print('username is incorrect')



balance = 50000
withdraw = 20000
if balance>=withdraw:
    pin = 1234
    if pin == 1234:
        print('Transaction successufll')
    else:
        print('incorrect pin')
else:
    print('insufficient balance')




balance = 50000
amount = 20000
if balance>=amount:
    otp_varified = True
    if otp_varified:
        print('Transaction successfull')
    else:
        print('otp varification failed')
else:
    print('Insufficient balance')




logged_in = True
payment_done = True
if logged_in:
    if payment_done:
        print('Order confirmed')
    else:
        print('complete the payment')
else:
    print('Please login')


marks = 80
attendence = 90
if marks>=35:
    if attendence >=70:
         print('Pass')
    else:
          print('attendence shortage')
else:
    print('Fail')




door_unlocked = True
finger_print_verified =  True
if door_unlocked:
    if finger_print_verified:
        print('Access granted ')
    else:
        print('fingerprint verification failed')
else:
    print('door locked')



age = 28
salary = 65000
credit_score = 780
if age>20:
    if salary >= 6000:
        if credit_score>750:
            print('Loan approved')
        else:
            print('credit score is too low ')
    else:
        print('Salary is low')
else:
    print('You are not elligible')





marks = 92
entrance_exam = True
documents_verified = True
if marks>75:
    if entrance_exam:
        if documents_verified:
            print('Admission Confirmed')
        else:
            print('Document veriy unsuccessfull')
    else:
        print('Entrance exam not cleared')
else:
    print('Insufficient marks')






card_inserted = True
pin = 1234
balance = 8000
withdraw = 3000
if card_inserted:
    if pin == 1234:
        pin_verified = True
        if withdraw<=balance:
            print('Transaction  Successfull')
        else:
            print('Balance in insufficient')
    else:
        print('wrong pin entered')
else:
    print('Please insert the card')






registered = True
doctor_available = True
fees_paid = False
if registered:
    if doctor_available:
        if fees_paid:
            print('Appointment cleared')
        else:
            print('Pay Consultation Fees')
    else:
        print("Doctor not available")
else:
    print('Register first')







ticket = True
passport = True
security_check = True
if ticket:
    if passport:
        if security_check:
            print("Board Flight")
        else:
            print("Complete Security Check")
    else:
        print("Passport Missing")
else:
    print("Ticket Not Found")






degree = True
experience = 4
interview_score = 88
if degree:
    if experience >= 2:
        if interview_score >= 80:
            print("Selected")
        else:
            print("Interview Not Cleared")
    else:
        print("Experience Required")
else:
    print("Degree Required")







repository_exists = True
is_collaborator = True
branch_protected = False
if repository_exists:
    if is_collaborator:
        if not branch_protected:
            print("Push Successful")
        else:
            print("Cannot Push to Protected Branch")
    else:
        print("Access Denied")
else:
    print("Repository Not Found")










repository_exists = True
is_collaborator = True
branch_protected = False
if repository_exists:
    if is_collaborator:
        if not branch_protected:
            print("Push Successful")
        else:
            print("Cannot Push to Protected Branch")
    else:
        print("Access Denied")
else:
    print("Repository Not Found")









gst_verified = True
bank_verified = True
products_uploaded = True
if gst_verified:
    if bank_verified:
        if products_uploaded:
            print("Seller Account Activated")
        else:
            print("Upload Products")
    else:
        print("Verify Bank Account")
else:
    print("Verify GST Details")








dataset_loaded = True
data_cleaned = True
gpu_available = True
if dataset_loaded:
    if data_cleaned:
        if gpu_available:
            print("Start Model Training")
        else:
            print("Training on CPU")
    else:
        print("Clean Dataset First")
else:
    print("Load Dataset")






    