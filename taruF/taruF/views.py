from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# from cryptography.fernet import Fernet
# import base64
from django.conf import settings
import pickle
import os

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


def disease(request):
    sweating = request.POST['sweating']
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
    # d21 = request.POST['#movement_stiffness']
    psymptoms = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    #psymptoms = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20]
    disName = pred(psymptoms)
    return JsonResponse({"disname": disName})

def home(request):
    return render(request, 'home.html')
