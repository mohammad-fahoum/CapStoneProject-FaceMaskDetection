from managedb import SimpleDB
from datetime import datetime
local = SimpleDB("localdb.db")

predictions = {
     'predict_id' : 'INTEGER PRIMARY KEY AUTOINCREMENT',
     'image_name' : 'VARCHAR(100)',
     'status' : 'VARCHAR(100)',
     'upload_time' : 'VARCHAR(100)'
}
try :
    local.add_table("predictions", **predictions)
except:
    pass
def transfer_data_to_local(image_name, status):
    local.add_record("predictions", image_name = f'"{image_name}"', status =f'"{status}"', upload_time = f'"{datetime.now().strftime("%d-%m-%y %H:%M:%S")}"')

# apartment = {
#     'apt_ID' : 'INT PRIMARY KEY NOT NULL',
#     'faculty_id' : 'INT NOT NULL',
#     'apt_name' : 'VARCHAR(100)',
#     'adminstrator' : 'VARCHAR(100)',
#     'FOREIGN KEY (faculty)' : 'REFERENCES faculty(faculty_ID)'
# }

# data1 = {
#     'faculty_id' : '1',
#     'faculty_name' : "'institute of earth and enviromental science'",
#     'adminstrator' : "'ali nouh'",
#     'openning_date' : "'2014-12-01'"
# }
# data2 = {
#     'apt_ID' : '1',
#     'faculty_id' : '1',
#     'apt_name' : "'geographic information system and remote sensing'",
#     'adminstrator' : "'mohammad fahoum'",
# }
# joins = {
#     "faculty" : "faculty_id",
#     "apartment" : "faculty_id"
# }

# new_table("apartment", **apartment)
# insert_record("faculty", **data1)
# insert_record("apartment", **data2)
# single_query("faculty")
# single_query("apartment")
# multitable_query(faculty = "fauculty_id", apartment = "faculty_id")
# # multitable_query(**joins)
# update_record("faculty", "faculty_id = 1", adminstrator = "'yazan'")
# update_table("apartment", apt_name = "'cypersecurity'", adminstrator = "'mahmoud hammad'")
# insert_record("faculty", faculty_id = "2")
# insert_record("faculty", faculty_id = "3", faculty_name = "'Prince Alhussien Bin Abdullah for Information Technology'")
# del_row("faculty", "faulty_id = 2")
# del_column("apartment", "apt_name")
# del_table("apartment")