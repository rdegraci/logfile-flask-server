# Logfile Flask Server

This project hosts a simple Flask server with a single endpoint that enables concatenation of log files based on a prefix provided through a POST request. The server reads its host and port configuration from a `server.yaml` file.

## Features

- **Log Concatenation**: Submits a prefix via a POST request to the `/logs/cat` endpoint, which executes a shell script, `concatenate_logs.sh`, to concatenate logs starting with the given prefix.
- **Configurable Server**: Reads host and port details from `server.yaml`.

## Requirements

- Python 3.x
- Flask
- pyyaml

## Installation

1. Clone the repository to your local machine.
```bash
$ git clone https://github.com/rdegraci/logfile-flask-server.git
```
2. Navigate into the project directory.
```bash
$ cd your-repo-name
```
3. Install the required dependencies.
```bash
$ pip install -r requirements.txt
```

## Configuration

- The server host and port can be configured in the `server.yaml` file.

```yaml
host: "0.0.0.0"
port: 4735
```

## Usage

1. Start the Flask server.
```bash
$ python server.py
```

2. Send a POST request to concatenate logs with the required prefix.
```bash
$ curl -X POST http://localhost:4735/logs/cat -H "Content-Type: application/json" -d '{"prefix":"your_log_prefix"}'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request.

## Author

- Rodney Degracia [rdegraci@gmail.com]
