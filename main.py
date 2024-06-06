try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "2")
    file.writelines("something")
except KeyError as error_message:
    print(f"The Key {error_message} is not found")
else:
    content = file.read()
    print(content)
finally:
    file.close()



