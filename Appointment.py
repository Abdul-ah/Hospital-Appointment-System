import random
def returnshift(num):
    numb={
        1:'Morning',
        2:'Afternoon',
        3:'Evening',
        4:'Night'
        }
    return numb.get(num, 'Unspecific')

def returnspecial(num):
    numb={
        1:'General Physician',
        2:'ENT',
        3:'Cardiologist',
        4:'Dentish',
        5:'Dermatologist',
        6:'Neonatologist',
        7:'Allergy Specialization'
        }
    return numb.get(num, 'Unspecific')

class Doctors:
    def avail1(self,num):
        numb={
            1:'Dr.Madhavan...MBBS',
            2:'Dr.Sarala...MBBS',
            3:'Dr.Anup...MBBS',
            4:'Dr.Varshini...MBBS'
            }
        return numb.get(num, 'Invalid Entry')
    def avail2(self,num):
        numb={
            1:'Dr.Shahina...MBBS',
            2:'Dr.John...MBBS',
            3:'Dr.Abdul Rahim...MBBS',
            4:'Dr.Imran.MBBS'
            }
        return numb.get(num, 'Invalid Entry')
    def avail3(self,num):
        numb={
            1:'Dr.Jessy...MBBS',
            2:'Dr.Akash...MBBS',
            3:'Dr.Keerthi...MBBS',
            4:'Dr.Mukundaan...MBBS'
            }
        return numb.get(num, 'Invalid Entry')
    def avail4(self,num):
        numb={
            1:'Dr.Ramakrishna...MBBS',
            2:'Dr.Joseph...MBBS',
            3:'Dr.Peter...MBBS',
            4:'Dr.Suresh...MBBS'
            }
        return numb.get(num, 'Invalid Entry')
    def avail5(self,num):
        numb={
            1:'Dr.Mariyam Begam...MBBS',
            2:'Dr.Lilly...MBBS',
            3:'Dr.Abdullah...MBBS',
            4:'Dr.Sanjay...MBBS'
            }
        return numb.get(num, 'Invalid Entry')
    def avail6(self,num):
        numb={
            1:'Dr.Sulthan Kani...MBBS',
            2:'Dr.Irfan...MBBS',
            3:'Dr.Sabina...MBBS',
            4:'Dr.Rasheed...MBBS'
            }
        return numb.get(num, 'Invalid Entry')
    def avail7(self,num):
        numb={
            1:'Dr.Arjun...MBBS',
            2:'Dr.Regina...MBBS',
            3:'Dr.Siva Prasath...MBBS',
            4:'Dr.Mohamed Ilyas...MBBS'
            }
        return numb.get(num, 'Invalid Entry')
class registration:
    def __init__(self):
        self.__name=str(input('Enter your name: '))
        self.__userid=str(input('Create your own user id: '))
        self.__pass=str(input('Create your password: '))
        self.__email=str(input('Enter your Email id: '))
        self.__phone=int(input('Enter Phone Number: '))
        print('Account created successfully :)',end='\n\n')
    def login(self):
        print('Enter login details')
        user=str(input('Enter User id: '))
        password=str(input('Enter password: '))
        if user==self.__userid and password==self.__pass:
            print('Login success',end='\n\n')
            return 1
        else:
            print('Login failed!',end='\n\n')
            return 0
class appointment(Doctors):
    def __init__(self):
        self.__name=str(input('Patient Name: '))
        self.__sex=str(input('Enter M for Male, F for Female: '))
        if self.__sex=='F' or self.__sex=='f':
            self.__sex='Female'
        elif self.__sex=='M' or self.__sex=='m':
            self.__sex='Male'
        print('Enter the Date, Month and Year of appointment: ')
        self.__date=int(input())
        self.__month=int(input())
        self.__year=int(input())
        print('Enter','  1 for Morning shift','  2 for Afternoon shift','  3 for Evening shift','  4 for Night shift',sep='\n')
        entry1=int(input())
        self.__shift=str(returnshift(entry1))
        print('Choose your Specialization','Enter','  1 for General physician','  2 for ENT','  3 for Cardiologist','  4 for Dentist','  5 for Dermatologist','  6 for Neonatologist(Childern Specialization)','  7 for Allergy specialist',sep='\n')
        entry2=int(input())
        if entry2 >= 1 and entry2 <=7:
            self.__special=str(returnspecial(entry2))
            doc=str(input('Can we provide any specific doctor for consultation: '))
            if doc=='yes' or doc=='Yes' or doc=='YES':
                print('We found 4 Doctors for you, here is one')
                seq=[1,2,3,4]
                doctor=random.choice(seq)
                if entry2==1:
                    self.__Doctor=str(Doctors.avail1(self,doctor))
                    print(self.__Doctor)
                elif entry2==2:
                    self.__Doctor=str(Doctors.avail2(self,doctor))
                    print(self.__Doctor)
                elif entry2==3:
                    self.__Doctor=str(Doctors.avail3(self,doctor))
                    print(self.__Doctor)
                elif entry2==4:
                    self.__Doctor=str(Doctors.avail4(self,doctor))
                    print(self.__Doctor)
                elif entry2==5:
                    self.__Doctor=str(Doctors.avail5(self,doctor))
                    print(self.__Doctor)
                elif entry2==6:
                    self.__Doctor=str(Doctors.avail6(self,doctor))
                    print(self.__Doctor)
                elif entry2==7:
                    self.__Doctor=str(Doctors.avail7(self,doctor))
                    print(self.__Doctor)
                entry3=str(input('Hope you are Comfort with our suggession: '))
                if entry3=='yes' or entry3=='Yes' or entry3=='YES':
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                else:
                    while entry3=='No' or entry3=='NO' or entry3=='no':
                        doctor=random.choice(seq)
                        if entry2==1:
                            self.__Doctor=str(Doctors.avail1(self,doctor))
                            print(self.__Doctor)
                        elif entry2==2:
                            self.__Doctor=str(Doctors.avail2(self,doctor))
                            print(self.__Doctor)
                        elif entry2==3:
                            self.__Doctor=str(Doctors.avail3(self,doctor))
                            print(self.__Doctor)
                        elif entry2==4:
                            self.__Doctor=str(Doctors.avail4(self,doctor))
                            print(self.__Doctor)
                        elif entry2==5:
                            self.__Doctor=str(Doctors.avail5(self,doctor))
                            print(self.__Doctor)
                        elif entry2==6:
                            self.__Doctor=str(Doctors.avail6(self,doctor))
                            print(self.__Doctor)
                        elif entry2==7:
                            self.__Doctor=str(Doctors.avail7(self,doctor))
                            print(self.__Doctor)
                        entry3=str(input('Hope you are Comfort with our new suggession: '))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
            else:
                print('Here we found 4 doctors,time to choose one','Enter',sep='\n')
                if entry2==1:
                    print('  1 for Dr.Madhavan...MBBS','  2 for Dr.Sarala...MBBS','  3 for Dr.Anup...MBBS','  4 for Dr.Varshini...MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail1(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                elif entry2==2:
                    print('  1 for Dr.Shahina...MBBS','  2 for Dr.John...MBBS','  3 for Dr.Abdul Rahim...MBBS','  4 for Dr.Imran.MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail2(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                elif entry2==3:
                    print('  1 for Dr.Jessy...MBBS','  2 for Dr.Akash...MBBS','  3 for Dr.Keerthi...MBBS','  4 for Dr.Mukundaan...MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail3(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                elif entry2==4:
                    print('  1 for Dr.Ramakrishna...MBBS','  2 for Dr.Joseph...MBBS','  3 for Dr.Peter...MBBS','  4 for Dr.Suresh...MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail4(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                elif entry2==5:
                    print('  1 for Dr.Mariyam Begam...MBBS','  2 for Dr.Lilly...MBBS','  3 for Dr.Abdullah...MBBS','  4 for Dr.Sanjay...MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail5(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                elif entry2==6:
                    print('  1 for Dr.Sulthan Kani...MBBS','  2 for Dr.Irfan...MBBS','  3 for Dr.Sabina...MBBS','  4 for Dr.Rasheed...MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail6(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                elif entry2==7:
                    print('  1 for Dr.Arjun...MBBS','  2 for Dr.Regina...MBBS','  3 for Dr.Siva Prasath...MBBS','  4 for Dr.Mohamed Ilyas...MBBS',sep='\n')
                    doctor=int(input())
                    self.__Doctor=str(Doctors.avail7(self,doctor))
                    self.__problem=str(input('Mention your Problem or Reason: '))
                    print('\n')
                print('Thanks for your patiency.',end='\n\n')
        else:
            print('Wrong Entry')
            self.__special=' -'
            self.__Doctor=' - '
            self.__problem=' - '
                
    def display(self):
        print('Here is your Appointment Details')
        print('Name:',self.__name,sep=' ')
        print('Sex:',self.__sex,sep=' ')
        print('Date:',end=' ')
        print(self.__date,self.__month,self.__year,sep='/')
        print('Shift:',self.__shift,sep=' ')
        print('Specialization:',self.__special,sep=' ')
        print('Doctor:',self.__Doctor,sep=' ')
        print('Problem or Reason:',self.__problem,sep=' ')
        if self.__shift!='Unspecific' and self.__special!='Unspecific' or self.__sex =='Female' or self.__sex =='Male':
            print('Status:','Confirmed :)',sep=' ')
            print('Meet you soon...')
        else:
            print('Status:','Denied :(')
            print ('Look above details and re-appoint')
            
        
print('                               Family Hospitals welcomes You!!!',end='\n\n')
print('                                    A Family like Feeling',end='\n\n')
print('Register Now to get all our Best Facilities',end='\n\n')
regi=registration()
doctor=Doctors()
if(regi.login()):
    appoint=str(input('Looking for an Appointment: '))
    if (appoint=='yes' or appoint=='Yes' or appoint=='YES'):
        print('\n','Under Process...',sep='',end='\n\n')
        app=appointment()
        app.display()
    else:
        print('Thank You,Visit Again!!!')
        
