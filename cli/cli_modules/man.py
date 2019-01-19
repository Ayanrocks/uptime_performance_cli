from .utilities import utilities as util


def man():
    commands = {
        "man": "Show the help page",
        "help": "Same as 'man' command",
        "clear": "Clears the cli",
        "check --url, --u (url) --packets, --p (packets)": "Pinging and testing server. Takes url as an optional argument",
        "os": "Shows info about the current os",
        "version, -v": "Shows version of the cli",
        "mem": "Shows available memory on the system",
        "cpu": "Shows info about the cpu",
        "get_id": "Shows the process id of the current process",
        "list_logs": "shows available logs",
        "more_log_info --(id)": "Show details of a specified log file",
        "exit": "Kills the cli"
    }

    util.horizontal_line()
    util.centered("CLI Manual")
    util.horizontal_line()
    util.vertical_space(2)

    for key, val in commands.items():
        value = "\033[92m" + val + "\033[0m"
        line = "\033[94m" + key + "\033[0m"
        padding = 60 - len(line)
        val = val[:40] + "\n" + (" " * padding) + val[40:]
        while(padding):
            line += " "
            padding -= 1

        line += value
        print(line)
        util.vertical_space()

    util.vertical_space(2)
    util.horizontal_line()
