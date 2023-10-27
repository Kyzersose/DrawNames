import random

def draw_name(names):
  """Randomly draws a name from the given list of names without repeating a drawn name.

  Args:
    names: A list of names.

  Returns:
    A string containing the name that was drawn.
  """
shaeffers = ["Matt", "Sarah", "Presley", "Nolan", "Cal", "Ben"]
lords = ['Josh','Holly','Levi','Noah','Isaac']
vaughans = ['Mitchel','Amanda','Sadie','Rachel']
powells = ['Steve','Anita']

drawn_names = set()
while True:
    name = random.choice(names)
    if name not in drawn_names:
      drawn_names.add(name)
    return name

def main():
  with open("names.json", "r") as f:
    names = json.load(f)

  drawn_names = []
  for person in names:
    name = draw_name(names)
    drawn_names.append(name)
    print(f"{person['name']}: {name}")

if __name__ == "__main__":
  main()