from .utilities import utilities as ut
import psutil as ps


def display_network():
    ut.vertical_space()
    ut.horizontal_line()
    ut.centered("Network Info")
    ut.horizontal_line()
    ut.vertical_space(2)

    net_io_counters = ps.net_io_counters()
    for i in net_io_counters._fields:
        print(ut.colored_string(i.replace("_", " ").title(), 92) + ": " +
              str(getattr(net_io_counters, i)) + " bytes")

    net_connections = ps.net_connections(kind="inet4")
    soc = 0
    for item in net_connections:
        print(ut.colored_string("\nSocket: " + str(soc) + "\n", 95))
        soc += 1
        for i in item._fields:
            print(ut.colored_string(i.replace("_", " ").title(), 92) + ": " +
                  str(getattr(item, i)))

    net_if_addrs = ps.net_if_addrs()
    for key, val in net_if_addrs.items():
        print(ut.colored_string("\n" + key + "\n", 91))
        for item in val:
            for i in item._fields:
                print(ut.colored_string(i.replace("_", " ").title(), 92) + ": " +
                      str(getattr(item, i)))

    net_if_stats = ps.net_if_stats()
    for k, v in net_if_stats.items():
        print(ut.colored_string("\n" + k + "\n", 96))
        for i in v._fields:
            print(ut.colored_string(i.replace("_", " ").title(), 92) +
                  ": " + str(getattr(v, i)))
