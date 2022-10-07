#BMI Calculator using python
print('hey!welcome to Bmicalculator')

def bmicount(height,weight):
    return round((weight/height**2),2)



while True:
    option=['meter','feet']
    person=None
    while person not in option:
        person=input('choose your height input format! A) meter or B) feet')
        if person=='meter':
            h=input('enter your height in meter:')
        elif person=='feet':
            h1=float(input('enter your height in feet:'))
            h=h1/3.3
        w = float(input('enter your weight in kg'))
        bmi = bmicount(h, w)
        print('your BMI is: ', bmi)
        if bmi<=18.5:
            print('you are under wight.')
        elif 18.5<bmi<=24.9:
            print('you are just perfect the way you are.')
        elif 24.9<=bmi<=29.29:
            print('you are bit overweight.')
        else:
            print('you are obese.')
        calculate_again=input('wanna calculate another bmi? press (y/n)')

        if calculate_again=='y':
            continue
        else:
            print('bye!stay healthy')




