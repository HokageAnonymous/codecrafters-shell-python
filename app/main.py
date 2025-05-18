import sys
import shutil
import os

def main():
    # Print the prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()  # Ensure the prompt is displayed immediately

    # Wait for user input
    command = input().strip()
    splitCommand = command.split()  # Split the command into a list

    if not splitCommand:
        main()
        return

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
    elif shutil.which(splitCommand[0]) is not None:
        os.system(command)
    elif splitCommand[0] == "cd":
        if len(splitCommand) > 1:
            path = os.path.expanduser(splitCommand[1])
            try:
                os.chdir(path)
            except FileNotFoundError:
                print(f"cd: {splitCommand[1]}: No such file or directory")
        else:
            print("cd: missing operand")
    elif splitCommand[0] == "pwd":
        print(os.getcwd())

    else:
        print(f"{splitCommand[0]}: command not found")
    main()

if __name__ == "__main__":
    main()

