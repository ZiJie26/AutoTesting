import os
import datetime


def cleanup_reports(directory, days=7):
    """
    删除指定目录中超过指定天数的报告文件。

    :param directory: 要清理的目录
    :param days: 超过多少天的文件会被删除
    """
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=days)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_mtime < cutoff:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
