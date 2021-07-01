#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdarg.h>

#define LOCAL_RED		"\033[31;1m"
#define LOCAL_YELLOW		"\033[0;33m"
#define LOCAL_GREEN		"\033[0;32m"
#define LOCAL_BULE		"\033[0;34m"
#define LOCAL_END		"\033[0m"

typedef enum _LOG_LEVEL {
	LOG_LEVEL_NONE = 0,
	LOG_LEVEL_DEBUG,
	LOG_LEVEL_INFO,
	LOG_LEVEL_WARN,
	LOG_LEVEL_ERROR,
	LOG_LEVEL_FATAL,
	LOG_LEVEL_MAX
} enLogLevel;

int g_current_dbg_level = 0;

#define LOG_DBG(tag, fmt, ...) \
	log_func(LOG_LEVEL_DEBUG, "D", tag, __LINE__, __func__, fmt, ##__VA_ARGS__)

#define LOG_INFO(tag, fmt, ...) \
	log_func(LOG_LEVEL_INFO, "I", tag, __LINE__, __func__, fmt, ##__VA_ARGS__)

#define LOG_WARN(tag, fmt, ...) \
	log_func(LOG_LEVEL_WARN, "W", tag, __LINE__, __func__, fmt, ##__VA_ARGS__)

#define LOG_ERROR(tag, fmt, ...) \
	log_func(LOG_LEVEL_ERROR, LOCAL_RED, "E", tag, __LINE__, __func__, fmt, ##__VA_ARGS__)

#define LOG_FATAL(tag, fmt, ...) \
	log_func(LOG_LEVEL_FATAL, "F", tag, __LINE__, __func__, fmt, ##__VA_ARGS__)


void log_func(int level, const char *color, const char *opt, const char *tag, int line, const char *func, const char *fmt, ...)
{
	if (level > g_current_dbg_level) {
		char msg_buf[20*1024];
		struct timeval current;

		va_list ap;
		va_start(ap, fmt);

		gettimeofday(&current, NULL);
		sprintf(msg_buf, "[%lu.%06lu] %s%s/%s (%d):(%s) ",
			current.tv_sec, current.tv_usec,
			color, opt, tag, line, func);

		vsprintf(msg_buf+strlen(msg_buf), fmt, ap);
		fprintf(stderr, "%s\033[0m", msg_buf);

		va_end(ap);
	}
}

#define TAG "VENC"

int main()
{
	//LOG_DBG(TAG, "log_debug \n");
	//LOG_INFO(TAG, "log info \n");
	//LOG_WARN(TAG, "log warn \n");
	LOG_ERROR(TAG, "log error \n");
	//LOG_FATAL(TAG, "log fatal \n");

	return 0;
}