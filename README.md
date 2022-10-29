# CS_361_Brian_Haug

# The function text_doc_function(pin_number, data_dictionary) writes the provided dictionary to a text file named after the provided pin number.

# The function read_function(pin) reads the contents of text file with the name of the provided pin number.

# Both functions are in seperate .py files and not imported or linked in any way.

# ------------------------------------------------------------------------------------------------------------

# To REQUEST data: call function text_doc_function(pin_number, data_dictionary) in microservice_function.py

# Example:

# workout_dict =
# {
#    "day": "Tuesday",
#    "group": "legs",
#    "duration": "30"
# }
# pin = 88654

# text_doc_function(pin, workout_dict )

# ------------------------------------------------------------------------------------------------------------

# To RECEIVE data: call function read_function(pin) in microservice_reader.py

# Example:

# read_function(88654)

# Returns:
# {
#    "day": "Tuesday",
#    "group": "legs",
#    "duration": "30“
# }





