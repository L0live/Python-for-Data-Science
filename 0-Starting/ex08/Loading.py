from os import get_terminal_size
from datetime import datetime as dt


def s_to_hms_str_time(seconds):
    """Convert seconds to formatted time string (HH:MM:SS or MM:SS).

    Args:
        seconds: Number of seconds to convert.

    Returns:
        str: Formatted time string.
    """
    hours, remainder = divmod(round(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours == 0:
        return '{:02}:{:02}'.format(int(minutes), int(seconds))
    return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


def get_tqdm_data_by_time(start_time, i, range):
    """Calculate timing statistics for progress bar.

    Args:
        start_time: Datetime when the iteration started.
        i: Current iteration index.
        range: Total number of iterations.

    Returns:
        tuple: (elapsed_time, estimate_time, average_iteration) as strings.
    """
    elapsed_seconds = (dt.now() - start_time).total_seconds()
    elapsed_time = s_to_hms_str_time(elapsed_seconds)
    if i == 0 or elapsed_seconds == 0:
        estimate_time = average_iteration = '?'
    else:
        average_iteration = i / elapsed_seconds
        estimate_time = s_to_hms_str_time((range - i) / average_iteration)
        average_iteration = '{:.2f}'.format(average_iteration)
    return elapsed_time, estimate_time, average_iteration


def get_tqdm_step_line(terminal_size, lst_len, i, start_time):
    """Generate a formatted progress bar line.

    Args:
        terminal_size: Width of terminal in columns.
        lst_len: Total length of the iterable.
        i: Current iteration index.
        start_time: Datetime when the iteration started.

    Returns:
        str: Formatted progress bar string.
    """
    progRatio = i / lst_len
    progBeg = f"{'{:3d}'.format(int(progRatio * 100))}%|"
    elapsT, estimT, averageIt = get_tqdm_data_by_time(start_time, i, lst_len)
    progEnd = f"| {i}/{lst_len} [{elapsT}<{estimT}, {averageIt}it/s]"
    progLen = terminal_size - len(progBeg + progEnd)
    if progRatio != 0.5:
        progFill = round(progLen * progRatio)
    else:
        progFill = int(progLen * 0.5)
    progress_bar = "█" * progFill + " " * round(progLen * (1 - progRatio))
    return progBeg + progress_bar + progEnd


def ft_tqdm(lst: range) -> None:
    """Display a progress bar for iteration (tqdm-like behavior).

    Args:
        lst: Range object to iterate over.

    Yields:
        None: Prints progress bar to stdout for each iteration.
    """
    terminal_size = int(get_terminal_size().columns)
    lst_len = len(lst)
    start_time = dt.now()
    for i in lst:
        step_line = get_tqdm_step_line(terminal_size, lst_len, i, start_time)
        yield print("\r" + step_line, end="", flush=True)
    step_line = get_tqdm_step_line(terminal_size, lst_len, lst_len, start_time)
    print("\r" + step_line, end="", flush=True)
