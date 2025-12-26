import os
import datetime


def s_to_hms_str_time(seconds):
    """Convert seconds to formatted time string (HH:MM:SS or MM:SS).
    
    Args:
        seconds: Number of seconds to convert.
    
    Returns:
        str: Formatted time string.
    """
    hours, remainder = divmod(round(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 0:
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    return '{:02}:{:02}'.format(int(minutes), int(seconds))


def get_tqdm_data_by_time(start_time, i, range):
    """Calculate timing statistics for progress bar.
    
    Args:
        start_time: Datetime when the iteration started.
        i: Current iteration index.
        range: Total number of iterations.
    
    Returns:
        tuple: (elapsed_time, estimate_time, average_iteration) as strings.
    """
    elapsed_seconds = (datetime.datetime.now() - start_time).total_seconds()
    elapsed_time = s_to_hms_str_time(elapsed_seconds)
    if i == 0 or elapsed_seconds == 0:
        estimate_time = average_iteration = '?'
    else:
        average_iteration = i / elapsed_seconds
        estimate_time = s_to_hms_str_time((range - i) / average_iteration)
        average_iteration = '{:.2f}'.format(average_iteration)
    return elapsed_time, estimate_time, average_iteration


def get_tqdm_step_line(terminal_columns_size, lst_len, i, start_time):
    """Generate a formatted progress bar line.
    
    Args:
        terminal_columns_size: Width of terminal in columns.
        lst_len: Total length of the iterable.
        i: Current iteration index.
        start_time: Datetime when the iteration started.
    
    Returns:
        str: Formatted progress bar string.
    """
    progress_ratio = i / lst_len
    progress_line_begin = f"{'{:3d}'.format(int(progress_ratio * 100))}%|"
    elapsed_time, estimate_time, average_iteration = get_tqdm_data_by_time(start_time, i, lst_len)
    progress_line_end = f"| {i}/{lst_len} [{elapsed_time}<{estimate_time}, {average_iteration}it/s]"
    progress_bar_len = terminal_columns_size - len(progress_line_begin + progress_line_end)
    progress_bar_filling_nb = round(progress_bar_len * progress_ratio) if progress_ratio != 0.5 else int(progress_bar_len * 0.5)
    progress_bar = "█" * progress_bar_filling_nb + " " * round(progress_bar_len * (1 - progress_ratio))
    return progress_line_begin + progress_bar + progress_line_end


def ft_tqdm(lst: range) -> None:
    """Display a progress bar for iteration (tqdm-like behavior).
    
    Args:
        lst: Range object to iterate over.
    
    Yields:
        None: Prints progress bar to stdout for each iteration.
    """
    terminal_columns_size = os.get_terminal_size().columns
    lst_len = len(lst)
    start_time = datetime.datetime.now()
    for i in lst:
        yield print("\r" + get_tqdm_step_line(terminal_columns_size, lst_len, i, start_time), end="", flush=True)
    print("\r" + get_tqdm_step_line(terminal_columns_size, lst_len, lst_len, start_time), end="", flush=True)
