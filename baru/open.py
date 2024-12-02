with open("Cafe.txt", "w", encoding="utf-8") as file_ujian:
    width = 87
    file_ujian.write(f"{' ' * ((width - len('Toko Perkakas')) // 2)}Toko Perkakas\n")
    file_ujian.write(f"{' ' * ((width - len('Monthly Summary')) // 2)}Monthly Summary\n\n")

    file_ujian.write(f"{(('Monday, 11 November 2024'))}\n\n")
    file_ujian.write(f"QTY" + " " * (10) + "Item" + " " * (50) + "AMT (Rp)\n")
    
    
    
