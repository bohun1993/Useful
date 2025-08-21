import pexpect

def ssh_interactive(host, username, command=None, port=22, key_file=None):
    try:
        # Build ssh command
        ssh_cmd = f"ssh -tt -p {port} {username}@{host}"
        if key_file:
            ssh_cmd = f"ssh -i {key_file} -tt -p {port} {username}@{host}"

        # Start interactive ssh session
        child = pexpect.spawn(ssh_cmd, encoding="utf-8")

        # Optional: capture initial login messages
        child.logfile_read = open("ssh_output.log", "w")  # also logs everything to file

        # If command provided, send it
        if command:
            child.expect(r"\$")  # wait for shell prompt (you can adjust regex for your shell, e.g. '>')
            child.sendline(command)
            child.expect(r"\$")  # wait for prompt again
            print(child.before)  # this contains the command output

        # Example: stay interactive
        print("Entering interactive mode. Type 'exit' to quit.\n")
        child.interact()  # hand over control to user interactively

    except Exception as e:
        print(f"SSH session failed: {e}")


if __name__ == "__main__":
    ssh_interactive(
        host="192.168.1.100",
        username="your_username",
        command="ls -la",   # optional initial command
        port=22,
        key_file=None
    )
