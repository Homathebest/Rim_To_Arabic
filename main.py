import tkinter as tk

def roman_to_arabic(numeral):
    roman_to_arabic_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    valid_numeral = "IVXLCDM"
    for i in numeral:
        if i not in valid_numeral:
            root = tk.Tk()
            output_label = tk.Label(root, text="Invalid Roman numeral: " + i)
            output_label.pack()
            root.mainloop()
    if "IIII" in numeral or "XXXX" in numeral or "CCCC" in numeral or "MMMM" in numeral or "VV" in numeral or "LL" in numeral or "DD" in numeral or "DM" in numeral or "LC" in numeral or "VX" in numeral or "CDC" in numeral or "XLX" in numeral or "IVI" in numeral or "IIV" in numeral or "IIX" in numeral or "IIL" in numeral or "IIC" in numeral or "IID" in numeral or "IIM" in numeral or "XXL" in numeral or "CCD" in numeral or "IXL" in numeral or "IVL" in numeral or "DCM" in numeral or "IXI" in numeral or "ILI" in numeral or "ICI" in numeral or "IDI" in numeral or "IMI" in numeral or "IL" in numeral or "IC" in numeral or "ID" in numeral or "IM" in numeral or "XD" in numeral or "XM" in numeral or "IXX" in numeral or "XCC" in numeral or "DCD" in numeral:
        root = tk.Tk()
        output_label = tk.Label(root, text="Invalid Roman numeral: " + numeral)
        output_label.pack()
        root.mainloop()
    result = 0
    for i in range(len(numeral)):
        if i > 0 and roman_to_arabic_map[numeral[i]] > roman_to_arabic_map[numeral[i - 1]]:
            result += roman_to_arabic_map[numeral[i]] - 2 * roman_to_arabic_map[numeral[i - 1]]
        else:
            result += roman_to_arabic_map[numeral[i]]
    if result > 3999:
        root = tk.Tk()
        output_label = tk.Label(root, text="Invalid Roman numeral, the numeral is greater than 3999")
        output_label.pack()
        root.mainloop()
    return result
def translate():
    input_text = input_entry.get()
    output_label.config(text=roman_to_arabic(input_text))

root = tk.Tk()
root.title("Roman to Arabic Converter")
root.configure(bg="gray")

input_label = tk.Label(root, bd=5, font = 15, text="Enter a Roman numeral:", bg="gray", fg="black")
input_label.pack()

input_entry = tk.Entry(root, width=30, bd=3, bg="gray", fg="white", font="bold")
input_entry.pack(padx=10, pady=10)

translate_button = tk.Button(root, text="Convert", command=translate, bg="gray")
translate_button.pack()

output_label = tk.Label(root, text="", font = 15, bg="gray", fg="white")
output_label.pack()

root.mainloop()