import timeit

from FileLib.file_library import FileLibrary

BENCH_DIR_PATH = '.'

def benchmark(fn, number=100):
    """
    Run benchmark test and measure time to run function `fn` with `number` times
    """
    time_taken = timeit.timeit(fn, number=number)
    print(f"{fn.__name__:<20} ran {number} times in {time_taken:.6f} seconds ({time_taken/number:.6f} sec per call)")

if __name__ == '__main__':
    file_lib = FileLibrary(BENCH_DIR_PATH, True, False)
    benchmark(file_lib.scan_dirs, number=100)