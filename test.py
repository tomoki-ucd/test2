from pathlib import Path

CUSTOM_TEMPLATE = "README.md"
assert Path(CUSTOM_TEMPLATE).is_file()

def main():
  print("Hello, world")


if __name__ == "__main__":
  main()
