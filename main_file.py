import os
import shutil
from cmp_img import CompareImg
from pathlib import Path
from send_email import SendEmail
import time

def move_image(src_path,dest_path,file_name):
    source_path = os.path.join(src_path,file_name)
    destanation_path = os.path.join(dest_path,file_name)
    shutil.copy(source_path,destanation_path)

def zip_folder(folder_path,zip_path):
    shutil.make_archive(zip_path,'zip',folder_path)

def create_folder(folder_name):
    os.makedirs(os.path.join('', folder_name), exist_ok=True)

def main_process():
    folder_path = "img" # all image location
    sample_img = "messi1.jpg" # using this img compare all images


    count = 0
    match_flag = False


    # Create a Path object for the folder
    folder = Path(folder_path)

    # Iterate through the files in the folder
    for file_path in folder.iterdir():
        if file_path.is_file():
            cmp_face = CompareImg(sample_img,str(file_path))
            if cmp_face.cmp_img():
                src_location = str(file_path).split('\\')[0]
                des_location = "extract_img"
                create_folder(des_location)
                file_name = str(file_path).split('\\')[1]
                move_image(src_location,des_location,file_name)
                count += 1
                match_flag = True
                print("Match")
            else:
                print("No Match")

    print(f"Total Matches Image : {count}")
    return match_flag



def main():  # start point
    flag = main_process()

    # zip process
    zip_folder_path = "extract_img"
    zip_output_path = "output"

    # email user info
    sender_email = ''
    receiver_email = ''
    subject = 'Using Photofi App sending you all of your image'
    body = 'Like you, your photos are beautiful'
    attachment_path = 'output.zip' # file name
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    smtp_username = ''
    smtp_password = ''

    if(flag):
        zip_folder(zip_folder_path,zip_output_path)
        print("Zip Done")
        time.sleep(2)
        # Ready
        email = SendEmail(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, smtp_username, smtp_password)
        email.send_email()
        print("Email sent successfully")

    else:
        print("Folder Empty")
    

# Action
if __name__ == "__main__":
    main()