from pathlib import Path

CUSTOM_TEMPLATE = "README.md"
assert Path(CUSTOM_TEMPLATE).is_file()

def main():
  print("hello, world")
  print("Bye")


if __name__ == "__main__":
  main()
