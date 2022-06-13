"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import Select  
from  .models import OfficeInfo ,UniversityProgram ,StudentResidence,  StudentInfo ,AllUserInfo  ,UniversityDegree ,StudentPaper ,DegreePaper ,StatusType
from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _ 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
 


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class LoginForm(forms.ModelForm):
        username = forms.CharField(label='Username' )
        password = forms.CharField(label='Password' ,widget =forms.PasswordInput() )
        class Meta:
            model  = User
            fields =('username' , 'password')

class UserCreationForm1(forms.ModelForm):
    
    password1 = forms.CharField(label='New password' , widget =forms.PasswordInput() ,min_length = 8 , required=False)
    password2 = forms.CharField(label='Confirm password' ,widget =forms.PasswordInput() ,min_length = 8, required=False)
    class Meta:
        model  = User
        fields =(   'password1','password2')
    
    #def clean_password2(self):
    #    cd =self.cleaned_data
    #    if cd['password1'] != cd['password2']:
    #        raise forms.ValidationError('Passwords is not matching')
    #    return  cd['password2']
 

 
#class OfficeInfoForm(forms.ModelForm):
class OfficeInfoForm(UserCreationForm):
        first_name = forms.CharField(max_length=32, help_text='First name')
        last_name = forms.CharField(max_length=32, help_text='Last name')
        email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
        address = forms.CharField(max_length=32, help_text='Address')
        phone = forms.CharField(max_length=32, help_text='Phone')
        residence =forms.ModelChoiceField(label='Residence' ,queryset=StudentResidence.objects.all(),initial=1, widget=forms.Select())  
        #forms.SelectMultiple(queryset=UniversityProgram.objects.all(),initial=1) # forms.CharField(max_length=32, help_text='Residence')
        
        #firstname = forms.CharField(label='First name' , widget=forms.TextInput(attrs={'placeholder':('First name')}  ))# help_text='Only letter')
        #lastname = forms.CharField(label='Last name' ,widget=forms.TextInput(attrs={'placeholder':('Last name')}  ))# help_text='Only letter')
        #username = forms.CharField(label='User name'  , widget=forms.TextInput(attrs={'placeholder':('User name')}  ))# help_text='Only letter')
        #email = forms.CharField(label='Email Address' , widget=forms.EmailInput(attrs={'placeholder':('Email Address')}))          
        #password = forms.CharField(label='Password' ,widget =forms.PasswordInput(attrs={'placeholder':('Password')}) ,min_length = 8 )
        #confirmpassword = forms.CharField(label='Confirm Password' ,widget =forms.PasswordInput(attrs={'placeholder':('Confirm Password')}) ,min_length = 8) 
       
 
        class Meta(UserCreationForm.Meta):
          model  = User  
          fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','address','phone','residence')
          #fields =('username' , 'firstname','lastname',   'email',  'password' ,'confirmpassword'  )
          widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'residence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Residence'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
         }
 
    
        def clean_password2(self):
          cd =self.cleaned_data
          if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords is not matching')
          return  cd['password2']
 
         
class AllUserInfoForm(forms.ModelForm):
        address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Address')}))
        residence = forms.SelectMultiple() #forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Country')}))
        phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Phone Number')}))

        class Meta:
          model  = AllUserInfo         
          fields =('address', 'residence','phone' )

  
          

class UniversityProgramForm(forms.ModelForm):
    class Meta:
        model = UniversityProgram
        fields =( 'universityName','language','universityName','universityDegree','department','universityCity',
                  'thesis','numberOfYears','notes','taksitFees','systemOfPayment')
        
class UniversityRegisterForm(forms.ModelForm):
    universityName =  forms.SelectMultiple()
    #department =  forms.SelectMultiple()
    #department  = forms.ModelChoiceField(label='department' ,queryset=UniversityProgram.objects.filter().only("universityName", "department"),initial=1, widget=forms.Select(attrs={"onclick":'SelectDep2(this)'}))  
    department  = forms.ModelChoiceField(label='department' ,queryset=UniversityProgram.objects.all(),initial=1, widget=forms.Select(attrs={"onclick":'SelectDep2(this)'}))  
    #department =  forms.SelectMultiple(queryset=UniversityProgram.objects.all(),to_field_name='department')  
    class Meta:
        model  = UniversityProgram
        fields = ('universityDegree','universityName','department' 
                    #auto added to form                
                 )   

class StudentRegisterForm(forms.ModelForm):
 
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Name')}  ))# help_text='Only letter')
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Surname')}  ))# help_text='Only letter')
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':('Email Address')}))  
    
    referenceNo = forms.CharField(label='Reference  Number',widget =forms.TextInput(attrs={'placeholder':('Reference Number')}) )    
    passportNo = forms.CharField(label='Passport Number',widget =forms.TextInput(attrs={'placeholder':('Passport Number')}) )    
    nationality =  forms.SelectMultiple()
    residence =  forms.SelectMultiple()
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':('Phone Number')}))
    #gender =  forms.SelectMultiple(attrs={'class': 'chosen','name':'gender'})  
    gender =  forms.SelectMultiple()      
    officeInfoid = forms.SelectMultiple() #forms.CharField(widget=forms.TextInput(attrs={'placeholder':('OfficeInfoid')}))

    class Meta:
        model = StudentInfo
        fields =('name','surname','officeInfoid','email','nationality' , 'residence',
                 'gender' , 'referenceNo' , 
                 'passportNo'  )  #null accept
                 #referenceNo ,documents ,statusType   #auto added to form                
                 

class UniversityDegreeForm(forms.ModelForm):
        #degree = forms.SelectMultiple()  
        degree  = forms.ModelChoiceField(label='Degree' ,queryset=UniversityDegree.objects.all(),initial=1)
        class Meta:
            model  = UniversityDegree
            fields = ['degree', ]
            

class StudentPaperForm(forms.ModelForm):
        #degree = forms.SelectMultiple()  
        picture = forms.FileField(label='picture',widget=forms.FileInput(attrs={'accept':'.pdf'}) )
        studentid = forms.ModelChoiceField(label='Student name', queryset=StudentInfo.objects.all(),initial=1)
        degreePaper = forms.CharField(label='Degree Paper')
        class Meta:
            model  = StudentPaper
            fields =['studentid' ,'picture','degreePaper']             