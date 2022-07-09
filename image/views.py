from MySQLdb import IntegrityError
from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
from django.http import HttpResponse
import numpy as np
import joblib
import librosa
import librosa.display
import keras
from image.models import login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        try:
            user=login.objects.get(email=request.POST['email'], password=request.POST['password'])
            print("Username=",user)
            request.session['email']=user.email
            return render(request,"home.html")
        except login.DoesNotExist as e:
            messages.error(request,'Username or Password Invalid..!')
    return render(request,"index.html")

def failure(request):
    if request.method=="POST":
        loaded_rf = joblib.load("image/random_forest_model1.joblib")
        inp1=int(request.POST['inp1'])
        inp2=float(request.POST['inp2'])
        inp3=int(request.POST['inp3'])
        inp4=int(request.POST['inp4'])
        inp5=int(request.POST['inp5'])
        res=loaded_rf.predict([[inp1,inp2,inp3,inp4,inp5]])
        if(res[0]==0):
            return render(request,'result.html',{'death':'NO'})
        else:
            return render(request,'result.html',{'death':'YES..! Please consult the Doctor.'})
    else:
        return render(request,"failure_predict.html")

def find_anamoly(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            path='media'+'/'+str(obj.image)
            if path.endswith(".wav"):
                duration = librosa.get_duration(filename=path)
                slice_size = 3
                iterations = int((duration-slice_size)/(slice_size-1))
                iterations += 1
    #                 initial_offset = (duration % slice_size)/2
                initial_offset = (duration - ((iterations*(slice_size-1))+1))/2
                for i in range(iterations):
                            offset = initial_offset + i*(slice_size-1)
                y, sr = librosa.load(path, offset=offset, duration=3)
                S = librosa.feature.melspectrogram(y, sr=sr, n_fft=2048, 
                                    hop_length=512, 
                                    n_mels=128)
                mfccs = librosa.feature.mfcc(S=librosa.power_to_db(S), n_mfcc=40)
                x=[mfccs]
                x=np.asarray(x)
                x=x.reshape(1,40,130,1)
                json_file = open('image/big_model.json', 'r')
                loaded_model_json = json_file.read()
                json_file.close()
                loaded_model = keras.models.model_from_json(loaded_model_json)
                loaded_model.load_weights("image/big_data_model.h5")
                r=loaded_model.predict(x)
                r=np.argmax(r,axis=1)
                if(r==1):
                    return render(request,'result2.html',{'res':'NORMAL HEARTBEAT'})
                else:
                    return render(request,'result2.html',{'res':'ABNORMAL HEARTBEAT..! \n Please consult the Doctor.'})
            else:
                messages.error(request,"ERROR: Only audio files with '.wav' formats are acceptable ..!")
                return render(request,'find_anamoly.html',{'form':form})
    else:
        form=ImageForm()   
    return render(request,'find_anamoly.html',{'form':form})

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        place=request.POST.get('place')
        password=request.POST.get('password')
        exist=login.objects.filter(email=email) .exists()
        if exist:
            messages.error(request,"Email is already registered..! Try again")
            return redirect('/register')
        else:
            login(name=name,email=email,age=age,place=place,password=password).save()
            messages.success(request,'The new User '+request.POST['name']+" Is saved Successfully..!")
            return render(request,'register.html')
    else:
        return render(request,'register.html')
def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,"home.html")

def home(request):
    return render(request,"home.html")