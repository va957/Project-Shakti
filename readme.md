<h1 align="center">Project Shakti 
  <img src="https://logos.textgiraffe.com/logos/logo-name/Shakti-designstyle-cartoon-m.png" alt="Logo" width="25" height="25">
</h1>
<p align="center"> 
 <a target="_blank" href="https://youtu.be/GvtHHi_M_Qs">Video Demo</a>
</p>

<!-- ABOUT THE PROJECT -->

## Brief About The Project
* Project Shakti is a developed as part of Code for Good' 2022 organised by JP Morgan Chase for Taru Foundation to provide remote health facilities to the underpriveleged sections of society.
* It is a Django based Web Application using Agora for video conferencing
* It is a telimedicine platform providing facilities of digital prescriptions,online consultations, Vitals Checkup and support offered by Rural Medical Practitioner to connect the patients and doctors.

### Salient Features
* Home page directs to sign up and sigin page where patient, RMP or doctor can register based on their Adhaar Card.
* Once a patient logins he/she can view profile details,prescription history,essential vitals and Appointment status(which will give an option to join the meeting according to time slot)
* RMPs and Doctors can view patient's info,history and details.
* RMPs can fill vitals, symtoms and patient details on their dashboard on behalf of the patient and contact doctors.
*Doctors can choose free time slots in their calendar according to which appointments will be allocated.
*The symptoms filled by RMPS can be studied and sorted into corresponding disease classification using a ML model according to which  specialised doctor can be contacted   



### Techstacks and Algorithms

* Frontend- Html,CSS,Javscript
* Backend-Django
* Database-DBSQLite
* Machine Learning Model- Disease Predictor based on symptoms using algorithms(Naive Bayes, Random Forest, Xgboost)

<!-- INSTALLATIONS -->

## Setup and Getting Started

To install and run the project on your local system, following are the requirements:

<<<<<<< HEAD
=======
### Installation

- Clone the Project and go to the project folder to run the following command to install all dependencies
>>>>>>> a1c6e1ffb525de07588b6e424721b91117015b72

- Run

```
git clone https://github.com/cfgmum22/team-48
```

### Running the Applications

- Open the terminal and run the command

<<<<<<< HEAD
* Clone the Project and go to the project folder to run the following command to install all dependencies

* Run
```
git clone https://github.com/cfgmum22/team-48
```

## Navigating Through The App
=======
```
python manage.py runserver
```

- You can access the django admin page at http://127.0.0.1:8000/admin

- Also a new admin user can be created using

```
python manage.py createsuperuser
```

- To migrate the data run the following on the command prompt

```
python manage.py makemigrations
python manage.py migrate
```


