def duration_show(duration):
    if duration < 60:
        return f'Duration: {duration} sec'
    elif duration < 3600:
        return f'Duration: {duration // 60} min {duration % 60} sec'
    else:
        return f'Duration: {duration // 3600} h {duration % 3600 // 60} min {duration % 60} sec'