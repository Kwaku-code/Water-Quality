from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView


from.models import Variables
import pickle



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


def login_view(request):
  context = {
    "login_view": "active"
  }
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]
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


  
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

 
def log_out(request):
    logout(request)
    return redirect("home")