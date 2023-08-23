import logging

# Choose your logging method:
# 1. Log to stdout
logging.basicConfig(level=logging.INFO)

# 2. Log directly to a file (uncomment the lines below if you want this method)
# log_file_path = '/app/logs/logfile.log'
# logging.basicConfig(filename=log_file_path, level=logging.INFO)

def main():
    logging.info("This is a log message.")

if __name__ == '__main__':
    main()
