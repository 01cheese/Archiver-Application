# Archiver Application

This is a simple GUI-based archiving application built using the Flet framework and zstandard for compression. The application allows you to compress files or directories into ZIP format with various compression options.

## Features

- Select a file or directory to compress
- Choose compression level (1-9)
- Choose compression method (Deflate, LZMA, Zstandard)
- Set dictionary size and word size
- Specify the number of CPU threads to use
- Configure memory usage for compression
- Set update and path modes
- Optional SFX archive creation
- Option to compress shared files and delete files after compression
- Password protection with selectable encryption methods (ZipCrypto, AES-256)
- Progress bar to show compression progress

## Usage

1. **Run the application**:
    ```bash
    python App.py
    ```

2. **Use the UI to configure your compression settings**:
    - Select a file or directory by clicking the folder icon next to the "Archive" field.
    - Choose your desired compression settings from the dropdowns and sliders.
    - Optionally set a password and choose the encryption method.
    - Click "OK" to start the compression process. The progress bar will indicate the progress.

## File Structure

- `app.py`: Main application script
- `requirements.txt`: List of required Python packages

## Dependencies

- `flet`: Framework for building GUI applications
- `zstandard`: Library for Zstandard compression
- `zipfile`: Standard library for handling ZIP files

## Acknowledgements

- [Flet](https://flet.dev/) for the GUI framework
- [Zstandard](https://github.com/indygreg/python-zstandard) for compression
- Python's built-in `zipfile` module for ZIP file handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, please open an issue or contact me at [your-email@example.com](mailto:zelenko009@gmail.com).
