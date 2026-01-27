student_data = {"1st Student":
                {"Name":"Inaya",
                 "Class":"7th",
                 "Favourite_subjects":["maths","English","Science"]}}
{"2nd Student":
                {"Name":"Alice",
                 "Class":"4th",
                 "Favourite_subjects":["English","Science"]}}
{"3rd Student":
                {"Name":"Zara",
                 "Class":"11th",
                 "Favourite_subjects":["maths","English","History"]}}
{"4th Student":
                {"Name":"Adam",
                 "Class":"8th",
                 "Favourite_subjects":["maths","Hindi","History"]}}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
        print(result)