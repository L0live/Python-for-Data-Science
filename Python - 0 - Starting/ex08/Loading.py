import os
import datetime

def get_elapsed_time(start_time, i, range):
    elapsed_seconds = (datetime.datetime.now() - start_time).total_seconds()
    hours, remainder = divmod(int(elapsed_seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 0:
        elapsed_time = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
    else:
        elapsed_time = '{:02}:{:02}'.format(int(minutes), int(seconds))
    if i == 0 or elapsed_seconds == 0:
        average_iteration = 0.00
    else:
        average_iteration = '{:.2f}'.format(i / elapsed_seconds)
    return elapsed_time, average_iteration

def ft_tqdm(lst: range) -> None:
    terminal_columns_size = os.get_terminal_size().columns
    lst_len = len(lst)
    start_time = datetime.datetime.now()
    average_iteration = 0
    estimate_time = 0
    for i in lst:
        progress_ratio = i / lst_len
        progress_line_begin = f"{'{:3d}'.format(int(progress_ratio * 100))}%|"
        elapsed_time, average_iteration = get_elapsed_time(start_time, i, lst_len)
        progress_line_end = f"| {i}/{lst_len} [{elapsed_time}<00:00, {average_iteration}it/s]"
        progress_bar_len = terminal_columns_size - len(progress_line_begin + progress_line_end)
        progress_bar = "█" * round(progress_bar_len * progress_ratio) + " " * round(progress_bar_len * (1 - progress_ratio))
        yield print("\r" + progress_line_begin + progress_bar + progress_line_end, end="", flush=True)

    progress_ended_line_begin = f"100%|"
    elapsed_time = get_elapsed_time(start_time, 0, lst_len)
    progress_ended_line_end = f"| {lst_len}/{lst_len} [{elapsed_time}<00:00, {average_iteration}it/s]"
    progress_ended_bar = "█" * (terminal_columns_size - len(progress_ended_line_begin + progress_ended_line_end) - 1)
    print("\r" + progress_ended_line_begin + progress_ended_bar + progress_ended_line_end, end="", flush=True) 
