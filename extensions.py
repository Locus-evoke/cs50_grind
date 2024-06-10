media_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

file_name = input("File name: ").strip().lower()

found = False

# file_len = file_name.split(sep = '.')
# while len(file_len) > 2:
#     file_len.pop()

# a,b = file_len
# file_name = a +"."+ b

for extension, correspondance in media_types.items():
    if file_name.endswith(extension):
        print(correspondance)
        found = True
        break

if not found:
    print("application/octet-stream")