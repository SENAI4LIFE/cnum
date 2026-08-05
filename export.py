import subprocess

message = input("Commit message [update]: ").strip()
if not message:
    message = "update"

branch = input("Branch name: ").strip()
while not branch:
    print("Branch name cannot be empty.")
    branch = input("Branch name: ").strip()

subprocess.run(["git", "add", "-A"], check=True)

commit = subprocess.run(
    ["git", "commit", "-m", message],
    text=True,
)

if commit.returncode != 0:
    print("Nothing to commit.")

subprocess.run(["git", "push", "origin", branch], check=True)

print(f"Done. Pushed to branch '{branch}'.")