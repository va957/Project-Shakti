from multiprocessing import context
from pydoc import Doc
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate ,logout
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pickle
import os
# relative import of forms
from .models import *

# pass id attribute from urls


def logoutUser(request):
    logout(request)
    return redirect('home')

def rmp(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = RMP.objects.get(id = id)



    return render(request, "RMP.html", context)

def patient(request,id):
    context ={}

    # add the dictionary during initialization
    context["data"] = Patient.objects.get(id = id)

    return render(request, "Patient.html", context)

def doctor(request,id):
    context={}
    context["data"] = Doctor.objects.get(id = id)

    return render(request, "Doctor.html", context)

def pres(request,id):
    context={}
    context["data"] = Prescription.objects.get(id = id)

    return render(request, "Patient.html", context)

def slot(request,id):
    context={}
    context["data"] = Slots.objects.get(id = id)

    return render(request, "Doctor.html", context)

def medic(request,id):
    context={}
    context["data"] = Slots.objects.get(id = id)

    return render(request, "Doctor.html", context)

def appiont(request,id):
    context={}
    context["data"] = Appointments.objects.get(id = id)
    return render(request, "patient.html", context)


def patientDashBoardDetails(request):
    context = {}
    context["data"] = Patient.objects.filter(id=id)
    context["presc"] = Prescription.objects.filter(id=id)
    context["Appointments"] = Appointments.objects.filter(id=id)
    context["Vitals"] = Vitals.objects.filter(id=id)
    context["Med"] = medicines.objects.filter()
    return render(request, "",context)

def patientPrescription(request):
    context = {}
    context["data"] = Prescription.objects.filter(id=id)
    return render(request, "",context)

def patientAppointment(request):
    context = {}
    context["Patient"] = Patient.objects.raw("SELECT * FROM base_patient WHERE id = %s", [id])[0]
    context["vitals"] = Vitals.objects.filter(id=id)[0]
    context["appointments"] = Appointments.objects.filter(id=id)
    x= Prescription.objects.filter(id=id)
    y = []
    z = []
    for id in x:
        y.append(id.patient_id)
    for id in y :
        z.append(medicines.objects.filter(id=id))
    context["medicines"] = z
    print(context["appointments"])
    # context["vitals"] = Vitals.objects.raw("SELECT * FROM base_vitals WHERE id = %s", [id])[0]
    # context["appointments"] = Appointments.objects.raw("SELECT * FROM base_appointments WHERE id = %s AND ", [id])
    return render(request, "patients-details.html",context)

def doctor_dashBoard(request):
    did= 1

    context={}
    context["doctor"] = Doctor.objects.filter(id=did)[0]
    context["Patient"] = Patient.objects.all()
    a = Slots.objects.filter(doctor_id=did)
    b = []
    for id in a:
        b.append(id.doctor_id)
    context["Appointments"] = Appointments.objects.filter(id__in=b)
    print(context["doctor"])
    return render(request, "doc.html",context)

def rmp_dashbaord(request):
    rmid = 1
    pid = 1
    context = {}
    context["doctors"] = Doctor.objects.all()
    context["patient-all"] = Patient.objects.all()
    context["appointments"] = Appointments.objects.filter(id=pid)
    x= Prescription.objects.filter(id=id)
    y = []
    z = []
    for id in x:
        y.append(id.patient_id)
    for id in y :
        z.append(medicines.objects.filter(id=id))
    context["medicines"] = z
    a = Slots.objects.all()
    b = []
    for id in a:
        b.append(id.doctor_id)
    context["Doctor"] = Doctor.objects.filter(id__in=b)
    context["Slots"] = Slots.objects.all()
    context["rmd"]= RMP.objects.filter(id=rmid)

    return render(request, "rmp.html",context)

def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")

def login(request):
    return render(request, "login.html")
    context["data"] = Appointments.objects.filter(id=id)
    return render(request, "",context)

def patientVitals(request):
    context = {}
    context["data"] = Vitals.objects.filter(id=id)
    return render(request, "",context)




symptomslist = ['sweating', 'breathlessness', 'continuous_feel_of_urine', 'bladder_discomfort', 'burning_micturition', 'foul_smell_of urine', 'vomiting', 'constipation',
                'toxic_look_(typhos)', 'belly_pain', 'skin_rash', 'continuous_sneezing', 'pus_filled_pimples', 'blackheads', 'scurring', 'shivering', 'watering_from_eyes', 'red_spots_over_body', 'swelling_joints', 'painful_walking', 'movement_stiffness']
diseaselist = ['Fungal infection', 'Allergy', 'Acne', 'Arthritis', 'Hyperthyroidism', 'Hypothyroidism', 'Pneumonia', 'Common Cold',
               'Tuberculosis',
               'Typhoid',
               'Dengue',
               'Chicken pox',
               'Malaria',
               'Jaundice',
               'Migraine',
               'Gastroenteritis',
               'Diabetes',
               'Urinary tract infection']

print(os.getcwd())
with open('token.pickle', 'rb') as efile:
    clf = pickle.load(efile)


def pred(psymptoms):
    testingsymptoms = []
    # append zero in all coloumn fields...
    for x in range(0, len(symptomslist)):
        testingsymptoms.append(0)

    # update 1 where symptoms gets matched...
    for k in range(0, len(symptomslist)):
        for z in psymptoms:
            if (z == symptomslist[k]):
                testingsymptoms[k] = 1

    inputtest = [testingsymptoms]

    print(inputtest)

    predicted = clf.predict(inputtest)
#   print("predicted disease is : ")
#   print(predicted)
    y_pred_2 = clf.predict_proba(inputtest)
    confidencescore = y_pred_2.max() * 100
#   print(" confidence score of : = {0} ".format(confidencescore))

    confidencescore = format(confidencescore, '.0f')
    predicted_disease = predicted[0]

    print(predicted_disease)
    return predicted_disease

@csrf_exempt
def disease(request):

    d1 = int(request.POST['sweating'])
    # d2 = request.POST.get['#breathlessness']
    # d3 = request.POST.get['#continuous_feel_of_urine']
    # d4 = request.POST.get['#bladder_discomfort']
    # d5 = request.POST.get['#burning_micturition']
    # d6 = request.POST.get['#foul_smell_of urine']
    # d7 = request.POST.get['#vomiting']
    # d8 = request.POST.get['#constipation']
    # d9 = request.POST['#toxic_look_(typhos)']
    # d10 = request.POST['#belly_pain']
    # d11 = request.POST['#skin_rash']
    # d12 = request.POST['#continuous_sneezing']
    # d13 = request.POST['#pus_filled_pimples']
    # d14 = request.POST['#blackheads']
    # d15 = request.POST['#scurring']
    # d16 = request.POST['#shivering']
    # d17 = request.POST['#watering_from_eyes']
    # d18 = request.POST['#red_spots_over_body']
    # d19 = request.POST['#swelling_joints']
    # d20 = request.POST['#painful_walking']
    # d21 = request.POST['#movement_stiffness']
    psymptoms = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # psymptoms = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]
    disName = pred(psymptoms)
    return JsonResponse({"disname": disName})






