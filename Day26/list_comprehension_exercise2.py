import pandas
with open("file1.txt") as file1:
    file1_content = file1.readlines()
print(file1_content)

with open("file2.txt") as file2:
    file2_content = file2.readlines()
print(file2_content)

result = [int(num) for num in file1_content if num in file2_content]

# Write your code above 👆

print(result)
