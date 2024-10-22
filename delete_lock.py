import os

def remove_lock_file(path):
  """Deletes the lock file if it exists."""
  if os.path.exists(path):
    try:
      os.remove(path)
      print(f"Deleted: {path}")
    except OSError as e:
      print(f"Deletion error {path}: {e}")
  else:
    print(f"The file does not exist: {path}")

if __name__ == "__main__":
  paths = [
    "/home/your_username/.var/app/com.jetbrains.IntelliJ-IDEA-Ultimate/config/JetBrains/IntelliJIdea2023.3/.lock",
    "/home/your_username/.var/app/com.jetbrains.IntelliJ-IDEA-Community/config/JetBrains/IdeaIC2023.3/.lock",
    "/home/your_username/.var/app/com.jetbrains.PyCharm-Professional/config/JetBrains/PyCharm2023.3/.lock"
  ]

  for path in paths:
    remove_lock_file(path)
