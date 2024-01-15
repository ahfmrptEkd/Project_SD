# python post_train.py input_image_path user_id url_id 

import os

# ex) python post_train.py /home/ds/api/input_img user http://127.0.0.1:7869

file = "post_train.py"
user_img = "/home/ds/api/input_img"
user_id = ""
url = "http://127.0.0.1:7869"
terminnal_command = f"python {file} {user_img} {user_id} {url}" 
os.system(terminnal_command)