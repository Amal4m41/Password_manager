#Master-password : 'unlock'
import getpass,random as r,hashlib as h
d={}

ch=p=''
def get_password():
  global p,ch  
  ch=p=''
  while(len(p)!=16):
    p+=chr(r.choice([r.randrange(47,127),r.choice([33,35,36,37,38,40,41,42,47])]))
    if(len(p)==16 and (p in d1.values())):
      p=''
  print("Password generated : ",p)
  ch=input("Continue with the password (Press 'Y')/Change (Press any other key) : ").lower()
  while(ch!='y'):
    get_password()

  return(p)

d1={}
def storage():                                 #generates a dictionary(d1) after reading the text file
  global d1
  d1={};l=1
  with open('password.txt','r') as f:
    while(l):
      l=f.readline()
      if(':' in l):
        c=l.replace('\n','').split(':')
        d1.update({c[0]:c[1]})
    #print(d1)
  

def update_storage():                          #rewrites the text file with the latest changes in dict(d) 
  #print(d)
  with open('password.txt','w') as f1:
    for i in d:
      f1.write(i+':'+d[i]+'\n')

  print('                                                 Updated')
        


def main():
  global d
  print("                                          Welcome to Password Manager")
  with open('master_pass.txt','r') as f1:
    mp=f1.read().replace('\n','').strip()
  for i in range(3):
    ch=getpass.getpass("Enter the masterpassword : ")
    if(((h.sha512(ch.encode())).hexdigest())==mp):
      while(1):
        storage()
        
        d.update(d1)
        ch=input('''
(A)dd new password/service, (G)et password or (C)hange password? (L)ist all Services ,(D)elete from list,(Q)uit                  
(M)aster password change
Enter option :''').lower()
        if(ch=='a'):
          while(1):
            s=input("Service name : ")          
            if(s not in d):
              p=get_password()
              d[s]=p
              print('Added successfully')
            else:
              print('Service already exist!')
            ch1=input("Add more[Y/N] ?").lower()
            if(ch1=='n'):
              break
            
        elif(ch=='g' or ch=='c'):
          s=input("Service name : ")
          while(s not in d):
            print("Service doesn't exist!")
            c=input("Do you want to try again[Y/N] ?")
            if(c.lower()=='n'):
              break
            s=input("Service name : ")
          else:
            print("Current Password : ",d[s])
            c1=input("Change password[Y/N] ?").lower()
            if(c1=='y'):
              p=get_password()
              d[s]=p

        elif(ch=='l'):
          if(d=={}):
            print("No Services:")
          else:
            print("Services:")
            for i in d:
              print(i)

        elif(ch=='d'):
          c3=input('Press (A) to delete ALL (else press any key) : ').lower()
          if(c3=='a'):
            d={}
            print("Done")
          else:
            while(1):
              s=input('Enter the service name to delete : ').lower()
              if(s in d):
                d.pop(s)
                print(s,"deleted")  	

              else:
                print("Service doesn't exist!")

              c2=input('Delete more service(s)[Y/N] ?').lower()
              if(c2=='n'):
                break

        elif(ch=='m'):
          c5=input("Change Master-password[Y/N] ?").lower()
          if(c5=='y'):
            z='n'
            while(z!='y'):
              new_pass=input('Enter the new Master-password : ')
              z=input('Continue with the new Master-password[Y/N] ? ').lower()
            
            with open('master_pass.txt','w') as fm:
              fm.write((h.sha512(new_pass.encode())).hexdigest())
              print("Master-password Updated")
          else:
            print("Master-password unchanged")

        elif(ch=='q'):
          print("Thank you")
          break
      
        else:
          print("Invalid option!")	
      
        
        update_storage()  

      break    	           
  else:
    print("Access denied!")

main()
