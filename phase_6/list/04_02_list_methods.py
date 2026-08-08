numbers = [10, 20, 30, 20]
numbers.remove(20)
print(numbers)



colors = ["Red", "Blue", "Green"]
colors.remove("Blue")
print(colors)



students = ["Rahul", "Priya", "Saniya", "Aman"]
students.remove("Rahul")
print(students)



subjects = ["Math", "Science", "English", "History"]
subjects.remove("Math")
print(subjects)



numbers = [10, 20, 30]
numbers.pop()
print(numbers)



numbers = [10, 20, 30, 40]
numbers.pop(1)
print(numbers)


students = ["Rahul", "Aisha", "Saniya"]
name = students.pop(0)
print(name)
print(students)



students = ["Saniya", "Priya", "Aman", "Neha"]
removed = students.pop()
print("Removed:", removed)
print(students)



cart = ["Laptop", "Mouse", "Keyboard", "Monitor"]
item = cart.pop(0)
print("Removed:", item)
print(cart)



actions = ["Open File", "Edit", "Save", "Print"]
last_action = actions.pop()
print("Undo:", last_action)
print(actions)




history = [
    "google.com",
    "youtube.com",
    "github.com",
    "chat.openai.com"
]
last_page = history.pop()
print("Closed:", last_page)
print(history)



stack = []
stack.append("Book 1")
stack.append("Book 2")
stack.append("Book 3")
print("Removed:", stack.pop())
print(stack)



numbers = [10, 20, 30]
numbers.clear()
print(numbers)



fruits = ["Apple", "Banana"]
fruits.clear()
print(fruits)



notifications = [
    "New Message",
    "Friend Request",
    "Software Update"
]
notifications.clear()
print(notifications)



numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)



numbers = [10, 20, 30, 40, 50]
del numbers[1:4]
print(numbers)



numbers = [10, 20, 30]
del numbers
print(numbers)



