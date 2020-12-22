import csv

with open("insurance.csv") as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)
    age_list = []
    sex_list = []
    bmi_list = []
    children_list = []
    smoker_list = []
    region_list = []
    charges_list = []
    for row in insurance_dict:
        age_list.append(row['age'])
        sex_list.append(row['sex'])
        bmi_list.append(row['bmi'])
        children_list.append(row['children'])
        smoker_list.append(row['smoker'])
        region_list.append(row['region'])
        charges_list.append(row['charges'])

patient_list = []
for x in range(1, len(age_list)):
    patient_list.append("Patient {}".format(x))

records_list = []
for i in range(0, len(patient_list)):
    current_patient = []
    current_patient.append(int(age_list[i]))
    current_patient.append(sex_list[i])
    current_patient.append(float(bmi_list[i]))
    current_patient.append(int(children_list[i]))
    current_patient.append(smoker_list[i])
    current_patient.append(region_list[i])
    current_patient.append(float(charges_list[i]))
    records_list.append(current_patient)

keys_for_records = [
    "Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges"
    ]

records_as_dict = []
for record in records_list:
    records_as_dict.append(dict(zip(keys_for_records, record)))

master_records = dict(zip(patient_list, records_as_dict))

print(master_records["Patient 3"]["BMI"])
