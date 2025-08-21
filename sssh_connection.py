import subprocess

def ssh_command(host, username, command, port=22, key_file=None):
    try:
        # Build ssh command for Git Bash
        ssh_cmd = ["ssh", f"{username}@{host}", "-p", str(port), command]

        # If using a private key
        if key_file:
            ssh_cmd = ["ssh", "-i", key_file, f"{username}@{host}", "-p", str(port), command]

        # Run command via Git Bash
        result = subprocess.run(
            ssh_cmd,
            capture_output=True,
            text=True,
            shell=True  # Needed for Git Bash on Windows
        )

        # Print stdout and stderr
        if result.stdout:
            print("Output:\n", result.stdout)
        if result.stderr:
            print("Error:\n", result.stderr)

    except Exception as e:
        print(f"Failed to execute SSH command: {e}")


# Example usage
if __name__ == "__main__":
    ssh_command(
        host="192.168.1.100",   # Replace with your host
        username="your_username",
        command="ls -la",       # Command to run remotely
        port=22,
        key_file=None           # Or provide path to private key, e.g. "C:/Users/you/.ssh/id_rsa"
    )
