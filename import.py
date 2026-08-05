import subprocess

branch = input("Branch name: ").strip()
while not branch:
    print("Branch name cannot be empty.")
    branch = input("Branch name: ").strip()

subprocess.run(
    ["git", "pull", "origin", branch],
    check=True,
)

print(f"Done. Pulled from branch '{branch}'.")