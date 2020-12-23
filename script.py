import csv
import matplotlib.pyplot as plt

with open("insurance.csv") as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)
    # lists for each column
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

# naming each row as a "Patient #"
patient_list = []
for x in range(1, len(age_list)):
    patient_list.append("Patient {}".format(x))

# each value in each column as a list
# changing to types that suit best
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

# going to change records_list to a dictionary with keys
# for easier access into values, created keys based on column names
keys_for_records = [
    "Age", "Sex", "BMI", "Children", "Smoker", "Region", "Charges"
    ]

# using for loop, made a list of dictionaries that used records_list and
# keys_records
records_as_dict = []
for record in records_list:
    records_as_dict.append(dict(zip(keys_for_records, record)))

# this master dictionary zips together the patient list with generic names
# and the records_as_dict, as if we did have names so everything is
# easily accessible.
master_records = dict(zip(patient_list, records_as_dict))

# function to calculate average BY LOCATION of values that use int or float
# can be used to calculate average of age, BMI, children, charges
# returns a dictionary
def average_by_location(master_records, column_to_inspect):
    sw_total, se_total, nw_total, ne_total = 0, 0, 0, 0
    sw_num, se_num, nw_num, ne_num = 0, 0, 0, 0
    for record in master_records.values():
        if record["Region"] == "southwest":
            sw_total += record[column_to_inspect]
            sw_num += 1
        elif record["Region"] == "southeast":
            se_total += record[column_to_inspect]
            se_num += 1
        elif record["Region"] == "northwest":
            nw_total += record[column_to_inspect]
            nw_num += 1
        elif record["Region"] == "northeast":
            ne_total += record[column_to_inspect]
            ne_num += 1
    sw_average = sw_total / sw_num
    se_average = se_total / se_num
    nw_average = nw_total / nw_num
    ne_average = ne_total / ne_num
    average_dict = {
        "Northeast " + column_to_inspect + " Average": round(ne_average, 2),
        "Southeast " + column_to_inspect + " Average": round(se_average, 2),
        "Southwest " + column_to_inspect + " Average": round(sw_average, 2),
        "Northwest " + column_to_inspect + " Average": round(nw_average, 2)
    }
    return average_dict


# testing out the function, it works!
# function rounds to two decimal places
reg_avg_charges = average_by_location(master_records, "Charges")
reg_avg_age = average_by_location(master_records, "Age")
reg_avg_bmi = average_by_location(master_records, "BMI")
reg_avg_child = average_by_location(master_records, "Children")
print(reg_avg_charges)
print(reg_avg_age)
print(reg_avg_bmi)
print(reg_avg_child)

def smoker_probability(master_records):
    sw_total, se_total, nw_total, ne_total = 0, 0, 0, 0
    sw_num, se_num, nw_num, ne_num = 0, 0, 0, 0
    for record in master_records.values():
        if record["Region"] == "southwest":
            if record["Smoker"] == "yes":
                sw_total += 1
                sw_num += 1
            else:
                sw_num += 1
        elif record["Region"] == "southeast":
            if record["Smoker"] == "yes":
                se_total += 1
                se_num += 1
            else:
                se_num += 1
        elif record["Region"] == "northwest":
            if record["Smoker"] == "yes":
                nw_total += 1
                nw_num += 1
            else:
                nw_num += 1
        elif record["Region"] == "northeast":
            if record["Smoker"] == "yes":
                ne_total += 1
                ne_num += 1
            else:
                ne_num += 1
    sw_y_smoker_prob = sw_total / sw_num
    se_y_smoker_prob = se_total / se_num
    nw_y_smoker_prob = nw_total / nw_num
    ne_y_smoker_prob = ne_total / ne_num
    average_dict = {
        "Northeast Smoker Probability": round(sw_y_smoker_prob, 2),
        "Southeast Smoker Probability": round(se_y_smoker_prob, 2),
        "Southwest Smoker Probability": round(nw_y_smoker_prob, 2),
        "Northwest Smoker Probability": round(ne_y_smoker_prob, 2)
    }
    return average_dict

# calculating the probability of being a smoker in decimal
smoker_prob = smoker_probability(master_records)

# bar chart to compare BMI levels across regions
diff_colors = ['green','blue','purple','brown']
plt.bar(
    ["Northeast", "Southeast", "Southwest", "Northwest"],
    reg_avg_bmi.values(),
    color=diff_colors
)
plt.title('Average BMI by Region', fontsize = 16)
plt.xlabel('Region')
plt.ylabel('BMI')
plt.show()
# Southeast Region leads the way in BMI levels

# bar chart to compare Smoking Probability levels across regions
diff_colors = ['green','blue','purple','brown']
plt.bar(
    ["Northeast", "Southeast", "Southwest", "Northwest"],
    smoker_prob.values(),
    color=diff_colors
)
plt.title('Smoker Probability by Region', fontsize = 16)
plt.xlabel('Region')
plt.ylabel('Smoker Probablity')
plt.show()
# Southeast Region leads the way in BMI levels

# bar chart to compare insurance costs by region
plt.bar(
    ["Northeast", "Southeast", "Southwest", "Northwest"],
    reg_avg_charges.values(),
    color=diff_colors
)
plt.title('Average Insurance Costs by Region', fontsize = 16)
plt.xlabel('Region')
plt.ylabel('Yearly Insurance Costs')
plt.show()

# Southeat Region yearly insurance costs lead the way, predicatably
# it's interesting that I have a few variables here that would directly
# influence insurance costs. Ages, Children, BMI, Smoker Status, etc.
# I chose to break everything down by region to highlight differences
# between different parts of the states and where people might pay the most.
# Ages and Children were basically flat anywhere you lived. So inconsequential.
# BMI and Smoker status gave a noticable edge to one region (Southeast).
# Southeast on average has higher BMI's and higher probability of smokers.
# Predictably, insurance costs were highest in the southeast.
# It's a chicken/egg conclusion though, with more data to dive into I could
# come to more conclusions. But are insurance costs high because of the
# lifestyles in the Southeast? Or are lifestyles the way they are because
# health insurance costs are so high? What could fix this?
# It's almost like high insurance costs are a hinderance to "getting healthier."
# So what will give or what can change to help change lifestyles for the better?
