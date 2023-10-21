import database

connection = database.connect()
database.create_table(connection)

print("Keyboard Ratings")
print("------------------")
print("""
1) Add new keyboard rating
2) List all keyboards
3) Find keyboard by name
4) Find highest rated keyboard
5) Exit program

Enter choice:""")

while (user_input := input()) != "5":
  match user_input:
    case "1":
      name, switch, brand, rating = input("Enter keyboard name: "), input("Enter switch type of keyboard: "), input("Enter brand of keyboard: "), input("Enter rating of keyboard (/100): ")

      database.add_kb(connection, name, switch, brand, rating)
    case "2":
      kbs = database.get_all_kb(connection)
      print("All keyboards rated")

      for kb in kbs:
        print(f"Name: {kb[1]}, Switch: {kb[2]}, Brand: {kb[3]}, Rating: {kb[4]}/100")
    case "3":
      name = input("Enter keyboard name: ")
      kbs = database.get_kb_by_name(connection, name)
      print(f"Keyboards named {name}")

      for kb in kbs:
        print(f"Name: {kb[1]}, Switch: {kb[2]}, Brand: {kb[3]}, Rating: {kb[4]}/100")
    case "4":
      kb = database.get_best_kb(connection)

      print(f"Highest rated keyboard\nName: {kb[1]}, Switch: {kb[2]}, Brand: {kb[3]}, Rating: {kb[4]}/100")
    case _:
      print("Invalid choice")

  print("Enter choice:")

print("Exited")