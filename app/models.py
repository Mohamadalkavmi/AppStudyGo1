 
 
from django.db import models
from django.contrib.auth.models   import User
from django.urls import reverse

#https://www.aspsnippets.com/Articles/Dynamically-add-and-remove-TextBoxes-using-JavaScript.aspx

# Create your models here.


class StudentStatus(models.Model):
    name = models.CharField(max_length=25 ,verbose_name= "Student Status"  ,  default="stage1" ,   unique= True) 
    statusDescription = models.CharField(max_length=25 ,verbose_name= "Status Description"   ,   unique= True) 

    def __str__(self):
        return format(self.name)+' , ' + format(self.statusDescription)
      
class StudentNationality(models.Model): 
    nationality = models.CharField(max_length=25 ,verbose_name= "Nationality"  ,    unique= True) 

    def __str__(self):
        return format(self.nationality)

class StudentResidence(models.Model):
    residence = models.CharField(max_length=25 ,verbose_name= "Residence"  ,    unique= True) 

    def __str__(self):
        return format(self.residence)

class UserType(models.Model):
    userType = models.CharField(max_length=25 ,verbose_name= "user Type"  ,    unique= True) 

    def __str__(self):
        return format(self.userType)


class StudentGender(models.Model):
    gender = models.CharField(max_length=15 ,verbose_name= "Student Gender"  ,  default="Male" ,   unique= True) 

    def __str__(self):
        return format(self.gender)

class StatusType(models.Model):
    name = models.CharField(max_length=60 , default="Missed document" ,  unique= True) 
    studentStatus =models.ForeignKey(StudentStatus,on_delete = models.CASCADE , verbose_name= "Student status"  ,default=1 )

    def __str__(self):
        return format(self.name)


class EmployeeInfo(models.Model):
    userid = models.ForeignKey(User, on_delete =models.CASCADE ,verbose_name ='User name'   ,default=1 ) 

    def __str__(self):
        return format(self.userid)

class ViewInfo(models.Model):
    userid = models.ForeignKey(User, on_delete =models.CASCADE ,verbose_name ='User name'   ,default=1 ) 

    def __str__(self):
        return format(self.userid)

class ManagerInfo(models.Model):
    userid = models.ForeignKey(User, on_delete =models.CASCADE ,verbose_name ='User name'   ,default=1 ) 

    def __str__(self):
        return format(self.userid)
      

class OfficeInfo(models.Model):
    userid = models.ForeignKey(User, on_delete =models.CASCADE ,verbose_name ='User name' ,default=1  ) 
    employeeInfoid = models.ForeignKey(EmployeeInfo, on_delete =models.CASCADE ,verbose_name ='Employee name', default=1  ) 

    def __str__(self):
        return format(self.userid )

class AllUserInfo(models.Model):
    userid = models.ForeignKey(User, on_delete =models.CASCADE ,verbose_name ='User name' ,default=1  )     
    phone =models.CharField(max_length=15 , default="0090")
    residence =models.ForeignKey(StudentResidence, on_delete =models.CASCADE ,verbose_name ='residence' ,default=1  ) #models.CharField(max_length=50 , default="Turkey")
    address =models.CharField(max_length=250 , default="Istanbul")    

    def __str__(self):
        return format(self.userid )

class UniversityDegree(models.Model):
    degree = models.CharField(max_length=40 , default = 'Bachelor' , verbose_name="Degree" ,null = False, unique= True)

    def __str__(self):
      return format(self.degree)

class DegreePaper(models.Model):
    degree =   models.ForeignKey(UniversityDegree, on_delete =models.CASCADE, verbose_name ='University Degree' ,default=1)
    paperName = models.CharField(max_length=40 , default = 'Passport' , verbose_name="Paper Name" )

    def __str__(self):
      return format(self.degree)  + ' ,' + format(self.paperName)  

 
class StudentInfo(models.Model):   
    referenceNo = models.CharField(max_length=25 , default="009988") # must be year and other info id for example
    officeInfoid = models.ForeignKey(OfficeInfo, on_delete =models.CASCADE ,verbose_name ='Office name' ,default=1  )     
    name  =models.CharField(max_length=20 , default="name" )   
    surname =models.CharField(max_length=20 , default="surname" )   
    gender = models.ForeignKey(StudentGender, on_delete =models.CASCADE ,verbose_name ='Student Gender' ,default=1  )     
    nationality = models.ForeignKey(StudentNationality, on_delete =models.CASCADE ,verbose_name ='Nationality' ,default=1  )     
    residence = models.ForeignKey(StudentResidence, on_delete =models.CASCADE ,verbose_name ='Residence' ,default=1)
    phone =models.CharField(max_length=25 , default="009988",null=True  )  #null accept
    email = models.EmailField(max_length=100,verbose_name =('email'),default = 'Info@studygo.com')
    passportNo =models.CharField(max_length=25 , default="009988"   )  #null accept
    documents =models.CharField(max_length=15 , default="No" ,null=True )    
    statusType =   models.ForeignKey(StatusType, on_delete =models.CASCADE,null=True  ,verbose_name ='Status Type' ,default=1)
    degree =   models.ForeignKey(UniversityDegree, on_delete =models.CASCADE,null=True  ,verbose_name ='University Degree' ,default=1)
    reject  =models.CharField(max_length=50 , default="" ,null=True )   

    def __str__(self):
        return format(self.name) + ' ' + format(self.surname)
 

class StudentPaper(models.Model):
    #file = models.FileField(upload_to='uploads/%Y/%m/%d/',widget=forms.FileInput(attrs={'accept':'txt/*,docx/*'},max_upload_size=242880,blank=True, null=True))
    picture = models.FileField(upload_to='uploads/%Y/%m/%d/', null = True)   
    studentid = models.ForeignKey(StudentInfo, on_delete =models.CASCADE,verbose_name ='Student name',default=1 )  
    degreePaper =models.CharField(max_length=40 ,verbose_name ='Degree Paper',default="degree Paper" , null=True ) 
      
    def __str__(self):
        return format(self.studentid.name)  + ' ,' + format(self.degreePaper)


class DocumentPaper(models.Model):
    #file = models.FileField(upload_to='uploads/%Y/%m/%d/',widget=forms.FileInput(attrs={'accept':'txt/*,docx/*'},max_upload_size=242880,blank=True, null=True))
    documentFile = models.FileField(upload_to='uploads/%Y/%m/%d/', null = True)   
    studentid = models.ForeignKey(StudentInfo, on_delete =models.CASCADE,verbose_name ='Student name',default=1 )  
    documentName =models.CharField(max_length=40 ,verbose_name ='Degree Paper',default="document Name" , null=True ) 
      
    def __str__(self):
        return format(self.studentid.name)  + ' ,' + format(self.documentName)


class UniversityLanguage(models.Model):
    language = models.CharField(max_length=50 ,  default = 'Turkish' , verbose_name="language" ,null = False,  unique= True)  

    def __str__(self):
      return format(self.language)

class UniversityName(models.Model):
    universityName = models.CharField(max_length=50 , default = 'Istanbul' , verbose_name="University Name" ,null = False, unique= True)  

    def __str__(self):
      return format(self.universityName)

 

class UniversityCity(models.Model):
    universityCity = models.CharField(max_length=40 , verbose_name="University City" , default = 'Istanbul',null = False , unique= True)  

    def __str__(self):
      return format(self.universityCity)

 
class UniversityProgram(models.Model):
    universityDegree = models.ForeignKey(UniversityDegree, on_delete =models.CASCADE ,verbose_name ='University Degree' ,default=1)     
    universityCity = models.ForeignKey(UniversityCity, on_delete =models.CASCADE ,verbose_name ='University city' ,default=1) 
    universityName = models.ForeignKey(UniversityName, on_delete =models.CASCADE ,verbose_name ='University name'   ,default=1)     
    department =  models.CharField(max_length=150, verbose_name="Department" , default = 'Law',null = False)           
    language = models.ForeignKey(UniversityLanguage, on_delete =models.CASCADE ,verbose_name ='Language' ,default=1 )     

    thesis = models.CharField(max_length=40 ,default="No" ,verbose_name="Thesis" , null =True)         
    numberOfYears = models.CharField(max_length=40 ,default="2" ,verbose_name="Number of Years",null =True )             
    notes = models.CharField(max_length=40 ,default="No" ,verbose_name="Notes" ,null =True)         
    systemOfPayment = models.CharField(max_length=40 ,default="Per year",null =True,verbose_name="System of Payment" )             
    taksitFees= models.CharField(max_length=40 ,default=""   ,verbose_name="Taksit Fees", null =True)
    activeSeat= models.BooleanField( default=1,verbose_name="Active seat")         

    CashFees = models.CharField(max_length=40 ,default="",null = True ,verbose_name="Cash Fees" )         

    def __str__(self):
        return   format(self.universityDegree.degree)+','+format(self.universityName.universityName)+',' + format(self.department) + ' ,' + format(self.language.language)    
 
class SeatsRegistration(models.Model):
    studentInfo = models.ForeignKey(StudentInfo, on_delete =models.CASCADE ,verbose_name ='Student Info' ,default=1  )   
    universityProgram =models.ForeignKey(UniversityProgram, on_delete =models.CASCADE ,verbose_name ='university Program' ,default=1  )   

   
    def __str__(self):
        return format(self.studentInfo.name)+' '+format(self.studentInfo.surname)+' ,'+format(self.universityProgram.universityName) 

 