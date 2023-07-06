with open("logs.txt", "a+", encoding='utf-8') as f:
    f.seek(0)  # Move the file pointer to the beginning
    data = f.read()
    f.write("abcd")
