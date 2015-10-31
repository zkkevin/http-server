__author__ = 'Kevin Zhang'

# I modified this HTTP server based on a source code I downloaded from GitHub. But I unfortunely forget where I got it from.
# Please inform me if someone knows where this is sourced from... Thanks. :)

from HTTP import HTTP_Server
import cProfile


def main():
    server = HTTP_Server("localhost", 8080)
    #server.set_web_root("E:\\Program Files\\PythonWorkSpace\\HTTP-Server-master\\web_boot")
    server.run()


if __name__ == "__main__":
    # run main, don't save results in a file, sort by column 2 (cumtime)
    #cProfile.run('main()', None, 2)
    profiler = cProfile.Profile()
    try:
        profiler.run('main()')
    except KeyboardInterrupt:
        profiler.print_stats(2)  # Sort by cumulative time
        quit()
