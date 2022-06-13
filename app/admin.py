from django.contrib import admin
from .models import  UserType ,OfficeInfo ,EmployeeInfo ,StatusType, StudentStatus ,StudentInfo ,StudentGender  , StudentNationality ,StudentResidence
from .models import  UniversityCity,UniversityLanguage,  UniversityProgram,UniversityName,UniversityDegree
from .models import SeatsRegistration ,AllUserInfo   ,DegreePaper ,StudentPaper ,ViewInfo ,ManagerInfo ,DocumentPaper

# Register your models here.
admin.site.register(UserType)
admin.site.register(AllUserInfo) 
admin.site.register(OfficeInfo)
admin.site.register(EmployeeInfo)
admin.site.register(ViewInfo )  
admin.site.register(ManagerInfo )  
admin.site.register(StatusType)
admin.site.register(StudentStatus)
admin.site.register(StudentInfo) 
admin.site.register(StudentGender)   
admin.site.register(StudentResidence) 
admin.site.register(StudentNationality) 
admin.site.register(SeatsRegistration) 
admin.site.register(DocumentPaper) 


admin.site.register(UniversityLanguage)  
  
admin.site.register(UniversityCity)   
admin.site.register(UniversityProgram)  
admin.site.register(UniversityName)  
admin.site.register(UniversityDegree)  
admin.site.register(DegreePaper )  
admin.site.register(StudentPaper )  
 
   
 