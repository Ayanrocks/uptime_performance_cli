import os


def open_file(curr_dir, file):
    file_path = os.path.join(curr_dir, file)
    print("\n Reading Log...\n\n")
    try:
        fs = open(file_path, "r")
        print(fs.read())
        print("\n\n ------End of LOG------\n")
        fs.close()
        return
    except:
        print("\nError Opening log.")
        return


def get_logs(log):
    curr_dir = os.path.abspath(".data/logs/")
    files = [f for f in os.listdir(
        curr_dir) if os.path.isfile(os.path.join(curr_dir, f)) and f.endswith(".log") and log in f]
    if len(files) == 0:
        print("Print No log file found. Remember log format is DD-MM-YY--HHMMSS")

    elif len(files) > 1:
        print("Multiple Log Entries found. Choose the desired one")
        for i, v in enumerate(files):
            i += 1
            print(str(i) + " - " + str(v))
        ch = input("\nWhich File to open: ")
        try:
            ch = int(ch)
            if not ch <= len(files):
                print("\nInvalid entry")
                return
            else:
                open_file(curr_dir, files[ch - 1])
        except:
            ch = input("\nInvalid entry choose again. Press q to exit: ")
            if ch.replace(" ", "") == 'q':
                return
            else:
                try:
                    ch = int(ch)
                    if not ch <= len(files):
                        print("\nInvalid entry")
                        return
                    else:
                        open_file(curr_dir, files[ch - 1])

                except:
                    return
    else:
        open_file(curr_dir, files[0])


def log_info(cmd):
    cmd_split = cmd.split("--")
    if len(cmd_split) == 2:
        log = cmd_split[1]
        get_logs(log)
    elif len(cmd_split) == 3:
        log = cmd_split[1] + "--" + cmd_split[2]
        get_logs(log)
    else:
        log = input(
            "Please enter a valid log name. (For all logs use 'list_log' command): ")
        get_logs(log)
