import sys
import shutil
import os 

def main():
    # Print the prompt
    sys.stdout.write("$ ")
    sys.stdout.flush()  # Ensure the prompt is displayed immediately

    # Wait for user input
    command = input().strip()
    splitCommand = command.strip()
    if command == "exit 0":
        sys.exit(0)
    elif command.startswith("type "):
        type_command = command.replace("type ", "")
        if type_command in ("echo", "exit", "type"):
            print(f"{type_command} is a shell builtin")
        else:
        
            path = shutil.which(type_command)
            if path:
                print(f"{type_command} is {path}")
            else:
                print(f"{type_command}: not found")
    elif shutil.which(splitCommand[0]) is not None:
        os.system(command)

    elif command.startswith("echo "):
        print(command[5:])
    else:
        print(f"{command}: command not found")
    main()

if __name__ == "__main__":
    main()

