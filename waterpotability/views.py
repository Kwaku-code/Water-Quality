# from WaterQuality.waterpotability.models import Potability
# from WaterQuality.waterpotability.models import Potability
from django.shortcuts import redirect, render
from django.db.models import Sum, F
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


from.models import Variables
# from .forms import SignUpCreateForm, LoginCreateForm, EnterVariablesForm, ResultsForm 

import pickle
# our home page view


def home(request):
    context = {"prediction": ""}
    if request.method == "POST":
        ph = float(request.POST['ph'])
        Hardness = float(request.POST['Hardness'])
        Solids = float(request.POST['Solids'])
        Chloramines = float(request.POST['Chloramines'])
        Sulfate = float(request.POST['Sulfate'])
        Conductivity = float(request.POST['Conductivity'])
        Organic_carbon = float(request.POST['Organic_carbon'])
        Trihalomethanes = float(request.POST['Trihalomethanes'])
        Turbidity = float(request.POST['Turbidity'])
        input_var = [ph, Hardness,Solids, Chloramines, Sulfate, 
        Conductivity, Organic_carbon, Trihalomethanes, Turbidity]
        result = getPredictions(input_var)
        context = {"prediction": result}

        saved = Variables(
            ph = ph,
            Hardness = Hardness,
            Solids = Solids,
            Chloramines = Chloramines,
            Sulfate = Sulfate,
            Conductivity = Conductivity,
            Organic_carbon = Organic_carbon,
            Trihalomethanes = Trihalomethanes,
            Turbidity = Turbidity,
            Potability=result
            )
        saved.save()

    return render(request, 'waterpotability/index.html', context)



# custom method for generating predictions
def getPredictions(input_var):
    print("Model Loaded Successfully")
    model = pickle.load(open("waterpotability/waterpotability.sav", "rb"))
    scaled = pickle.load(open("waterpotability/scaler.sav", "rb"))
    scaled_input_var = scaled.transform([input_var])
    print(scaled_input_var)
    print("Model Loaded Successfully 1")
    prediction = model.predict(scaled_input_var)

    if prediction == 0:
        return "not potable"
    elif prediction == 1:
        return "potable"
    else:
        return "error"


# our result page view
def result(request):
    
    return render(request, 'result.html', {'result': result})



def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
    # Add your code below:
    user = authenticate(request, username=username, password=password)
    if user is not None:
        results = Variables.objects.all()
        return render(request, "waterpotability/database.html", {'results': results})
    else:
      return HttpResponse("invalid credentials")
  return render(request, "registration/login.html", context)


class Database(LoginRequiredMixin, ListView):
    model = Variables
    template_name = "waterpotability/database.html"

# def SignUp(request):
#   context = {
#       "SignUp": "active"
#   }
#   if request.method == "POST":
#      username = request.POST["username"]
#      password = request.POST["password"]
#      if user is not None:
#       return redirect("home")
#     else:
#       return HttpResponse("invalid credentials")
#   return render(request, "registration/signup.html", context)
  


# class PotabilityView(ListView):
#     model = Potability
#     template_name = waterpotability/database.html
  
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
   
  

# class Login(CreateView):
#     model = Login
#     success_url = reverse_lazy('result')
#     template_name = "registration/login.html"
#     form_class = LoginCreateForm


# class EnterVariablesView(CreateView):
#     model = EnterVariables
#     success_url = reverse_lazy('result.html')
#     template_name = "waterpotability/index.html"
#     form_class = EnterVariablesForm

# class ResultsView(CreateView):
#     model = Potability
#     success_url = reverse_lazy('index.html')
#     template_name = "waterpotability/result.html"
#     form_class = ResultsForm
 
def log_out(request):
    logout(request)
    return redirect("home")


