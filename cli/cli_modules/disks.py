from .utilities import utilities as ut
import psutil as ps


def disks():
    ut.vertical_space()
    ut.horizontal_line()
    ut.centered("Disks")
    ut.horizontal_line()
    ut.vertical_space(2)

    print(ut.colored_string("\n    DISKS  \n", 93))
    disk_partitions = ps.disk_partitions()
    disk_usage = ps.disk_usage('/')
    disk_io = ps.disk_io_counters(perdisk=True)

    part = 0
    for item in disk_partitions:
        print(ut.colored_string("\nPartition: " + str(part) + "\n", 95))
        part += 1
        for i in item._fields:
            print(ut.colored_string(i.replace("_", " ").title(), 92) + ": " +
                  str(getattr(item, i)))
    try:
        for i in disk_usage._fields:
            print(ut.colored_string(i.replace("_", " ").title(), 92) + ": " +
                  str(getattr(disk_usage, i)) + " bytes")
    except:
        pass

    for k, v in disk_io.items():
        print(ut.colored_string("\n" + k + "\n", 96))
        for i in v._fields:
            print(ut.colored_string(i.replace("_", " ").title(), 92) +
                  ": " + str(getattr(v, i)))
