print('WELCOME TO THE HOTEL')        
print('Please enter your details:')

class Guest():
    '''
    This class create a set of attributes and
    methods for guest.
    '''
    def __init__(self):
        self.name=''
        self.id=''
        self.members=0
        self.duration=0
        
    def EnterYourName(self):
        self.name=input('Your Name:')
        
    def EnterIdProof(self):
        i=input('Enter your Aadhaar no. :')
        self.id=i
        
    def EnterNoOfMembers(self):
        n=int(input('Enter no. of members:'))
        self.members=n

        
    def Duration(self):
        d=int(input('Enter the duration of your stay in Days'))
        self.duration=d
        
        
class AddOns():
    '''
    This class creates certain extra features
    you can enjoy living in a hotel.
    '''
    def __init__(self):
        self.charge=0
        
    def Food(self):
        z=int(input('Please Select Your Choice:\n1.Just Breakfast \n2.All meals Included'))
        if(z==1):
            self.charge=self.charge+20
        else:
            self.charge=self.charge+50
            
    def Pool(self):
        self.charge=self.charge+10
        
    def CarRental(self):
        dis=int(input('Enter the distance to be covered by the car in Kms:'))
        self.charge=self.charge+(dis*5)



class HotelReservation(AddOns):
    '''
    This class deals with different types of 
    rooms available and their respective prices.
    '''
    def __init__(self):
        AddOns.__init__(self)
        self.choice=''
        self.cost=''
    
    def singleRoom(self):
            self.choice='Single Room'
            self.cost=1200
            
    def DoubleRoom(self):
        
            self.choice='Double Room'
            self.cost=2000
            
    def TripleRoom(self):
        
            self.choice='Triple Room'
            self.cost=3000
            
    def KingRoom(self):
        self.choice='King Sized Room'
        self.cost=5000
    def MasterSuite(self):
        self.choice='Master Suit'
        self.cost=6000
        
        

        
#while True:

G=Guest()
G.EnterYourName()
G.EnterIdProof()
G.EnterNoOfMembers()
G.Duration()
y=G.members
g=G.duration
while True:
    x=int(input('Please Select Your Type of Room:\n1.Single Room\n2.Double Room\n3.Triple Room\n4.King Room\n5.Master Suite'))
    Reserve=HotelReservation()
    if(x==1):
        if(y!=1):
            print("Insufficient Space for more than 1 person")
            continue
        else:
            Reserve.singleRoom()
            break
    elif(x==2):
        if(y>2):
            print("Insufficient Space for more than 2 person")
            continue
        else:
            Reserve.DoubleRoom()
            break
    
    elif(x==3):
        if(y>3):
            print("Insufficient Space for more than 3 person")
            
        else:
            Reserve.TripleRoom()
            break
    
    elif(x==4):
        Reserve.KingRoom()
        break
    
    elif(x==5):
        Reserve.MasterSuite()
        break
    
    else:
        print('Wrong Choice')
        continue
    
z=input('Do you Want any Add Ons For Your Room?-Y or N:')
if(z=='Y'):
    sel=int(input('PLease Select Your Choice:\n1.Food\n2.Pool\n3.Car Rental'))
    if(sel==1):
        Reserve.Food()
    elif(sel==2):
        Reserve.Pool()
    elif(sel==3):
        Reserve.CarRental()
    elif(sel==12):
        Reserve.Food()
        Reserve.Pool()
    elif(sel==13):
        Reserve.Food()
        Reserve.CarRental()
    elif(sel==23):
        Reserve.Pool()
        Reserve.CarRental()
        
    else:
        Reserve.Food()
        Reserve.Pool()
        Reserve.CarRental()
        

total=(Reserve.charge+Reserve.cost)*g     #Here we have multiplied the total cost of living for one day in the hotel with the stay duration.  
print('The Total Bill Amount is:{}'.format(total))
        
    



    