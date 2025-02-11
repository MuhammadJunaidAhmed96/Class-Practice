print("Signup")

Empname= input("Enter Your Name \n")
empemail= input("Enter Your Email \n")
emppass= input("Enter Your Password \n")
Empcontact= input("Enter Your Contact \n")
EmpAdress= input("Enter Your Address \n")
EmpProvince= input("Enter Your Province \n")
EmpCity= input("Enter Your City \n")
EmpCity= input("Enter Your District \n")

print("Account successfully Created")


empEmailLogin= input("Enter Your Login Email\n")
empPassLogin= input("Enter Your Login Password\n")

if((empEmailLogin==empemail) and (empPassLogin==emppass)):
    print("Account Succesfully Login")

    eng= float(input("Enter your english marks"))
    math= float(input("Enter your Math marks"))
    Urdu= float(input("Enter your Urdu marks"))
    Physics= float(input("Enter your Physics marks"))
    Chemistry= float(input("Enter your Chemistry marks"))
    Islamiat= float(input("Enter your Islamiat marks"))
    PakistanStudies= float(input("Enter your Pakistan Studies marks"))

    obtainedMarks = eng+math+Urdu+Physics+Chemistry+Islamiat+PakistanStudies

    percentage= (obtainedMarks/700)*100

    if percentage<=100 and percentage>=80:
        print("Grade A1")
    elif percentage<=79 and percentage>=70:
        print("Grade A")
    elif percentage<=69 and percentage>=60:
        print("Grade B")
    elif percentage<=59 and percentage>=50:
        print("Grade C")
    else:
        print(fail)



