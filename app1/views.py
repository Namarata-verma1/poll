from asyncore import poll
from multiprocessing import context
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Customer_Class,Poll,Author_Class

from .forms import CreatePollForm
from .models import Poll


# Create your views here.

def login(request):
    if request.POST:
        em = request.POST['Email']
        ps = request.POST['Password']
        
        try:
            data = Customer_Class.objects.get(cust_email=em)
            if data.cust_password == ps:
                request.session['author'] = data.cust_email
                return redirect('index')
            else:
                messages.warning(request, 'Password is Wrong ...')
                messages.warning(request, 'Try Something Else ...')
        except:
            messages.warning(request, 'Email Is Not Registered ...')
        
    return render(request,'login.html')

def reg(request):
    if request.POST:
        unm = request.POST['Username']
        em = request.POST['email']
        no = request.POST['no']
        ps1 = request.POST['password_1']
        ps2 = request.POST['password_2']
        
        try:
            val = Customer_Class.objects.get(cust_email=em)
            messages.warning(request, 'Email Id Already Exists ...')
        except: 
            if ps1 == ps2:
                obj = Customer_Class()
                obj.cust_name = unm
                obj.cust_email = em
                obj.cust_m_no = no
                obj.cust_password = ps1
                obj.save()               
                return redirect('login')
            else:
                messages.warning(request, 'Password Not Same ...')
    return render(request,'reg.html')

def index(request):
    if "author" in request.session.keys():
        em = request.session['author']
        context = Author_Class.objects.get(p_email=em)
        polls = Poll.objects.all()
        context = {
            'polls' : polls
        }
        return render(request, 'index.html', context,)
    else:
        return redirect('login')

def create(request):
    if "author" in request.session.keys():
        if request.method == 'POST':
            form = CreatePollForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = CreatePollForm()
        context = {
            'form' : form
        }
        return render(request, 'create.html', context)

    else:
         return redirect('login')


def vote(request, poll_id):
    if "author" in request.session.keys():
        poll = Poll.objects.get(pk=poll_id)

        if request.method == 'POST':

            selected_option = request.POST['poll']
            if selected_option == 'option1':
                poll.option_one_count += 1
            elif selected_option == 'option2':
                poll.option_two_count += 1
            elif selected_option == 'option3':
                poll.option_three_count += 1
            else:
                return HttpResponse(400, 'Invalid form')

            poll.save()

            return redirect('results', poll.id)

        context = {
            'poll' : poll
        }
        return render(request, 'vote.html', context)
    else:
        return redirect('login')

def results(request, poll_id):
    if "author" in request.session.keys():
        poll = Poll.objects.get(pk=poll_id)
        context = {
            'poll' : poll
        }
        return render(request, 'results.html', context)
    else:
        return redirect('login')
   
def Delete(request ,id):
    if "author" in request.session.keys():
        prod=Poll.objects.get(id=id)
        prod.delete()
        return redirect('index')
    else:
        return redirect('login')

def Profile(request):
    if "author" in request.session.keys():
        
        return render(request,'profile.html')
    else:
        return redirect('login') 

def logout(request):
    if "author" in request.session.keys():
        del request.session['author']
        return redirect('index')
    else:
        return redirect('login')
#-------------------------------------------------------------------------------------------
def plogout(request):
    if "poller" in request.session.keys():
        del request.session['poller']
        return redirect('login')
    else:
        return redirect('plogin')

def plogin(request):
    if request.POST:
        em = request.POST['Email']
        ps = request.POST['Password']
        print(em,ps)
        try:
            data = Author_Class.objects.get(p_email=em)
            if data.p_password == ps:
                request.session['poller'] = data.p_email
                return redirect('pindex')
            else:
                messages.warning(request, 'Password is Wrong ...')
                messages.warning(request, 'Try Something Else ...')
        except:
            messages.warning(request, 'Email Is Not Registered ...')
        
    return render(request,'plogin.html')
    
    
def preg(request):
        if request.POST:
            unm = request.POST['Username']
            em = request.POST['email']
            no = request.POST['no']
            ps1 = request.POST['password_1']
            ps2 = request.POST['password_2']
            try:
                val = Author_Class.objects.get(p_email=em)
                messages.warning(request, 'Email Id Already Exists ...')
            except: 
                if ps1 == ps2:
                    obj = Author_Class()
                    obj.p_name = unm
                    obj.p_email = em
                    obj.p_m_no = no
                    obj.p_password = ps1
                    obj.save()               
                    return redirect('plogin')
                else:
                    messages.warning(request, 'Password Not Same ...')
        return render(request,'preg.html')



def pindex(request):
    if "poller" in request.session.keys():
        em = request.session['User']
        cust_user= Customer_Class.objects.get(cust_email=em)
        obj = Poll.objects.all()
        return render(request,"pindex.html",{'data':obj,'customer':cust_user})
    else:
        return redirect('plogin')
   