"""
Definition of views.
"""
from asyncio.windows_events import NULL
from pickle import NONE
from tarfile import NUL
from django.shortcuts import render,redirect  
from datetime import datetime
 
from django.contrib.auth.models import User,Group
from django.contrib import messages
#from .admin import admin

import os
from django.conf import settings
from django.contrib.auth.hashers import  make_password, check_password  

from .forms import  UserCreationForm1 ,  UniversityRegisterForm , StudentRegisterForm ,LoginForm , AllUserInfoForm ,OfficeInfoForm ,UniversityProgramForm    ,UniversityDegreeForm ,StudentPaperForm  

from  .models import  UserType ,OfficeInfo  , StudentInfo ,EmployeeInfo,AllUserInfo ,UniversityCity,UniversityLanguage,   UniversityProgram,UniversityName ,ViewInfo
from  .models import  StudentGender ,StudentResidence,UniversityDegree , StudentNationality ,StudentStatus ,SeatsRegistration ,StudentInfo ,DegreePaper ,StudentPaper ,StatusType,UniversityProgram ,ManagerInfo,DocumentPaper
from django.contrib.auth  import authenticate , login ,logout 
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpRequest
 
import openpyxl
#import csv
from pathlib import Path
from django.shortcuts import get_object_or_404


Payment_Receipt_Uploaded='Payment Receipt Uploaded'
University_Enrollment_Completed='University Enrollment Completed'
Acceptance_Letter_Sent ='Acceptance Letter Sent'

def import_csv(request):
    try:
      if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']
          
            myfileName =Path(myfile.name).stem #Path('/root/file.ext').stem
            
            excel = openpyxl.load_workbook(myfile)
            sheet = excel.active      
            sheet.delete_rows(1) # remove header 

            if myfileName == 'UniversityCity':
              sqlinfo = "SELECT  * FROM app_universitycity" 
              Seatstemps =UniversityCity.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id +=1
               obj = UniversityCity.objects.create(id=id,universityCity=r[0].value) 
               obj.save()

            if myfileName == 'UniversityName':
              sqlinfo = "SELECT  * FROM app_universityname" 
              Seatstemps =UniversityName.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id +=1
               obj = UniversityName.objects.create(id=id,universityName=r[0].value) 
               obj.save()

            if myfileName == 'UniversityLanguage':
              sqlinfo = "SELECT  * FROM app_universitylanguage" 
              Seatstemps =UniversityLanguage.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id +=1
               obj = UniversityLanguage.objects.create(id=id,language=r[0].value) 
               obj.save()

            if myfileName == 'UniversityDegree':
              sqlinfo = "SELECT  * FROM app_universitydegree" 
              Seatstemps =UniversityDegree.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id+=1
               obj = UniversityDegree.objects.create(id=id,degree=r[0].value) 
               obj.save()

            if myfileName == 'DegreePaper':
              sqlinfo = "SELECT  * FROM app_degreepaper" 
              Seatstemps =DegreePaper.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id +=1 
               obj = DegreePaper.objects.create(id=id,degree_id=format(r[0].value),paperName=r[1].value) 
               obj.save()
               
            #if myfileName == 'UniversityDepartment':
            #  UniversityDepartment.objects.all().delete()
            #  for r  in   sheet.rows: #sheet.rows:
            #   obj = UniversityDepartment.objects.create(department=r[0].value) 
            #   obj.save()

            if myfileName == 'StudentGender':
              for r  in   sheet.rows: #sheet.rows:
               obj = StudentGender.objects.create(gender=r[0].value) 
               obj.save()                              

            if myfileName == 'StudentResidence':
              sqlinfo = "SELECT  * FROM app_studentresidence" 
              Seatstemps =StudentResidence.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id +=1
               obj = StudentResidence.objects.create(id=id,residence=r[0].value) 
               obj.save()                              

            if myfileName == 'StudentNationality':
              sqlinfo = "SELECT  * FROM app_studentnationality" 
              Seatstemps =StudentNationality.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:
               id +=1
               obj = StudentNationality.objects.create(id=id,nationality=r[0].value) 
               obj.save()    
               
            if myfileName == 'StudentStatus': 
              for r  in   sheet.rows: #sheet.rows:
               obj = StudentStatus.objects.create(name=r[0].value , statusDescription = r[1].value) 
               obj.save()  


            if myfileName == 'StatusType': 
              for r  in   sheet.rows: #sheet.rows:
               studentStatus =get_object_or_404(StudentStatus,name=r[0].value.lstrip()  )
               obj = StatusType.objects.create( name = r[1].value , studentStatus_id=studentStatus.id) 
               obj.save()  


            if myfileName == 'UniversityProgram':
              sqlinfo = "SELECT  * FROM app_universityprogram" 
              Seatstemps =UniversityProgram.objects.raw(sqlinfo )
              for Seatstemp in Seatstemps:      
                Seatstemp.delete() 
                 
              id = 0
              for r  in   sheet.rows: #sheet.rows:  
               id +=1
               universityDegree =get_object_or_404(UniversityDegree,degree=r[0].value.lstrip()  )         
               universityCity =get_object_or_404(UniversityCity,universityCity=r[1].value.lstrip()  )               
               universityName =get_object_or_404(UniversityName,universityName=r[2].value.lstrip() )
               language =get_object_or_404(UniversityLanguage,language=r[4].value.lstrip() )               
               try:
                  thesis =r[5].value 
               except:
                  thesis=""

               try:
                  numberOfYears =r[6].value 
               except:
                  numberOfYears=""
               try:
                  notes =r[7].value 
               except:
                  notes=""

               try:
                  systemOfPayment =r[8].value 
               except:
                  systemOfPayment=""

               try:
                  taksitFees =r[9].value 
               except:
                  taksitFees=""
               #obj = UniversityProgram.objects.create(universityName_id=universityName.id ,language_id = language.id  ,universityDegree_id =universityDegree.id 
               obj = UniversityProgram.objects.create(id = id ,universityDegree_id =universityDegree.id ,universityCity_id =universityCity.id ,  universityName_id=universityName.id        ,department =r[3].value   , language_id = language.id  , 
                                                      #thesis=r[5].value.lstrip() ,numberOfYears =skip_empty_rows(r[6].value).lstrip()  , notes =r[7].value.lstrip() ,systemOfPayment =r[8].value.lstrip() ,     taksitFees =r[9].value.lstrip()   ,activeSeat=1 )
                                                      thesis= thesis  ,numberOfYears = numberOfYears , notes =notes   ,systemOfPayment =systemOfPayment ,  taksitFees =taksitFees  ,activeSeat=1 )
                                                        
               obj.save()  


               
                
               
    except Exception as identifier:            
        print(identifier)
 
    return   redirect('officepageEmp',request.user.username)    


def adminpage(request):    
    return redirect('/admin/')

def logout_user(request):
    logout(request) 
    return render( 
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )   
   
  
def officepage(request,username):  
  try:
   userid =request.user.id   
   officeid = -1   
   adminids =OfficeInfo.objects.raw("SELECT id  FROM app_officeinfo WHERE userid_id ="+format(userid))                     
           
   for admid in adminids:
        officeid= admid.id
 
 
   if   (officeid !=-1):    
    officeInfoid =0
    studentInfo = StudentInfo()
    sqluser="SELECT  auth_user.id,auth_user.username,app_officeinfo.userid_id ,app_officeinfo.id AS offid  FROM auth_user,app_officeinfo WHERE  auth_user.id=app_officeinfo.userid_id AND auth_user.username='"+ username+"'"  
    officeinfoids= User.objects.raw(sqluser)

    for offid in officeinfoids:
       officeInfoid = offid.offid

    sqluser="SELECT  * FROM app_studentinfo WHERE OfficeInfoid_id="+ format(officeInfoid) + " ORDER BY id DESC   " 
    studentInfos= StudentInfo.objects.raw( sqluser )
    
     
   
    sqluser ="SELECT  app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_studentinfo,app_statustype  WHERE app_studentinfo.OfficeInfoid_id="+ format(officeInfoid) +" AND app_studentinfo.statustype_id =app_statustype.id   GROUP BY app_studentinfo.statustype_id "  

    statusTypesNum = StatusType.objects.raw(sqluser ) #statusType
    statusTypes = StatusType.objects.raw("SELECT  * FROM app_statustype " ) #statusType
    studentStatus = StudentStatus.objects.raw("SELECT  * FROM app_studentstatus " )
    tableTitle ='Students Table'

    statusTypesNumAll=0 
    for typesnums in statusTypesNum:
      statusTypesNumAll += typesnums.statustypeNum

    return render(
          request,
          'app/officepage.html',
          {
              'title':'OfficePage',
              'studentInfo':'studentInfo',
              'studentInfos' :studentInfos ,
              'username' :username, 
              'statusTypes':statusTypes,
              'statusTypesNumAll':statusTypesNumAll,
              'seatslist' :'seatslist',
              'officepage':'officepage',
              'statusTypesNum' :statusTypesNum,
              'studentStatus':studentStatus,
              'tableTitle':tableTitle,
              'uploadfile' :'uploadfile',
              'officepage' :'officepage', 
              'logout_user' :'logout_user',
              'studendata' :'studendata',
              'newApplication':'newApplication',
              'seatslist' :'seatslist',
              'year':datetime.now().year,
          }
              
           
         )  
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )

 
def officepageEmp(request,username):
  try:
   employeeId =-1
   userid =request.user.id   
   sqluser="SELECT  auth_user.id,auth_user.username,app_employeeinfo.userid_id ,app_employeeinfo.id AS offid  FROM auth_user,app_employeeinfo WHERE  auth_user.id=app_employeeinfo.userid_id AND auth_user.id="+format(request.user.id)
   empinfoids= User.objects.raw(sqluser)

   for offid in empinfoids:
    employeeId = offid.offid

   officename = "All"
   userid =request.user.id   
   if (employeeId !=-1):
    sqluser="SELECT  app_employeeinfo.id AS employeeId,auth_user.id,app_employeeinfo.userid_id FROM  auth_user ,app_employeeinfo WHERE auth_user.id =app_employeeinfo.userid_id   AND auth_user.id="+ format(userid)  
    employeeIds =  OfficeInfo.objects.raw(sqluser )
    for empId in employeeIds:
         employeeId = empId.employeeId 
    
    sqluser="SELECT   id   FROM  app_officeinfo WHERE   employeeInfoid_id="+ format(employeeId)  
    officelists =  OfficeInfo.objects.raw(sqluser )

    if request.method =='POST':
     try:
      officeid = request.POST['officelists']
     except:
      officeid ='All'
      
     if (officeid !='All'):
       officename ="All" 
       sqluser="SELECT  auth_user.id,auth_user.username AS username FROM  auth_user ,app_officeinfo WHERE auth_user.id =app_officeinfo.userid_id   AND app_officeinfo.id="+ format(officeid)  
       officeanems= StudentInfo.objects.raw( sqluser )

       for offname in officeanems:
         officename = offname.username 
       sqluser ="SELECT  app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_studentinfo,app_statustype  WHERE app_studentinfo.OfficeInfoid_id="+ format(officeid) +" AND app_studentinfo.statustype_id =app_statustype.id   GROUP BY app_studentinfo.statustype_id "       
       statusTypesNum = StatusType.objects.raw(sqluser ) #statusType
       sqluser="SELECT  * FROM app_studentinfo WHERE officeInfoid_id="+ format(officeid) + " ORDER BY id DESC   " 
       studentInfos= StudentInfo.objects.raw( sqluser )
     else:
       
       sqluser="SELECT  app_officeinfo.employeeInfoid_id, app_studentinfo.id ,app_studentinfo.referenceNo,app_studentinfo.officeInfoid_id ,app_studentinfo.name ,app_studentinfo.surname ,app_studentinfo.gender_id ,app_studentinfo.nationality_id  ,app_studentinfo.residence_id ,app_studentinfo.phone ,app_studentinfo.email ,app_studentinfo.passportNo, app_studentinfo.documents ,app_studentinfo.degree_id,app_studentinfo.statusType_id , app_studentinfo.reject FROM app_studentinfo , app_officeinfo  WHERE  app_studentinfo.officeInfoid_id = app_officeinfo.id  AND   app_officeinfo.employeeInfoid_id="+ format(employeeId) + " ORDER BY app_studentinfo.id  DESC     "        
       studentInfos= StudentInfo.objects.raw( sqluser )
      
       sqluser="SELECT  app_officeinfo.employeeInfoid_id ,app_studentinfo.officeinfoid_id , app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_officeinfo, app_studentinfo,app_statustype   WHERE app_studentinfo.statustype_id =app_statustype.id AND app_officeinfo.id =app_studentinfo.officeInfoid_id  AND app_officeinfo.employeeInfoid_id="+ format(employeeId) +"   GROUP BY app_studentinfo.statustype_id "
       statusTypesNum = StatusType.objects.raw(sqluser ) #statusType


    else:       
     sqluser="SELECT  app_officeinfo.employeeInfoid_id, app_studentinfo.id ,app_studentinfo.referenceNo,app_studentinfo.officeInfoid_id ,app_studentinfo.name ,app_studentinfo.surname ,app_studentinfo.gender_id ,app_studentinfo.nationality_id  ,app_studentinfo.residence_id ,app_studentinfo.phone ,app_studentinfo.email ,app_studentinfo.passportNo, app_studentinfo.documents ,app_studentinfo.degree_id,app_studentinfo.statusType_id , app_studentinfo.reject FROM app_studentinfo , app_officeinfo  WHERE  app_studentinfo.officeInfoid_id = app_officeinfo.id  AND   app_officeinfo.employeeInfoid_id="+ format(employeeId) + " ORDER BY app_studentinfo.id  DESC     " 
     studentInfos= StudentInfo.objects.raw( sqluser )

     sqluser="SELECT  app_officeinfo.employeeInfoid_id ,app_studentinfo.officeinfoid_id , app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_officeinfo, app_studentinfo,app_statustype   WHERE app_studentinfo.statustype_id =app_statustype.id AND app_officeinfo.id =app_studentinfo.officeInfoid_id  AND app_officeinfo.employeeInfoid_id="+ format(employeeId) +"   GROUP BY app_studentinfo.statustype_id "
     statusTypesNum = StatusType.objects.raw(sqluser ) #statusType

    statusTypesNumAll=0 
    for typesnums in statusTypesNum:
      statusTypesNumAll += typesnums.statustypeNum
    statusTypes = StatusType.objects.raw("SELECT  * FROM app_statustype " ) #statusType
    studentStatus = StudentStatus.objects.raw("SELECT  * FROM app_studentstatus " )
    tableTitle ='Students Table'

    return render(
          request,
          'app/officepageEmp.html',
          {
              'title':'EmployeePage',
              'studentInfo':'studentInfo',
              'studentInfos' :studentInfos ,
              'officename' :officename,
              'statusTypesNumAll' :statusTypesNumAll,
              'officelists' : officelists, 
              'officepageEmp' :'officepageEmp',
              'username' :username, 
              'statusTypes':statusTypes,
              'studendataEmp' :'studendataEmp',
              'seatslistEmp':'seatslistEmp',
              'statusTypesNum' :statusTypesNum,
              'studentStatus':studentStatus,
              'tableTitle':tableTitle,
              'uploadfile' :'uploadfile',           
              'logout_user' :'logout_user',               
              'year':datetime.now().year,
          }
              
           
         )   
   else:
        return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )
 

def officepageManager(request,username):  
  try:
   managerId =-1
   userid =request.user.id   
   sqluser="SELECT  auth_user.id,auth_user.username,app_managerinfo.userid_id ,app_managerinfo.id AS offid  FROM auth_user,app_managerinfo WHERE  auth_user.id=app_managerinfo.userid_id AND auth_user.id="+format(request.user.id)
   maninfoids= User.objects.raw(sqluser)

   for offid in maninfoids:
    managerId = offid.offid
   officename = "All"
   userid =request.user.id   
   if (managerId !=-1):
    officelists =  OfficeInfo.objects.all()

    if request.method =='POST':
     officeid = request.POST['officelists']
 
     
     if (officeid !='All'):
       officename ="All" 
       sqluser="SELECT  auth_user.id,auth_user.username AS username FROM  auth_user ,app_officeinfo WHERE auth_user.id =app_officeinfo.userid_id   AND app_officeinfo.id="+ format(officeid)  
       officeanems= StudentInfo.objects.raw( sqluser )

       for offname in officeanems:
         officename = offname.username 
       sqluser ="SELECT  app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_studentinfo,app_statustype  WHERE app_studentinfo.OfficeInfoid_id="+ format(officeid) +" AND app_studentinfo.statustype_id =app_statustype.id   GROUP BY app_studentinfo.statustype_id "       
       statusTypesNum = StatusType.objects.raw(sqluser ) #statusType
       sqluser="SELECT  * FROM app_studentinfo WHERE OfficeInfoid_id="+ format(officeid) + " ORDER BY id DESC   " 
       studentInfos= StudentInfo.objects.raw( sqluser )
     else:
       
       sqluser="SELECT  * FROM app_studentinfo   ORDER BY id DESC " 
       studentInfos= StudentInfo.objects.raw( sqluser )

       sqluser ="SELECT  app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_studentinfo,app_statustype   WHERE app_studentinfo.statustype_id =app_statustype.id  GROUP BY app_studentinfo.statustype_id "  
       statusTypesNum = StatusType.objects.raw(sqluser ) #statusType


    else:       
     sqluser="SELECT  * FROM app_studentinfo   ORDER BY id DESC " 
     studentInfos= StudentInfo.objects.raw( sqluser )

     sqluser ="SELECT  app_studentinfo.id, app_studentinfo.statustype_id, count(app_studentinfo.statustype_id) AS statustypeNum,app_statustype.name AS  statustypename FROM app_studentinfo,app_statustype   WHERE app_studentinfo.statustype_id =app_statustype.id  GROUP BY app_studentinfo.statustype_id "  
     statusTypesNum = StatusType.objects.raw(sqluser ) #statusType

    statusTypesNumAll=0 
    for typesnums in statusTypesNum:
      statusTypesNumAll += typesnums.statustypeNum
    statusTypes = StatusType.objects.raw("SELECT  * FROM app_statustype " ) #statusType
    studentStatus = StudentStatus.objects.raw("SELECT  * FROM app_studentstatus " )
    tableTitle ='Students Table'

    return render(
          request,
          'app/officepageManager.html',
          {
              'title':'officepageManager',
              'studentInfo':'studentInfo',
              'studentInfos' :studentInfos ,
              'officename' :officename,
              'statusTypesNumAll' :statusTypesNumAll,
              'officelists' : officelists, 
              'officepageManager' :'officepageManager',
              'username' :username, 
              'statusTypes':statusTypes,
              'seatslist' :'seatslist',
              'officepage':'officepage',
              'statusTypesNum' :statusTypesNum,
              'studentStatus':studentStatus,
              'tableTitle':tableTitle,
              'uploadfile' :'uploadfile',
              'officepage' :'officepage', 
              'logout_user' :'logout_user',
              'studendata' :'studendata',
              'newApplication':'newApplication',
              'seatslist' :'seatslist',
              'year':datetime.now().year,
          }
              
           
         )   
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )


def officepageAdmin(request,username):  
  try:
   userid =request.user.id      
   adminid = -1   

   adminids =User.objects.raw("SELECT * FROM auth_user WHERE is_staff=1 AND is_superuser=0 AND id ="+format(userid))  
   for admid in adminids:
       adminid= admid.id

 
   if (adminid !=-1): 
 
    userlists =   User.objects.all()
    tableTitle ='System Manager'

    return render(
          request,
          'app/officepageAdmin.html',
          {
              'title':'officepageAdmin',
              'officepageAdmin' :'officepageAdmin',
              'username' :username, 
              'userlists' :userlists,              
              'tableTitle':tableTitle,
              'uploadfile' :'uploadfile',   
              'UpdateAdmin' :'UpdateAdmin',
              'logout_user' :'logout_user',

              'year':datetime.now().year,  
          }
              
           
         )   
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )

def UpdateAdmin(request,ids):  
  try:
   userid =request.user.id      
   adminid = -1   

   adminids =User.objects.raw("SELECT * FROM auth_user WHERE is_staff=1 AND is_superuser=0 AND id ="+format(userid))  
   for admid in adminids:
       adminid= admid.id

 
   if (adminid !=-1): 
    username =request.user.username 
    if request.method =='POST':
     try:
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']          
        phone = request.POST['phone']
        address = request.POST['address']          
        residence = request.POST['residence'] 
        id =  request.POST['personid']          
        is_staff = request.POST['is_staff']
        is_active = request.POST['is_active']
        userType = request.POST['userType']   
        empType =   request.POST['empType']   
        passwordtemp = request.POST['password1']   
        password = make_password(passwordtemp)        
             
        if (password != ""):
          User.objects.filter(id=format(id)).update(first_name=firstname, last_name=lastname, username=username ,email=email,is_active=is_active, is_staff=is_staff ,password=password)  
        else:
          User.objects.filter(id=format(id)).update(first_name=firstname, last_name=lastname, username=username ,email=email,is_active=is_active, is_staff=is_staff,password=password)  
        allUserInfo = AllUserInfo.objects.filter(userid_id=format(id)).update(residence_id=residence, phone=phone, address=address)  

        User.objects.filter(id= format(id)).update(is_staff=False)
        try:
          emps= EmployeeInfo.objects.get(userid_id= format(id))
          emps.delete()
        except:
           pass
        try:
          emps= OfficeInfo.objects.get(userid_id= format(id))
          emps.delete()
        except:
           pass
        try:
          emps= ViewInfo.objects.get(userid_id= format(id))
          emps.delete()
        except:
           pass
        try:
          emps= ManagerInfo.objects.get(userid_id= format(id))
          emps.delete()
        except:
           pass
        
        
        if (userType =='Employee'):
          EmployeeInfo.objects.create(userid_id= format(id))
        if (userType =='Office'):
          OfficeInfo.objects.create(userid_id= format(id) ,employeeInfoid_id= empType)
        if (userType =='Viewer'):
          ViewInfo.objects.create(userid_id= format(id))
        if (userType =='Manager'):
          ManagerInfo.objects.create(userid_id= format(id))
        if (userType =='Admin'):
          User.objects.filter(id= format(id)).update(is_staff=True)
        
        #print("The accout had been updated.")

        return redirect('officepageAdmin',username)
     except Exception as identifier:            
        print(identifier)

    residence = StudentResidence.objects.all() 
    personinfo =   User.objects.filter(id=ids) 
    persons =   AllUserInfo.objects.filter(userid_id=format(ids) ) 

    sqluser="SELECT  auth_user.id ,auth_user.username ,app_employeeinfo.userid_id ,app_employeeinfo.id AS offid  FROM auth_user,app_employeeinfo WHERE  auth_user.id=app_employeeinfo.userid_id "
    empTypes= User.objects.raw(sqluser)
 
    userCreateionForm = UserCreationForm1()
    userTypeInfo ='NONE'
    userTypes = UserType.objects.filter()  
    usertemp = -1
    employeeIdOffice =1
    usertemp  = ManagerInfo.objects.filter(userid_id=ids).first()   
    if (usertemp != None):
     userTypeInfo ='Manager'
    usertemp  = ViewInfo.objects.filter(userid_id=ids).first()     
    if (usertemp != None):
     userTypeInfo ='Viewer'
    usertemp  = EmployeeInfo.objects.filter(userid_id=ids).first()    
    if (usertemp != None):
     userTypeInfo ='Employee'         
    usertemp  = OfficeInfo.objects.filter(userid_id=ids).first()   
    if (usertemp != None):
     userTypeInfo ='Office'
     employeeIdOffice = usertemp.employeeInfoid_id
    if (usertemp == None):
      adminid = -1
      adminids =User.objects.raw("SELECT * FROM auth_user WHERE is_staff=1 AND is_superuser=0 AND id ="+format(ids))  
      for admid in adminids:
        adminid= admid.id
      if (adminid !=-1):
        userTypeInfo ='Admin'
    tableTitle ='System Manager'

    return render(
          request,
          'app/updateAdmin.html',
          {
              'title':'UserUpdate',
              'officepageAdmin' :'officepageAdmin',
              'username' :username,               
              'personinfo' :personinfo,
              'residence' :residence,
              'userTypes' :userTypes,
              'employeeIdOffice': employeeIdOffice,
              'empTypes' :empTypes,
              'userTypeInfo': userTypeInfo,
              'persons' : persons,
              'tableTitle':tableTitle,
              'userCreateionForm':userCreateionForm,
              'UpdateAdmin' :'UpdateAdmin',
              'uploadfile' :'uploadfile',       
              'logout_user' :'logout_user',

              'year':datetime.now().year,
          }
              
           
         )   
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      )
    

def SendApplication(request):   
  
  try:
   officeInfoid =-1
   userid =request.user.id   
   sqluser="SELECT  auth_user.id,auth_user.username,app_officeinfo.userid_id ,app_officeinfo.id AS offid  FROM auth_user,app_officeinfo WHERE  auth_user.id=app_officeinfo.userid_id AND auth_user.id="+format(request.user.id)   
   officeInfoids= User.objects.raw(sqluser)

   for offid in officeInfoids:
    officeInfoid = offid.offid
   officename = "All"
   userid =request.user.id   
 
   if(officeInfoid !=-1):   
    username =request.POST['username']
    officeInfoid =0
    studentInfo = StudentInfo()
    sqluser="SELECT  auth_user.id,auth_user.username,app_officeinfo.userid_id ,app_officeinfo.id AS offid  FROM auth_user,app_officeinfo WHERE  auth_user.id=app_officeinfo.userid_id AND auth_user.username='"+ username+"'"  
    officeinfoids= User.objects.raw(sqluser)
    for officeId in officeinfoids:
            officeInfoid = officeId.offid

    if request.method =='POST':
      universityRegisterForm = UniversityRegisterForm(request.POST)
      studentRegisterForm = StudentRegisterForm(request.POST) 
      universityDegree  = UniversityDegreeForm(request.POST)
      studentPaperForm = StudentPaperForm(request.POST, request.FILES)
      universityDegree = UniversityDegree.objects.all()
      try:                   
          #add other info
          name =request.POST['name'] 
          surname =request.POST['surname']
          email =request.POST['email']
          referenceNo =request.POST['referenceNo']
          passportNo =request.POST['passportNo']
          nationality =request.POST['nationality']
          residence =request.POST['residence']
          phone =request.POST['phone']
          gender =request.POST['gender']
          degree =request.POST['degree']

          sqluser="SELECT id FROM app_UniversityDegree  WHERE degree='"+degree+"'"
          degreeids= UniversityDegree.objects.raw(sqluser)
          for degid in degreeids:
             degreeId = degid.id   
          
          studentids = 0
          try:
             studentids= StudentInfo.objects.last().id 
          except: 
           studentids = 1
          studentid = studentids+1
          referenceNo = passportNo+format(studentid+1)
          studentRegisterObj = StudentInfo.objects.create(degree_id=format(degreeId), officeInfoid_id =format(officeInfoid) ,name=name , surname=surname ,email=email ,referenceNo = referenceNo ,
                     passportNo= passportNo,nationality_id=format(nationality),residence_id= format(residence), phone=phone ,gender_id= format(gender)  )
          studentRegisterObj.save()
            
          #sqluser="SELECT id FROM app_StudentInfo  WHERE passportNo='"+format(passportNo)+"'"
          if (studentids != 1):
           studentids= StudentInfo.objects.last().id 
          #for stuid in studentids:
          #  studentid = stuid.id
          
          studentid = studentids
           #uploadsForm.is_valid():
          if request.method == 'POST' and request.FILES['picture']:                                                                       
             studentPaper = StudentPaper.objects.create( picture = request.FILES['picture'] , studentid_id =format(studentid) , degreePaper='Perosnal picture' )
             studentPaper.save()                  
             studentPaper = StudentPaper.objects.create( picture = request.FILES['passportfile'] , studentid_id =format(studentid) , degreePaper='Passport' )
             studentPaper.save()  

             if ( (degree == 'Diploma') or (degree == 'Bachelor') or (degree == 'Prep') ): #Here Add paper for degrees , manual to DB              
               studentPaper = StudentPaper.objects.create( picture = request.FILES['schoolDiploma'] , studentid_id =format(studentid) , degreePaper='School Diploma')
               studentPaper.save()  
               studentPaper = StudentPaper.objects.create( picture = request.FILES['schoolDiplomaTranscript'] , studentid_id =format(studentid) , degreePaper='School Diploma Transcript' )
               studentPaper.save()

             if ( (degree == 'Master') or (degree == 'PhD') ): #Here Add paper for degrees , manual to DB              
               studentPaper = StudentPaper.objects.create( picture = request.FILES['bachelorDiploma'] , studentid_id =format(studentid) , degreePaper='Bachelor Diploma' )
               studentPaper.save()
               if (degree == 'Master'):
                 studentPaper = StudentPaper.objects.create( picture = request.FILES['bachelorTranscript'] , studentid_id =format(studentid) , degreePaper='Bachelor Diploma Transcript' )
                 studentPaper.save()

               if (degree == 'PhD'):
                 studentPaper = StudentPaper.objects.create( picture = request.FILES['masterDiploma'] , studentid_id =format(studentid) , degreePaper= 'Master Diploma' )
                 studentPaper.save()
                 studentPaper = StudentPaper.objects.create( picture = request.FILES['masterTranscript'] , studentid_id =format(studentid) , degreePaper='Master Transcript' )
                 studentPaper.save()

               studentPaper = StudentPaper.objects.create( picture = request.FILES['recommendationLetter'] , studentid_id =format(studentid) , degreePaper='Recommendation Letter' )
               studentPaper.save()
               studentPaper = StudentPaper.objects.create( picture = request.FILES['CVimge'] , studentid_id =format(studentid) , degreePaper='C.V' )
               studentPaper.save()  

               

             #Save unviersity data
             departmentList = request.POST.getlist('department')
             universityNameList = request.POST.getlist('universityName')
             i=0
             for departmentName in departmentList:              
              sqluser="SELECT id FROM app_universityprogram  WHERE universityName_id='"+universityNameList[i]+"' AND department='"+departmentName + "'"  
              proids= UniversityProgram.objects.raw(sqluser)
              i= i+1
              for proid in proids:
                programid = proid.id 
              seatsRegistration = SeatsRegistration.objects.create(studentInfo_id =format(studentid) , universityProgram_id=format(programid) )

             #Save Document data              
             FilesLists = request.POST.getlist('filePaperName')
             for FilesLists in FilesLists:                        
              documentPaper = DocumentPaper.objects.create( documentFile = request.FILES['filePaper'] , studentid_id =format(studentid) , documentName=request.POST['filePaperName']    )
              documentPaper.save()        
            
      
      except Exception as identifier:            
        print(identifier)
      

    for offid in officeinfoids:
       officeInfoid = offid.offid
    studentInfo= StudentInfo.objects.raw("SELECT  * FROM app_studentinfo WHERE OfficeInfoid_id="+ format(officeInfoid)  )

    universityRegisterForm = UniversityRegisterForm()
    studentRegisterForm = StudentRegisterForm()
 
    universityNameList= UniversityName.objects.all()
    universityDegreeForm = UniversityDegreeForm()
    universityDegree = UniversityDegree.objects.all()
    referenceNo=  format(datetime.now().year)+'/'+format(userid)
    universityRegisterlist =  UniversityProgram.objects.raw(" SELECT id,universityName_id,department From app_universityProgram ")

    return render(
          request,
          'app/newApplication.html',
          {
              'title':'newApplication',
              'studentInfo' :studentInfo ,
              'universityNameList':universityNameList ,
              'universityRegisterlist' :universityRegisterlist,
              'universityRegisterForm':universityRegisterForm,                            
              'studentRegisterForm' :studentRegisterForm,
              'universityDegreeForm':universityDegreeForm,
              'studentPaperForm' :studentPaperForm,
              'universityDegree' :universityDegree,
              'referenceNo' : referenceNo,
              'studeninfo' :'studeninfo',
              'username' :username, 
              'logout_user' :'logout_user',
              'officepage' :'officepage',              
              'newApplication' :'newApplication', 
              'seatslist' :'seatslist',
              'year':datetime.now().year,
          }
         )  
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 
def UpdateInfo(request,username):   
 
    userid =request.user.id   
    officeid = -1
    employeeid = -1  
    adminids =OfficeInfo.objects.raw("SELECT id  FROM app_officeinfo WHERE userid_id ="+format(userid))                     
           
    for admid in adminids:
          officeid= admid.id

    adminids =EmployeeInfo.objects.raw("SELECT id  FROM app_employeeinfo WHERE userid_id ="+format(userid))                     

    for admid in adminids:
          employeeid= admid.id

    if  (employeeid !=-1) or  (officeid !=-1):     
    
    #Update data
      if request.method =='POST':
        try:
        
          studentid=request.POST['studentid'] 
          name =request.POST['name'] 
          surname =request.POST['surname']
          email =request.POST['email']        
          passportNo =request.POST['passportNo']
          nationality =request.POST['nationality']
          residence =request.POST['residence']
          statustype =request.POST['statusType']    
          phone =request.POST['phone']
          gender =request.POST['gender']
          documents = request.POST['documents']
          degreeId =request.POST['degree']
                  
          sqluser="SELECT * FROM app_UniversityDegree  WHERE id ='"+degreeId+"'"
          degreeids= UniversityDegree.objects.raw(sqluser)
          for degid in degreeids:
             degree = degid.degree   


          statustypeId= statustype 
          StudentInfo.objects.filter(pk=studentid).update(name=name,surname=surname,email=email,passportNo=passportNo ,phone=phone,documents=documents, nationality_id=format(nationality),residence_id=format(residence),gender_id=format(gender),degree_id=format(degreeId), statusType_id=format(statustypeId))
          sqlinfo = "SELECT  * FROM app_seatsregistration WHERE studentinfo_id="+  studentid  
          Seatstemps =SeatsRegistration.objects.raw(sqlinfo )
          for Seatstemp in Seatstemps:      
            Seatstemp.delete()
 
          departmentList = request.POST.getlist('department')
          universityNameList = request.POST.getlist('universityName')
          i=0
          for departmentName in departmentList:              
           sqluser="SELECT id FROM app_universityprogram  WHERE universityName_id='"+universityNameList[i]+"' AND department='"+departmentName + "'"  
           proids= UniversityProgram.objects.raw(sqluser)
           i= i+1
           for proid in proids:
             programid = proid.id 

           seatsRegistration = SeatsRegistration.objects.create( studentInfo_id =format(studentid) , universityProgram_id=format(programid) )
           seatsRegistration.save()  


          departmentList = request.POST.getlist('departmentA')
          universityNameList = request.POST.getlist('universityNameA')
          i=0
          for departmentName in departmentList:              
           sqluser="SELECT id FROM app_universityprogram  WHERE universityName_id='"+universityNameList[i]+"' AND department='"+departmentName + "'"  
           proids= UniversityProgram.objects.raw(sqluser)
           i= i+1
           for proid in proids:
             programid = proid.id 

           seatsRegistration = SeatsRegistration.objects.create( studentInfo_id =format(studentid) , universityProgram_id=format(programid) )
           seatsRegistration.save()  


          if request.method == 'POST':  
  
            if request.FILES.get('pictureu', False):     
             sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Perosnal picture' AND studentid_id="+format(studentid)
             Paperemps =StudentPaper.objects.raw(sqlinfo )
             for Paperemp in Paperemps: 
               os.remove(Paperemp.picture.path)
               Paperemp.delete()                             
               
             studentPaper = StudentPaper.objects.create( picture = request.FILES['pictureu'] , studentid_id =format(studentid) , degreePaper='Perosnal picture' )
             studentPaper.save()                  
            if request.FILES.get('passportfileu', False):  
             sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Passport' AND studentid_id="+format(studentid)
             Paperemps =StudentPaper.objects.raw(sqlinfo )
             for Paperemp in Paperemps:      
              os.remove(Paperemp.picture.path)
              Paperemp.delete()
              
             studentPaper = StudentPaper.objects.create( picture = request.FILES['passportfileu'] , studentid_id =format(studentid) , degreePaper='Passport' )
             studentPaper.save()  
 
            if ( (degree == 'Diploma') or (degree == 'Bachelor')  or (degree == 'Prep') ): #Here Add paper for degrees , manual to DB    
               sqlinfo = "SELECT  * FROM app_studentpaper WHERE   (degreePaper='Bachelor Diploma' OR  degreePaper='Bachelor Diploma Transcript'   OR degreePaper='Master Diploma' OR degreePaper='Master Transcript' OR degreePaper='Recommendation Letter'  OR degreePaper='C.V') AND studentid_id="+format(studentid)
               Paperemps =StudentPaper.objects.raw(sqlinfo )
               for Paperemp in Paperemps:    
                  os.remove(Paperemp.picture.path)
                  Paperemp.delete()

               if request.FILES.get('schoolDiplomau', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='School Diploma' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:   
                  os.remove(Paperemp.picture.path)
                  Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['schoolDiplomau'] , studentid_id =format(studentid) , degreePaper='School Diploma')
                 studentPaper.save()  
               if request.FILES.get('schoolDiploma', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='School Diploma' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:   
                  os.remove(Paperemp.picture.path)
                  Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['schoolDiploma'] , studentid_id =format(studentid) , degreePaper='School Diploma')
                 studentPaper.save()   

               if request.FILES.get('schoolDiplomaTranscriptu', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='School Diploma Transcript' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:  
                  os.remove(Paperemp.picture.path)
                  Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['schoolDiplomaTranscriptu'] , studentid_id =format(studentid) , degreePaper='School Diploma Transcript' )
                 studentPaper.save()
               if request.FILES.get('schoolDiplomaTranscript', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='School Diploma Transcript' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:  
                  os.remove(Paperemp.picture.path)                   
                  Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['schoolDiplomaTranscript'] , studentid_id =format(studentid) , degreePaper='School Diploma Transcript' )
                 studentPaper.save()


            if ( (degree == 'Master') or (degree == 'PhD') ): #Here Add paper for degrees , manual to DB  
               sqlinfo = "SELECT  * FROM app_studentpaper WHERE   (degreePaper='School Diploma' OR  degreePaper='School Diploma Transcript'   ) AND studentid_id="+format(studentid)
               Paperemps =StudentPaper.objects.raw(sqlinfo )
               for Paperemp in Paperemps:   
                  os.remove(Paperemp.picture.path)                 
                  Paperemp.delete()
               
               if request.FILES.get('bachelorDiplomau', False):
                sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Bachelor Diploma' AND studentid_id="+format(studentid)
                Paperemps =StudentPaper.objects.raw(sqlinfo )
                for Paperemp in Paperemps: 
                  os.remove(Paperemp.picture.path)
                  Paperemp.delete()

                studentPaper = StudentPaper.objects.create( picture = request.FILES['bachelorDiplomau'] , studentid_id =format(studentid) , degreePaper='Bachelor Diploma' )
                studentPaper.save()
               if request.FILES.get('bachelorDiploma', False):
                sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Bachelor Diploma' AND studentid_id="+format(studentid)
                Paperemps =StudentPaper.objects.raw(sqlinfo )
                for Paperemp in Paperemps:  
                  os.remove(Paperemp.picture.path)
                  Paperemp.delete()
                studentPaper = StudentPaper.objects.create( picture = request.FILES['bachelorDiploma'] , studentid_id =format(studentid) , degreePaper='Bachelor Diploma' )
                studentPaper.save()

               if (degree == 'Master'):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='School Diploma Transcript' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:  
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                 if request.FILES.get('bachelorTranscriptu', False):
                  sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Bachelor Diploma Transcript' AND studentid_id="+format(studentid)
                  Paperemps =StudentPaper.objects.raw(sqlinfo )
                  for Paperemp in Paperemps: 
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                  studentPaper = StudentPaper.objects.create( picture = request.FILES['bachelorTranscriptu'] , studentid_id =format(studentid) , degreePaper='Bachelor Diploma Transcript' )
                  studentPaper.save()

                 if request.FILES.get('bachelorTranscript', False):
                  sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Bachelor Diploma Transcript' AND studentid_id="+format(studentid)
                  Paperemps =StudentPaper.objects.raw(sqlinfo )
                  for Paperemp in Paperemps:    
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                  studentPaper = StudentPaper.objects.create( picture = request.FILES['bachelorTranscript'] , studentid_id =format(studentid) , degreePaper='Bachelor Diploma Transcript' )
                  studentPaper.save()
 

               if (degree == 'PhD'):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Bachelor Diploma Transcript' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps: 
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                 if request.FILES.get('masterDiplomau', False):
                  sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Master Diploma' AND studentid_id="+format(studentid)
                  Paperemps =StudentPaper.objects.raw(sqlinfo )
                  for Paperemp in Paperemps:  
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                  studentPaper = StudentPaper.objects.create( picture = request.FILES['masterDiplomau'] , studentid_id =format(studentid) , degreePaper='Master Diploma' )
                  studentPaper.save()

                 if request.FILES.get('masterDiploma', False):
                  sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Master Diploma' AND studentid_id="+format(studentid)
                  Paperemps =StudentPaper.objects.raw(sqlinfo )
                  for Paperemp in Paperemps:  
                   os.remove(Paperemp.picture.path)                    
                   Paperemp.delete()

                  studentPaper = StudentPaper.objects.create( picture = request.FILES['masterDiploma'] , studentid_id =format(studentid) , degreePaper='Master Diploma' )
                  studentPaper.save()


                 if request.FILES.get('masterTranscriptu', False):
                  sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Master Transcript' AND studentid_id="+format(studentid)
                  Paperemps =StudentPaper.objects.raw(sqlinfo )
                  for Paperemp in Paperemps:
                    os.remove(Paperemp.picture.path)
                    Paperemp.delete()

                  studentPaper = StudentPaper.objects.create( picture = request.FILES['masterTranscriptu'] , studentid_id =format(studentid) , degreePaper='Master Transcript' )
                  studentPaper.save()
                
                 if request.FILES.get('masterTranscript', False):
                  sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Master Transcript' AND studentid_id="+format(studentid)
                  Paperemps =StudentPaper.objects.raw(sqlinfo )
                  for Paperemp in Paperemps:     
                    os.remove(Paperemp.picture.path)
                    Paperemp.delete()

                  studentPaper = StudentPaper.objects.create( picture = request.FILES['masterTranscript'] , studentid_id =format(studentid) , degreePaper='Master Transcript' )
                  studentPaper.save()
  

               if request.FILES.get('recommendationLetteru', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Recommendation Letter' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:  
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['recommendationLetteru'] , studentid_id =format(studentid) , degreePaper='Recommendation Letter' )
                 studentPaper.save()

               if request.FILES.get('recommendationLetter', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='Recommendation Letter' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:   
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['recommendationLetter'] , studentid_id =format(studentid) , degreePaper='Recommendation Letter' )
                 studentPaper.save()

           

               if request.FILES.get('CVimgeu', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='C.V' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps:   
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['CVimgeu'] , studentid_id =format(studentid) , degreePaper='C.V' )
                 studentPaper.save()

               if request.FILES.get('CVimge', False):
                 sqlinfo = "SELECT  * FROM app_studentpaper WHERE degreePaper='C.V' AND studentid_id="+format(studentid)
                 Paperemps =StudentPaper.objects.raw(sqlinfo )
                 for Paperemp in Paperemps: 
                   os.remove(Paperemp.picture.path)
                   Paperemp.delete()

                 studentPaper = StudentPaper.objects.create( picture = request.FILES['CVimge'] , studentid_id =format(studentid) , degreePaper='C.V' )
                 studentPaper.save()
 
          if request.FILES.get('PaymentFile', False):
            sqlinfo = "SELECT  * FROM app_documentpaper WHERE documentName='"+Payment_Receipt_Uploaded +"' AND studentid_id="+format(studentid)
            documentpapers =DocumentPaper.objects.raw(sqlinfo)
            for Paperdoc in documentpapers: 
              os.remove(Paperdoc.documentFile.path)
              Paperdoc.delete()

            documentPaper = DocumentPaper.objects.create( documentFile = request.FILES['PaymentFile'] , studentid_id =format(studentid) , documentName=Payment_Receipt_Uploaded )
            documentPaper.save()        
            
            statustypeId =get_object_or_404(StatusType,name=Payment_Receipt_Uploaded )
            StudentInfo.objects.filter(pk=studentid).update( statusType_id=format(statustypeId.id))
 
          #Update new files Document data              
          FilesLists = request.POST.getlist('filePaperName')
          for FilesLists in FilesLists:                
           documentPaper = DocumentPaper.objects.create( documentFile = request.FILES['filePaper'] , studentid_id =format(studentid) , documentName=request.POST['filePaperName']    )
           documentPaper.save()        

          if (employeeid != -1):
           return redirect('officepageEmp',username)

          if (officeid != -1):
           return redirect('officepage',username)
        
        except Exception as identifier:            
          print(identifier)       
          return render(
           request,
           'app/login.html',
           {
              'title':'Main',
              'year':datetime.now().year,
           }
          ) 


def newApplication(request,username):   
   userid =request.user.id 
   officeid = -1    
   adminids =OfficeInfo.objects.raw("SELECT id  FROM app_officeinfo WHERE userid_id ="+format(userid))                                
   for admid in adminids:
       officeid= admid.id          

   if (officeid !=-1):  
    officeInfoid =0
    studentInfo = StudentInfo()
    sqluser="SELECT  auth_user.id,auth_user.username,app_officeinfo.userid_id ,app_officeinfo.id AS offid  FROM auth_user,app_officeinfo WHERE  auth_user.id=app_officeinfo.userid_id AND auth_user.username='"+ username+"'"  
    officeinfoids= User.objects.raw(sqluser)
 
    universityRegisterForm = UniversityRegisterForm()    
    studentRegisterForm = StudentRegisterForm()
 
    universityDegreeForm= UniversityDegreeForm()
    studentPaperForm  = StudentPaperForm()
    universityDegree = UniversityDegree.objects.all()
    referenceNo=  format(datetime.now().year)+'/'+format(userid)
    universityNameList= UniversityName.objects.all()
    universityRegisterlist =  UniversityProgram.objects.raw(" SELECT id,universityName_id,department From app_universityProgram ")

    return render(
          request,
          'app/newApplication.html',
          {
              'title':'newApplication',              
              'universityRegisterlist' :universityRegisterlist,
              'universityNameList':universityNameList,
              'universityRegisterForm':universityRegisterForm,              
              'studentRegisterForm' :studentRegisterForm,
              'universityDegreeForm':universityDegreeForm, 
              'studentPaperForm' :studentPaperForm,
              'universityDegree' :universityDegree ,
              'referenceNo' : referenceNo,
              'username' :username, 
              'logout_user' :'logout_user',
              'officepage' :'officepage', 
              'uploadfile' :'uploadfile', 
              'newApplication' :'newApplication', 
              'seatslist' :'seatslist',
              'year':datetime.now().year,
          }
         )  
 
def uploadfile(request,username):   
   
  try:   
   officeid = -1                     
   sqluser="SELECT   auth_user.id,app_employeeinfo.id AS offid  FROM auth_user,app_employeeinfo WHERE  auth_user.id=app_employeeinfo.userid_id AND auth_user.id="+format( request.user.id )
   officeinfoids= User.objects.raw(sqluser)
   for admid in officeinfoids:
       officeid= admid.offid  

   if (officeid !=-1):  
    return render(
          request,
          'app/uploadfile.html',
          {
              'title':'uploadfile', 
              'officepageEmp' :'officepageEmp', 
              'uploadfile' :'uploadfile', 
              'logout_user' :'logout_user',
              'newApplication' :'newApplication', 
              'seatslistEmp' :'seatslistEmp',
              'username' :username,    
              'year':datetime.now().year,
          }
         )  
  except:
   return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 

def seatslist(request,username):   
  
  try:
   officeInfoid =-1
   
   sqluser="SELECT  auth_user.id,auth_user.username,app_officeinfo.userid_id ,app_officeinfo.id AS offid  FROM auth_user,app_officeinfo WHERE  auth_user.id=app_officeinfo.userid_id AND auth_user.id="+format(request.user.id)   
   officeInfoids= User.objects.raw(sqluser)

   degreelist = UniversityDegree.objects.filter()

   for offid in officeInfoids:
    officeInfoid = offid.offid
  
   if(officeInfoid !=-1):    
     try:
      degreesId = request.POST['degrees']      
     except:
      degreesId =2
      
     degrees = UniversityDegree.objects.filter(id=degreesId)
     degreelists =UniversityDegree.objects.all()
     sqlseat="SELECT *   FROM  app_universityprogram WHERE universityDegree_id="+format(degreesId)# WHERE  activeSeat=0"     
     seatslist= UniversityProgram.objects.raw(sqlseat)

     tableTitle = 'Seats List'
     return render(
          request,
          'app/seatlist.html',
          {
              'title':'seatsList',
              'degrees':degrees,
              'degreelists':degreelists,
              'seatslist' :seatslist ,
              'degreelist' :degreelist,
              'username' :username, 
              'tableTitle' :tableTitle,
              'officepage' :'officepage', 
              'officepageManager' :'officepageManager',
              'logout_user' :'logout_user',
              'newApplication' :'newApplication', 
              'seatslist' :'seatslist',
              'year':datetime.now().year,
          }
         )
   else:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 
 
def seatslistEmp(request,username):   
  try:
   userid =request.user.id      
   employeeid = -1   
   adminids =EmployeeInfo.objects.raw("SELECT id  FROM app_employeeinfo WHERE userid_id ="+format(userid))                     

   for admid in adminids:
       employeeid= admid.id
 
   if (employeeid !=-1):
     try:
      degreesId = request.POST['degrees']      
     except:
      degreesId =2
      
     degrees = UniversityDegree.objects.filter(id=degreesId)
     degreelists =UniversityDegree.objects.all()
     sqlseat="SELECT *   FROM  app_universityprogram WHERE universityDegree_id="+format(degreesId)# WHERE  activeSeat=0"     
     seatslist= UniversityProgram.objects.raw(sqlseat)

     tableTitle = 'Seats List'
     return render(
          request,
          'app/seatlistEmp.html',
          {
              'title':'seatsList',              
              'username' :username, 
              'seatslist':seatslist,
              'degreelists' :degreelists,
              'degrees' :degrees,
              'tableTitle' :tableTitle,
              'uploadfile' :'uploadfile',
              'officepageEmp' :'officepageEmp', 
              'logout_user' :'logout_user',                
              'seatslistEmp' :'seatslistEmp',
              'year':datetime.now().year,
          }
         )
   else:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 

  except:
      return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 

def seatslistView(request,username):   
  
  try:
   viewerid =-1
   sqluser="SELECT  auth_user.id,auth_user.username,app_viewinfo.userid_id ,app_viewinfo.id AS offid  FROM auth_user,app_viewinfo WHERE  auth_user.id=app_viewinfo.userid_id AND auth_user.id="+format(request.user.id)   
   adminids= User.objects.raw(sqluser)
          
   for admid in adminids:
        viewerid= admid.id

  
   if(viewerid !=-1):    
     try:
      degreesId = request.POST['degrees']      
     except:
      degreesId =2
      
     degrees = UniversityDegree.objects.filter(id=degreesId)
     degreelists =UniversityDegree.objects.all()
     sqlseat="SELECT *   FROM  app_universityprogram WHERE universityDegree_id="+format(degreesId)# WHERE  activeSeat=0"     
     seatslist= UniversityProgram.objects.raw(sqlseat)

     tableTitle = 'Seats List'
     return render(
          request,
          'app/seatlistView.html',
          {
              'title':'seatsList',
              'degrees':degrees,
              'degreelists':degreelists,
              'seatslist' :seatslist ,
              'username' :username, 
              'tableTitle' :tableTitle,
              'officepageView' :'officepageView', 
              'logout_user' :'logout_user',
              'seatslistView' :'seatslistView',
              'year':datetime.now().year,
          }
         )
   else:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 
  except:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 

def officepageView(request,username):   

  #if not request.user.is_authenticated:
   userid =request.user.id 
   if userid is not None:   
     try:
      degreesId = request.POST['degrees']      
     except:
      degreesId =2
      
     degrees = UniversityDegree.objects.filter(id=degreesId)
     degreelists =UniversityDegree.objects.all()
     sqlseat="SELECT *   FROM  app_universityprogram WHERE universityDegree_id="+format(degreesId)# WHERE  activeSeat=0"     
     seatlist= UniversityProgram.objects.raw(sqlseat)
     tableTitle = 'Seats List'
     return render(
          request,
          'app/officepageView.html',
          {
              'title':'seatsList',
              'seatslistView' :'seatslistView' ,
              'seatlist' :seatlist ,
              'degreelists':degreelists,
              'username' :username,              
              'degrees' : degrees,
              'officepageView' :'officepageView',
              'tableTitle' :tableTitle,
              'logout_user' :'logout_user',                              
              'year':datetime.now().year,
          }
         )
   else:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 



def studendata(request, studentId):   
  #if not request.user.is_authenticated:
   userid =request.user.id   
   officeid = -1   
   adminids =OfficeInfo.objects.raw("SELECT id  FROM app_officeinfo WHERE userid_id ="+format(userid))                     
           
   for admid in adminids:
        officeid= admid.id
 
 
   if   (officeid !=-1): 
     username = request.user.username 
     sqlInfo=  "SELECT  * FROM app_studentinfo WHERE id="+ studentId   
     studentInfos= StudentInfo.objects.raw(sqlInfo)

     sqlInfo=  "SELECT  * FROM app_seatsregistration WHERE studentInfo_id="+ studentId   
     seatsRegistrations= SeatsRegistration.objects.raw(sqlInfo)

 
     #sqlInfo=  "SELECT  * FROM app_studentPaper WHERE studentid_id="+ studentId   
     studentPaperlist= StudentPaper.objects.filter(studentid_id =studentId)

     sqlInfo=  "SELECT  app_universityprogram.universityname ,app_universityprogram.department  FROM app_seatsregistration,app_universityprogram WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id "  
     sqlInfo=  "  SELECT  app_universityprogram.universityname_id ,app_universityname.universityName    FROM app_seatsregistration,app_universityprogram ,app_universityname WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id  AND  app_universityname.id =app_universityprogram.universityname_id  "
     #sqlInfo= "  SELECT app_seatsregistration.id,app_universityprogram.universityname_id,app_universityprogram.department AS department ,app_universityname.universityname  AS universityname ,app_universityprogram.department   FROM     app_seatsregistration,app_universityprogram ,app_universityname WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id  AND  app_universitydepartment.id=app_universityprogram.department_id  AND app_universityname.id =app_universityprogram.universityname_id "
     sqlInfo= "  SELECT app_seatsregistration.id,app_universityprogram.universityname_id,app_universityprogram.department AS department ,app_universityname.universityname  AS universityname ,app_universityprogram.id  AS universityprogramId FROM     app_seatsregistration,app_universityprogram ,app_universityname WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id  AND  app_universityname.id =app_universityprogram.universityname_id "
     seatsRegistrationslist= SeatsRegistration.objects.raw(sqlInfo)
 
     statusTypeForm = StatusType.objects.all()
     studentResidenceForm = StudentResidence.objects.all()
     studentNationalityForm = StudentNationality.objects.all()
     universityNameList =  UniversityName.objects.all()      

     studentGendereForm = StudentGender.objects.all()
     universityDegreeForm = UniversityDegree.objects.all()
     universityRegisterForm = UniversityRegisterForm()
     universityRegisterlist =  UniversityProgram.objects.raw(" SELECT id,universityName_id,department From app_universityProgram  ")
     documentPaperList =  DocumentPaper.objects.raw(" SELECT * From app_documentpaper  WHERE studentid_id="+ studentId )
     
     studentPaperForm = StudentPaperForm()
     tableTitle = 'Student Information'
 
     return render(
          request,
          'app/studendata.html',
          {
              'title':'StudentInfo', 
              'username' :username, 
              'tableTitle' :tableTitle,
              'statusTypeForm':statusTypeForm,
              'universityRegisterlist': universityRegisterlist,
              'universityNameList':universityNameList,              
              'universityDegreeForm' :universityDegreeForm,
              'studentPaperlist':studentPaperlist,
              'documentPaperList' :documentPaperList,
              'seatsRegistrationslist' :seatsRegistrationslist,
              'studentGendereForm' :studentGendereForm,
              'studentNationalityForm':studentNationalityForm,
              'studentResidenceForm' :studentResidenceForm,
              'studentPaperForm' :studentPaperForm,
              'universityRegisterForm':universityRegisterForm,              
              'officepage' :'officepage',               
              'studendata':'studendata',
              'seatsRegistrations': seatsRegistrations,
              'studentInfos' :studentInfos,
              'logout_user' :'logout_user',
              'newApplication' :'newApplication', 
              'seatslist' :'seatslist',
              'UpdateInfo' :'UpdateInfo',
              'year':datetime.now().year,
          }
         )
   else:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 

 
def studendataEmp(request, studentId):   
  #if not request.user.is_authenticated:
   userid =request.user.id      
   employeeid = -1   

   adminids =EmployeeInfo.objects.raw("SELECT id  FROM app_employeeinfo WHERE userid_id ="+format(userid))                     

   for admid in adminids:
       employeeid= admid.id

 
   if (employeeid !=-1): 
     username = request.user.username 
     sqlInfo=  "SELECT  * FROM app_studentinfo WHERE id="+ studentId   
     studentInfos= StudentInfo.objects.raw(sqlInfo)

     sqlInfo=  "SELECT  * FROM app_seatsregistration WHERE studentInfo_id="+ studentId   
     seatsRegistrations= SeatsRegistration.objects.raw(sqlInfo)

 
     #sqlInfo=  "SELECT  * FROM app_studentPaper WHERE studentid_id="+ studentId   
     studentPaperlist= StudentPaper.objects.filter(studentid_id =studentId)

     sqlInfo=  "SELECT  app_universityprogram.universityname ,app_universityprogram.department  FROM app_seatsregistration,app_universityprogram WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id "  
     sqlInfo=  "  SELECT  app_universityprogram.universityname_id ,app_universityname.universityName    FROM app_seatsregistration,app_universityprogram ,app_universityname WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id  AND  app_universityname.id =app_universityprogram.universityname_id  "
     #sqlInfo= "  SELECT app_seatsregistration.id,app_universityprogram.universityname_id,app_universityprogram.department AS department ,app_universityname.universityname  AS universityname ,app_universityprogram.department   FROM     app_seatsregistration,app_universityprogram ,app_universityname WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id  AND  app_universitydepartment.id=app_universityprogram.department_id  AND app_universityname.id =app_universityprogram.universityname_id "
     sqlInfo= "  SELECT app_seatsregistration.id,app_universityprogram.universityname_id,app_universityprogram.department AS department ,app_universityname.universityname  AS universityname ,app_universityprogram.id  AS universityprogramId FROM     app_seatsregistration,app_universityprogram ,app_universityname WHERE app_seatsregistration.studentInfo_id="+ studentId +   " And app_seatsregistration.universityProgram_id=app_universityprogram.id  AND  app_universityname.id =app_universityprogram.universityname_id "
     seatsRegistrationslist= SeatsRegistration.objects.raw(sqlInfo)
 
     statusTypeForm = StatusType.objects.all()
     studentResidenceForm = StudentResidence.objects.all()
     studentNationalityForm = StudentNationality.objects.all()
     universityNameList =  UniversityName.objects.all()      

     studentGendereForm = StudentGender.objects.all()
     universityDegreeForm = UniversityDegree.objects.all()
     universityRegisterForm = UniversityRegisterForm()
     universityRegisterlist =  UniversityProgram.objects.raw(" SELECT id,universityName_id,department From app_universityProgram  ")
     documentPaperList =  DocumentPaper.objects.raw(" SELECT * From app_documentpaper  WHERE studentid_id="+ studentId )
     
     studentPaperForm = StudentPaperForm()
     tableTitle = 'Student Information'
 
     return render(
          request,
          'app/studendataEmp.html',
          {
              'title':'StudentInfo', 
              'username' :username, 
              'tableTitle' :tableTitle,
              'statusTypeForm':statusTypeForm,
              'universityRegisterlist': universityRegisterlist,
              'universityNameList':universityNameList,              
              'universityDegreeForm' :universityDegreeForm,
              'studentPaperlist':studentPaperlist,
              'documentPaperList' :documentPaperList,
              'seatsRegistrationslist' :seatsRegistrationslist,
              'studentGendereForm' :studentGendereForm,
              'studentNationalityForm':studentNationalityForm,
              'studentResidenceForm' :studentResidenceForm,
              'studentPaperForm' :studentPaperForm,
              'universityRegisterForm':universityRegisterForm,
              'uploadfile' :'uploadfile', 
              'officepageEmp' :'officepageEmp',               
              'studendata':'studendata',
              'seatsRegistrations': seatsRegistrations,
              'studentInfos' :studentInfos,
              'logout_user' :'logout_user',              
              'seatslistEmp' :'seatslistEmp',
              'UpdateInfo' :'UpdateInfo',
              'year':datetime.now().year,
          }
         )
   else:
    return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
      ) 

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.method =='POST':
      
      form = LoginForm()
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username =username ,password = password) 
      if user is not None:

          login(request,user)
          userid =request.user.id
          officeid = -1
          employeeid = -1
          viewid = -1
          Managerid =-1
          adminid = -1

          adminids =OfficeInfo.objects.raw("SELECT id  FROM app_officeinfo WHERE userid_id ="+format(userid))                     
           
          for admid in adminids:
               officeid= admid.id

          adminids =EmployeeInfo.objects.raw("SELECT id  FROM app_employeeinfo WHERE userid_id ="+format(userid))                     

          for admid in adminids:
               employeeid= admid.id

          adminids =ViewInfo.objects.raw("SELECT id  FROM app_viewinfo WHERE userid_id ="+format(userid))                     

          for admid in adminids:
               viewid= admid.id

          adminids =ManagerInfo.objects.raw("SELECT id  FROM app_managerinfo WHERE userid_id ="+format(userid))                     

          for admid in adminids:
               Managerid= admid.id
               
          adminid = -1
           

          #adminid =     get_object_or_404(User,"SELECT * FROM auth_user WHERE is_staff=1 AND is_superuser=0 AND userid ="+format(userid))                     
          adminids =  User.objects.raw("SELECT * FROM auth_user WHERE is_staff=1 AND is_superuser=0 AND id ="+format(userid))                     
          for admid in adminids:
               adminid= admid.id

          if (employeeid !=-1):
              return redirect('officepageEmp',username)

          if (officeid  !=-1):
              return redirect('officepage',username)

          if (viewid  !=-1):
              return redirect('officepageView',username)

          if  (Managerid !=-1):
              return redirect('officepageManager',username)

          if  (adminid !=-1):
              return redirect('officepageAdmin',username)


          if  (officeid ==-1) & (employeeid ==-1) & (viewid ==-1)  & (Managerid ==-1) & (adminid ==-1)   :
              return redirect('adminpage')
            
        
      else:                 
         return render(
          request,
          'app/login.html',
          {
              'title':'Main',
              'year':datetime.now().year,
          }
         )


    else:
      return render(
          request,
          'app/login.html',
          {
              'title':'Main',               
              'year':datetime.now().year,
          }
      )

def loginMain(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Main',
            'year':datetime.now().year,
        }
    )

def register(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    model = User
    form =OfficeInfoForm()
    alluserInfoForm =AllUserInfoForm()
    if request.method =='POST':
      form= OfficeInfoForm(request.POST)
      #form1 = UserCreateionForm(request.POST)
      if form.is_valid():
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']          
        passwordtemp = request.POST['password1'] 
        password = make_password(passwordtemp)
        confirmpassword = request.POST['password2']

        userinfo = User.objects.create(first_name=firstname, last_name=lastname, username=username ,email=email ,password=password)  
        
        
        residence = request.POST['residence']          
        phone = request.POST['phone']    
        address = request.POST['address']    
        
        userids =User.objects.raw("SELECT  id   FROM  auth_user    WHERE username='"+  username +"'")        
        for stuid in userids:
           userid = stuid.id   
        allUserInfo = AllUserInfo.objects.create( userid_id=userid ,residence_id=residence, phone=phone, address=address)  
     
        return redirect('home')
 
    return render(
        request,
        'app/register.html',
        {
            'title':'Register',
            'officeInfoForm' : form  ,
            'alluserInfoForm' :alluserInfoForm,
            'message':'Register your office.',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )




 
