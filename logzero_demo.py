import os
import logzero

# 默认格式
DEFAULT_FORMAT = '%(color)s [%(levelname)s %(asctime)s %(module)s:%(lineno)s ==> %(message)s] %(end_color)s'
# 时间格式
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
# 默认存放路径
# DEFAULT_LOG_FILE_PATH = os.environ['DEFAULT_LOG_FILE_PATH']
DEFAULT_LOG_FILE_PATH = ''


def get_customized_logger(filename,  # 日志名称
                          logfile_path='',  # 日志存储位置
                          level=logzero.DEBUG,  # 日志最低等级（根据开发、线上调整）
                          formatter=None,  # 日志格式
                          max_bytes=1024 * 1024 * 5,  # 日志文件最大存储量，默认 5M
                          backup_count=3,  # 要保留的备份数量
                          disableStderrLogger=False,
                          isRootLogger=False,
                          json=False,  # 日志输出启用json格式
                          json_ensure_ascii=False):
    """
    此函数生成自定义日志实例，可根据需求灵活调整参数配置
    """
    if logfile_path:
        logfile_path = os.path.join(logfile_path, f'{filename}.log')
    else:
        logfile_path = os.path.join(DEFAULT_LOG_FILE_PATH, f'{filename}.log')
    if not formatter:
        formatter = DEFAULT_FORMAT
    return logzero.setup_logger(
        name=filename,
        logfile=logfile_path,
        level=level,
        formatter=logzero.LogFormatter(fmt=formatter, datefmt=DEFAULT_DATE_FORMAT),
        maxBytes=max_bytes,
        backupCount=backup_count,
        disableStderrLogger=disableStderrLogger,
        isRootLogger=isRootLogger,
        json=json,
        json_ensure_ascii=json_ensure_ascii
    )


# 支付宝日志
alipay_log = get_customized_logger('alipay', r'G:\PangQiu\日常开发')

alipay_log.debug('debug')
alipay_log.info('info')
alipay_log.warning('warning')
alipay_log.error('error')
