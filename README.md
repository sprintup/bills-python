## Setup
- `python -m venv venv_scrape` to make the virtual environment first.

### setup.py to .egg-info way
- `pip install -e .`

### pyproject.toml way
- `pip install poetry` 
- `poetry new my_package`
- `poetry init`
- 

### Docker
- build 'docker build -t bills-python-practice .'

- If you wanted your Python logs to be written to C:\Users\MyUser\logs\logfile.log on your Windows machine, and assuming your Python script inside the container writes logs to /app/logs/logfile.log, you'd run: `docker run -v /c/repos/bills-python-practice/logs:/app/logs your_image_name` 
- When you run the container, redirect its stdout to a file on the host: `docker run bills-python-practice > C:/repos/bills-python-practice/logfile.log`
- If you want to ensure that both stdout and stderr from the Docker container are redirected to the file, you can use the following command: `docker run bills-python-practice > C:/repos/bills-python-practice/logfile.log 2>&1` 
  - Here, `2>&1` is a shell redirection that says "redirect standard error (file descriptor 2) to wherever standard output (file descriptor 1) is currently going". In this context, it ensures that both standard output and standard error from the Docker command are written to logfile.log.


- [chat GPT python convo on docker](https://chat.openai.com/c/cb21464f-1ab8-4bef-adbc-247478b0ed9c)