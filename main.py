import tkinter as tk
import webbrowser
import arabic_reshaper

def reshape(text):
    return arabic_reshaper.reshape(text)[::-1]  # فقط عكس النص لتقريب شكل العربية

def open_android_tracker():
    webbrowser.open("https://www.google.com/android/find")

def open_apple_tracker():
    webbrowser.open("https://www.icloud.com/find")

root = tk.Tk()
root.title("تتبع الهاتف")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text=reshape("اختر نوع جهازك لتتبع الهاتف"), font=("Arial", 14, "bold"), bg="#f0f0f0")
label.pack(pady=20)

android_button = tk.Button(root, text=reshape("هاتف أندرويد"), command=open_android_tracker, width=25, height=2, bg="#4CAF50", fg="white", font=("Arial", 12))
android_button.pack(pady=10)

apple_button = tk.Button(root, text=reshape("هاتف آيفون"), command=open_apple_tracker, width=25, height=2, bg="#2196F3", fg="white", font=("Arial", 12))
apple_button.pack(pady=10)

footer = tk.Label(root, text=reshape("هذه الخدمة تعتمد على مواقع Google و Apple الرسمية"), font=("Arial", 9), bg="#f0f0f0", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
