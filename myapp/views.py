from copyreg import constructor
from email import message
from django.shortcuts import render ,  redirect
from django.contrib import messages
from .models import Psychomotor, Psychomotor1, Psychomotor2, UserDetail , Cognitive , Cognitive1 , AffectiveDomain , AffectiveDomain1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'index.html')

def steps(request):
    return render(request,'steps.html')

def query(request):
    return render(request,'query.html')

def reset(request):
    UserDetail.objects.all().delete()
    Psychomotor.objects.all().delete()
    Psychomotor1.objects.all().delete()
    Psychomotor2.objects.all().delete()
    Cognitive.objects.all().delete()
    Cognitive1.objects.all().delete()
    AffectiveDomain.objects.all().delete()
    AffectiveDomain1.objects.all().delete()
    User.objects.all().delete()
    logout(request)
    return redirect('/')

def basicDetails(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        childs_name = request.POST['childs-name']
        relationship = request.POST['relationship']
        childs_age = request.POST['age']

        ins = UserDetail(name=name,email=email,childs_name=childs_name,relationship=relationship,childs_age=childs_age)
        ins.save()
        user = User.objects.create_user(name)
        password = user.set_password(name+email)
        user.save()
        authenticate(username=user, password=password)
        login(request,user)
        return redirect('selectTest')
        
    return render(request,'basicDetails.html')

@login_required(login_url='/')
def selectTest(request):
    return render(request,'selectTest.html')

@login_required(login_url='/')
def psychomotor(request):
    if(request.method == 'POST'):
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        ins = Psychomotor(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
        ins.save()
        return redirect('psychomotor1')
    return render(request,'psychomotor.html')

@login_required(login_url='/')
def psychomotor1(request):
    if(request.method == 'POST'):
        q6 = request.POST['q6']
        q7 = request.POST['q7']
        q8 = request.POST['q8']
        q9a = request.POST['q9a']
        q9b = request.POST['q9b']
        q9c = request.POST['q9c']
        q10a = request.POST['q10a']
        q10b = request.POST['q10b']
        q10c = request.POST['q10c']
        ins = Psychomotor1(q6=q6,q7=q7,q8=q8,q9a=q9a,q9b=q9b,q9c=q9c,q10a=q10a,q10b=q10b,q10c=q10c)
        ins.save()
        return redirect('psychomotor2')
    return render(request,'psychomotor1.html')

@login_required(login_url='/')
def psychomotor2(request):
    if(request.method == 'POST'):
        q11a = request.POST['q11a']
        q11b = request.POST['q11b']
        q11c = request.POST['q11c']
        q12a = request.POST['q12a']
        q12b = request.POST['q12b']
        q12c = request.POST['q12c']
        q13a = request.POST['q13a']
        q13b = request.POST['q13b']
        q13c = request.POST['q13c']
        q14a = request.POST['q14a']
        q14b = request.POST['q14b']
        q14c = request.POST['q14c']
        ins = Psychomotor2(q11a=q11a,q11b=q11b,q11c=q11c,q12a=q12a,q12b=q12b,q12c=q12c,q13a=q13a,q13b=q13b,q13c=q13c,q14a=q14a,q14b=q14b,q14c=q14c)
        ins.save()
        messages.success(request,'Thank You.')
        return redirect('result')
    return render(request,'psychomotor2.html')

@login_required(login_url='/')
def result(request):
    mydata = UserDetail.objects.all().values()
    psy = Psychomotor.objects.all().values()
    psy1 = Psychomotor1.objects.all().values()
    psy2 = Psychomotor2.objects.all().values()

    name = mydata[len(mydata)-1].get('name')
    email = mydata[len(mydata)-1].get('email')
    childs_name = mydata[len(mydata)-1].get('childs_name')
    relationship = mydata[len(mydata)-1].get('relationship')
    childs_age = mydata[len(mydata)-1].get('childs_age')

    q1 = psy[len(psy)-1].get('q1')
    q2 = psy[len(psy)-1].get('q2')
    q3 = psy[len(psy)-1].get('q3')
    q4 = psy[len(psy)-1].get('q4')
    q5 = psy[len(psy)-1].get('q5')
    
    q6 = psy1[len(psy1)-1].get('q6')
    q7 = psy1[len(psy1)-1].get('q7')
    q8 = psy1[len(psy1)-1].get('q8')
    q9a = psy1[len(psy1)-1].get('q9a')
    q9b = psy1[len(psy1)-1].get('q9b')
    q9c = psy1[len(psy1)-1].get('q9c')
    q10a = psy1[len(psy1)-1].get('q10a')
    q10b = psy1[len(psy1)-1].get('q10b')
    q10c = psy1[len(psy1)-1].get('q10c')

    q11a = psy2[len(psy2)-1].get('q11a')
    q11b = psy2[len(psy2)-1].get('q11b')
    q11c = psy2[len(psy2)-1].get('q11c')
    q12a = psy2[len(psy2)-1].get('q12a')
    q12b = psy2[len(psy2)-1].get('q12b')
    q12c = psy2[len(psy2)-1].get('q12c')
    q13a = psy2[len(psy2)-1].get('q13a')
    q13b = psy2[len(psy2)-1].get('q13b')
    q13c = psy2[len(psy2)-1].get('q13c')
    q14a = psy2[len(psy2)-1].get('q14a')
    q14b = psy2[len(psy2)-1].get('q14b')
    q14c = psy2[len(psy2)-1].get('q14c')

    context = {
        'name' : name , 
        'email' : email,
        'childs_name': childs_name,
        'relationship': relationship,
        'childs_age': childs_age,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'q5': q5,
        'q6': q6,
        'q7': q7,
        'q8': q8,
        'q9a': q9a,
        'q9b': q9b,
        'q9c': q9c,
        'q10a': q10a,
        'q10b': q10b,
        'q10c': q10c,
        'q11a': q11a,
        'q11b': q11b,
        'q11c': q11c,
        'q12a': q12a,
        'q12b': q12b,
        'q12c': q12c,
        'q13a': q13a,
        'q13b': q13b,
        'q13c': q13c,
        'q14a': q14a,
        'q14b': q14b,
        'q14c': q14c
    }

    return render(request,'result.html' , context)

@login_required(login_url='/')
def cognitive(request):
    if(request.method == 'POST'):
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']
        ins = Cognitive(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5,q6=q6)
        ins.save()
        return redirect('cognitive1')
        
    return render(request,'cognitive.html')

@login_required(login_url='/')
def cognitive1(request):
    if(request.method == 'POST'):
        q7 = request.POST['q7']
        q8 = request.POST['q8']
        q9 = request.POST['q9']
        q10 = request.POST['q10']
        q11 = request.POST['q11']
        ins = Cognitive1(q7=q7,q8=q8,q9=q9,q10=q10,q11=q11)
        ins.save()
        return redirect('cognitive_result')
    return render(request,'cognitive1.html')

@login_required(login_url='/')
def cognitive_result(request):
    mydata = UserDetail.objects.all().values()
    cog = Cognitive.objects.all().values()
    cog1 = Cognitive1.objects.all().values()

    name = mydata[len(mydata)-1].get('name')
    email = mydata[len(mydata)-1].get('email')
    childs_name = mydata[len(mydata)-1].get('childs_name')
    relationship = mydata[len(mydata)-1].get('relationship')
    childs_age = mydata[len(mydata)-1].get('childs_age')

    q1 = cog[len(cog)-1].get('q1')
    q2 = cog[len(cog)-1].get('q2')
    q3 = cog[len(cog)-1].get('q3')
    q4 = cog[len(cog)-1].get('q4')
    q5 = cog[len(cog)-1].get('q5')
    q6 = cog[len(cog)-1].get('q6')

    q7 = cog1[len(cog1)-1].get('q7')
    q8 = cog1[len(cog1)-1].get('q8')
    q9 = cog1[len(cog1)-1].get('q9')
    q10 = cog1[len(cog1)-1].get('q10')
    q11 = cog1[len(cog1)-1].get('q11')

    Yesarr = []
    Noarr = []
    if(q1 == 'Yes'):
        Yesarr.append('Not justified:- derange mental coordination-requires counselling by Psychologist/Medical Attention to improve coordination and intellectuality between parents and child. ')
    else:
        Noarr.append('Normal intellectuality')           
    if(q2 == 'Yes'):
        Yesarr.append('Lack in self-confidence:- needs more attention by parents to boost his/her mental confidence/psychologist consultation')
    else:
        Noarr.append('Normal')    
    if(q3 == 'Yes'):
        Yesarr.append('Confused state of mind:- needs to be relaxed and to remain free from to be disturbed by others. ')
    else:
        Noarr.append('Normal.')    
    if(q4 == 'Yes'):
        Yesarr.append('Normal state of mind.')
    else:
        Noarr.append('Unsocial/lintrovert:- needsmore parentalattention/psychologist consultation')    
    if(q5 == 'Yes'):
        Yesarr.append('Emotional and sensitive:- needs to socialized more. More attention of parents are essential. ')
    else:
        Noarr.append('Normal')
    if(q6 == 'Yes'):
        Yesarr.append('Mentally Hyperactive:-needs psychologist intervention')
    else:
        Noarr.append('Normal')           
    if(q7 == 'Yes'):
        Yesarr.append('Normal')
    else:
        Noarr.append('Confused stateof mind needs corrections/counseling by Psychologist')    
    if(q8 == 'Yes'):
        Yesarr.append('Derangement ofMotor (Brain) activity needs more attention by parents and counselling bythe Psychologist..')
    else:
        Noarr.append('Normal')    
    if(q9 == 'Yes'):
        Yesarr.append('Abnormal state of fearness/too emotional:- needs corrections by parents/counselling by Psychologist. ')
    else:
        Noarr.append('Normal')    
    if(q10 == 'Yes'):
        Yesarr.append('Mental retardation-needs more attention by parents/medical attention is required to find out under lying causes')
    else:
        Noarr.append('Normal ')
    if(q10 == 'Yes'):
        Yesarr.append('Mental disorder- needs more attention by parents/medical attention is required to find out under lying causes.')
    else:
        Noarr.append('Normal ')
    Mainarr = Yesarr + Noarr 
    str1 = " " 
    Mainstr = str1.join(Mainarr)
    MainStrUpper = Mainstr.upper()
    normal = MainStrUpper.count("NORMAL")
    normal2 = (normal/11)*100
    other = (100-normal2)
    print(other,normal2)
    context = {
        'name' : name , 
        'email' : email,
        'childs_name': childs_name,
        'relationship': relationship,
        'childs_age': childs_age,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'q5': q5,
        'q6': q6,
        'q7': q7,
        'q8': q8,
        'q9': q9,
        'q10': q10,
        'q11': q11,
        'Yesarr': Noarr,
        'Noarr': Yesarr,
        'Yesavg': normal2,
        'Noavg': other,
        # 'mainConclusion': mainConclusion
    }

    return render(request,'cognitive_result.html' , context)

@login_required(login_url='/')
def affectiveDomain(request):
    if(request.method == 'POST'):
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        ins = AffectiveDomain(q1=q1,q2=q2,q3=q3,q4=q4,q5=q5)
        ins.save()
        return redirect('affectiveDomain1')
    return render(request,'AffectiveDomain.html')

@login_required(login_url='/')
def affectiveDomain1(request):
    if(request.method == 'POST'):
        q6 = request.POST['q6']
        q7 = request.POST['q7']
        q8 = request.POST['q8']
        q9 = request.POST['q9']
        q10 = request.POST['q10']
        ins = AffectiveDomain1(q6=q6,q7=q7,q8=q8,q9=q9,q10=q10)
        ins.save()
        return redirect('affectiveDomain_result')
    return render(request,'AffectiveDomain1.html')

@login_required(login_url='/')
def affectiveDomain_result(request):
    mydata = UserDetail.objects.all().values()
    afd = AffectiveDomain.objects.all().values()
    afd1 = AffectiveDomain1.objects.all().values()

    name = mydata[len(mydata)-1].get('name')
    email = mydata[len(mydata)-1].get('email')
    childs_name = mydata[len(mydata)-1].get('childs_name')
    relationship = mydata[len(mydata)-1].get('relationship')
    childs_age = mydata[len(mydata)-1].get('childs_age')

    q1 = afd[len(afd)-1].get('q1')
    q2 = afd[len(afd)-1].get('q2')
    q3 = afd[len(afd)-1].get('q3')
    q4 = afd[len(afd)-1].get('q4')
    q5 = afd[len(afd)-1].get('q5')

    q6 = afd1[len(afd1)-1].get('q6')
    q7 = afd1[len(afd1)-1].get('q7')
    q8 = afd1[len(afd1)-1].get('q8')
    q9 = afd1[len(afd1)-1].get('q9')
    q10 = afd1[len(afd1)-1].get('q10')

    Yesarr = []
    Noarr = []
    if(q1 == 'Yes'):
        Yesarr.append('Social,respectful, high intellectual')
    else:
        Noarr.append('Arrogant')           
    if(q2 == 'Yes'):
        Yesarr.append('More social, thinks about hygiene,innovative')
    else:
        Noarr.append('Non innovative')    
    if(q3 == 'Yes'):
        Yesarr.append('Innovative, thoughtful, intelligent')
    else:
        Noarr.append('As usual')    
    if(q4 == 'Yes'):
        Yesarr.append('Thoughtful, intelligent and innovative')
    else:
        Noarr.append('Average')    
    if(q5 == 'Yes'):
        Yesarr.append('Intelligent, innovative and thoughtful')
    else:
        Noarr.append('Non innovative')
    if(q6 == 'Yes'):
        Yesarr.append('Un-usual mind set')
    else:
        Noarr.append('Innovative, rational, high intelligent,fight for justice')           
    if(q7 == 'Yes'):
        Yesarr.append('Realistic and innovative')
    else:
        Noarr.append('Average')    
    if(q8 == 'Yes'):
        Yesarr.append('Intelligent, more social')
    else:
        Noarr.append('Average')    
    if(q9 == 'Yes'):
        Yesarr.append('Realistic, thoughtful, more innovative')
    else:
        Noarr.append('Non innovative')    
    if(q10 == 'Yes'):
        Yesarr.append('Rational, innovative and intelligent')
    else:
        Noarr.append('Average')
    Mainarr = Yesarr + Noarr 
    str1 = " " 
    Mainstr = str1.join(Mainarr)
    MainStrUpper = Mainstr.upper()
    avg = MainStrUpper.count("AVERAGE")
    noninv = MainStrUpper.count("NON INNOVATIVE")
    negatives = avg+noninv
    inv = MainStrUpper.count("INNOVATIVE")
    intg = MainStrUpper.count("INTELLIGENT")
    reals = MainStrUpper.count("REALISTIC")
    positives = inv + intg + reals
    Yesavg = positives
    Noavg = negatives
    positivestr = "Maybe, Your child is very respectful , thoughtful and intelligent so inspire them for a better future and help them what he/she can do."
    negativestr = "Maybe, Your child is normal and he/she have as usual mindset , He/she needs to be more social and innovative"
    if(positives>negatives):
        mainConclusion = positivestr
    elif(negatives>positives):
        mainConclusion = negativestr
    context = {
        'name' : name , 
        'email' : email,
        'childs_name': childs_name,
        'relationship': relationship,
        'childs_age': childs_age,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'q5': q5,
        'q6': q6,
        'q7': q7,
        'q8': q8,
        'q9': q9,
        'q10': q10,
        'Yesarr': Yesarr,
        'Noarr': Noarr,
        'positives': positivestr,
        'negatives': negativestr,
        'Yesavg': Yesavg,
        'Noavg': Noavg,
        'mainConclusion': mainConclusion
    }

    return render(request,'AffectiveDomain_result.html' , context)