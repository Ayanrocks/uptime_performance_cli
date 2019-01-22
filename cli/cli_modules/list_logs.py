import os


def list_logs():
    curr_dir = os.path.abspath(".data/logs/")

    if not os.path.exists(curr_dir):
        print("No logs folder created or folder deleted")
    else:
        files = [f for f in os.listdir(
            curr_dir) if os.path.isfile(os.path.join(curr_dir, f)) and f.endswith(".log")]
        if len(files) == 0:
            print("No logs Created")
        else:

            print("\n" + str(len(files)) + " Logs Available -- \n")
            for f in files:
                print(f)
            print(
                "\nTo open a particular log use command more_log_info and pass the log name")
    return
