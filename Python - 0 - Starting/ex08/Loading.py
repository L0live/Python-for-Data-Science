import os
import datetime

def ft_tqdm(lst: range) -> None:
    terminal_columns_size = os.get_terminal_size().columns
    lst_len = len(lst)
    start_time = datetime.datetime.now()
    average_iteration = 0
    estimate_time = 0
    for i in lst:
        progress_ratio = i / lst_len
        progress_line_begin = f"{'{:3d}'.format(int(progress_ratio * 100))}%|"
        elapsed_time = datetime.datetime.now() - start_time
        progress_line_end = f"| {i}/{lst_len} [00:00<00:00, 0it/s]"
        progress_bar_len = terminal_columns_size - len(progress_line_begin + progress_line_end) - 1
        progress_bar = "█" * int(progress_bar_len * progress_ratio) + " " * int(progress_bar_len * (1 - progress_ratio))
        yield print("\r" + progress_line_begin + progress_bar + progress_line_end, end="", flush=True)

    progress_ended_line_begin = f"100%|"
    progress_ended_line_end = f"| {lst_len}/{lst_len} [00:00<00:00, 0it/s]"
    progress_ended_bar = "█" * (terminal_columns_size - len(progress_ended_line_begin + progress_ended_line_end) - 1)
    print("\r" + progress_ended_line_begin + progress_ended_bar + progress_ended_line_end, end="", flush=True)