import sys
import cv2
import pytesseract
from tkinter import Tk, filedialog, Button, Label
from PIL import Image
from tkinter import messagebox
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

def upload_image_and_extract_text():
    file_path = filedialog.askopenfilename(
        title="Select an image", 
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    
    if not file_path:
        return 
    
    status_label.config(text="Processing the image...")

    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    custom_config = r'--oem 3 --psm 6'
    try:
        text = pytesseract.image_to_string(gray, config=custom_config, lang='ben+eng')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"extracted_text_{timestamp}.txt"

        with open(output_filename, "w", encoding="utf-8") as text_file:
            text_file.write(text)

        messagebox.showinfo("Success", f"Text has been successfully extracted and saved to '{output_filename}'")
        status_label.config(text="Text extraction complete!")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="Error during text extraction.")

root = Tk()
root.title("Image to Text Converter")

upload_button = Button(root, text="Upload Image", command=upload_image_and_extract_text)
upload_button.pack(pady=20)

status_label = Label(root, text="Please upload an image.")
status_label.pack(pady=10)

root.geometry("300x150")
root.mainloop()
