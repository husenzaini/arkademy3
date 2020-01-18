def biodata(name, age):
    y = {
        "name": name,
        "age": age,
        "address": "Jala RA Kartini",
        "hobbies": ["futsal", "ngoding"],
        "is_married": False,
        "list_school": [
            {"SD": "MI Fathimiyah", "year_in": "2002", "year_out": "2008"},
            {"SMP": "Mts Babul Futuh", "year_in": "2008", "year_out": "2011"},
            {"SMA": "SMA Assaadah", "year_in": "2011", "year_out": "2014"},
            {"Universitas": "UPN Veteran Jatim", "year_in": "2015", "year_out": "2020"}],
        "skills": [{'skill_name': "python", "level": "beginner"}],
        "interest_in_coding": True
    }
    return y


print(biodata('husen', 23))
