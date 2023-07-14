import os
import shutil

def extract_all(main_directory,output_directory):
    print("Scraping...")
    if not os.path.exists("Images"):
        os.walk(output_directory)
        os.makedirs("Images")

    if not os.path.exists("Sounds"):
        os.walk(output_directory)
        os.makedirs("Sounds")

    if not os.path.exists("Other"):
        os.walk(output_directory)
        os.makedirs("Other")

    if not os.path.exists("Archives"):
        os.walk(output_directory)
        os.makedirs("Archives")




    # Rectify different image formats to a tuple (why do so many exist bruh)

    # Iterate through the files in the song directory
    for root, _, files in os.walk(main_directory):
        for file in files:
            if file.lower().endswith((".png" or ".jpeg" or ".jpg" or ".bmp" or ".webm")):
                # Create the full path for the image file
                image_path = os.path.join(root, file);
                
                # Copy the image file to the output directory
                shutil.move(image_path, 'Images');
            else:
                if file.lower().endswith((".mp3" or ".wav")):

                    sound_path = os.path.join(root, file);
                
                    shutil.move(sound_path, 'Sounds');
                else:
                    if file.lower().endswith((".rar" or ".zip" or ".tar" or ".gz" or ".7zip")):
                        archive_path = os.path.join(root, file);
                        shutil.move(archive_path, 'Archives');
                    else:
                        other_path = os.path.join(root, file);
                        shutil.move(other_path, 'Other');

    print("Scraping complete!");

def take_input():
    print("\x1B[2J\x1B[1;1H");
    print("#-----------------------------------------------------------#");
    print("|                  Automatic file Sorter                    |");
    print("#-----------------------------------------------------------#");

    main_directory = input("Enter input directory!: ");

    output_directory = os.getcwd();
    extract_all(main_directory,output_directory);
    if input("Exit? (y/n): ") != "y":
        take_input();

take_input();
