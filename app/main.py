import sys
import shutil
import os
import subprocess

def main():
    # Print the prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()  # Ensure the prompt is displayed immediately

    # Wait for user input
    command = input().strip()

    if not command:
        main()
        return

    # Check for output redirection
    if '>' in command:
        # Split the command and the output file
        parts = command.split('>')
        cmd_part = parts[0].strip()
        output_file = parts[1].strip()

        # Handle the command execution with output redirection
        try:
            with open(output_file, 'w') as f:
                subprocess.run(cmd_part, shell=True, stdout=f, stderr=subprocess.PIPE, text=True)
        except Exception as e:
            print(f"Error: {e}")
        main()
        return

    splitCommand = command.split()

    if splitCommand[0] == "exit" and len(splitCommand) > 1 and splitCommand[1] == "0":
        sys.exit(0)
    elif splitCommand[0] == "type":
        if len(splitCommand) > 1:
            type_command = splitCommand[1]
            if type_command in ("echo", "exit", "type", "pwd", "cd"):
                print(f"{type_command} is a shell builtin")
            else:
                path = shutil.which(type_command)
                if path:
                    print(f"{type_command} is {path}")
                else:
                    print(f"{type_command}: not found")
        else:
            print("Usage: type <command>")
    elif splitCommand[0] == "echo":
        print(" ".join(splitCommand[1:]))
    elif splitCommand[0] == "pwd":
        print(os.getcwd())
    elif splitCommand[0] == "cd":
        if len(splitCommand) > 1:
            path = os.path.expanduser(splitCommand[1])  # Expand ~ to home directory
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: {splitCommand[1]}: No such file or directory")
        else:
            print("cd: missing operand")
    elif shutil.which(splitCommand[0]) is not None:
        os.system(command)
    else:
        print(f"{splitCommand[0]}: command not found")
    main()

if __name__ == "__main__":
    main()

