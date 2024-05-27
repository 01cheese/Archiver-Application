import flet as ft
import time
import zstandard as zstd
import os
import zipfile


class ZstdCompressor:
    def __init__(self, compression_level):
        self.compression_level = compression_level
        self.compressor = zstd.ZstdCompressor(level=compression_level)
        self.decompressor = zstd.ZstdDecompressor()

    def compress_file(self, input_path, output_path):
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            self.compressor.copy_stream(f_in, f_out)
        print(f"File {input_path} compressed to {output_path}")

    def decompress_file(self, input_path, output_path):
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            self.decompressor.copy_stream(f_in, f_out)
        print(f"File {input_path} decompressed to {output_path}")


def main(page: ft.Page):
    page.window_width = 800
    page.window_height = 600
    page.title = "Архиватор"
    page.scroll = "auto"

    # Function to update progress
    def update_progress(progress):
        progress_bar.value = progress
        page.update()

    # Handler for START button
    def start_compression(e):
        compression_level = int(compression_level_picker.value)
        input_path = input_file_path.value

        if not input_path:
            print("Input path is empty")
            return

        output_path = input_path + ".zip"
        encryption = password_field.value if password_field.value else None

        if os.path.isfile(input_path):
            # Compress single file
            compress_to_zip(input_path, output_path, encryption)
        elif os.path.isdir(input_path):
            # Compress directory
            compress_directory_to_zip(input_path, output_path, encryption)
        else:
            print("Invalid path")
            return

        # Dummy progress update for demonstration
        progress_bar.value = 0
        page.update()
        for i in range(1, 101):
            update_progress(i / 100.0)
            time.sleep(0.05)

        print("End")

    def compress_to_zip(input_path, output_path, password=None):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if password:
                zipf.setpassword(password.encode())
            zipf.write(input_path, os.path.basename(input_path))
        print(f"File {input_path} compressed to {output_path}")

    def compress_directory_to_zip(directory_path, output_path, password=None):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if password:
                zipf.setpassword(password.encode())
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))
        print(f"Directory {directory_path} compressed to {output_path}")

    # Handler for file picker result
    def on_file_picker_result(e: ft.FilePickerResultEvent):
        if e.files:
            input_file_path.value = e.files[0].path
            page.update()

    # Create UI elements
    input_file_path = ft.TextField(label="Archive", read_only=False, value="C:\\Users\\zelen\\Desktop\\750.zip")

    archive_format_picker = ft.Dropdown(
        label="Archive format",
        options=[
            ft.dropdown.Option("zip"),
            ft.dropdown.Option("7z"),
            ft.dropdown.Option("tar"),
        ],
        value="zip"
    )

    compression_level_picker = ft.Dropdown(
        label="Compression level",
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
            ft.dropdown.Option("6"),
            ft.dropdown.Option("7"),
            ft.dropdown.Option("8"),
            ft.dropdown.Option("9")
        ],
        value="9"
    )

    compression_method_picker = ft.Dropdown(
        label="Compression method",
        options=[
            ft.dropdown.Option("Deflate"),
            ft.dropdown.Option("LZMA"),
            ft.dropdown.Option("Zstandard"),
        ],
        value="Deflate"
    )

    dictionary_size_picker = ft.Dropdown(
        label="Dictionary size",
        options=[
            ft.dropdown.Option("32 KB"),
            ft.dropdown.Option("64 KB"),
            ft.dropdown.Option("128 KB"),
        ],
        value="32 KB"
    )

    word_size_picker = ft.Dropdown(
        label="Word size",
        options=[
            ft.dropdown.Option("128"),
            ft.dropdown.Option("256"),
            ft.dropdown.Option("512"),
        ],
        value="128"
    )

    cpu_threads_picker = ft.Slider(label="Number of CPU threads", min=1, max=8, divisions=7, value=4)

    memory_usage_picker = ft.Dropdown(
        label="Memory usage for Compressing",
        options=[
            ft.dropdown.Option("1 GB"),
            ft.dropdown.Option("2 GB"),
            ft.dropdown.Option("4 GB"),
            ft.dropdown.Option("8 GB"),
            ft.dropdown.Option("12 GB"),
        ],
        value="12 GB"
    )

    update_mode_picker = ft.Dropdown(
        label="Update mode",
        options=[
            ft.dropdown.Option("Add and replace files"),
            ft.dropdown.Option("Add and update files"),
        ],
        value="Add and replace files"
    )

    path_mode_picker = ft.Dropdown(
        label="Path mode",
        options=[
            ft.dropdown.Option("Relative pathnames"),
            ft.dropdown.Option("Full pathnames"),
        ],
        value="Relative pathnames"
    )

    create_sfx_checkbox = ft.Checkbox(label="Create SFX archive")
    compress_shared_files_checkbox = ft.Checkbox(label="Compress shared files")
    delete_files_after_compression_checkbox = ft.Checkbox(label="Delete files after compression")

    password_field = ft.TextField(label="Enter password", password=True, can_reveal_password=True)
    reenter_password_field = ft.TextField(label="Reenter password", password=True, can_reveal_password=True)
    encryption_method_picker = ft.Dropdown(
        label="Encryption method",
        options=[
            ft.dropdown.Option("ZipCrypto"),
            ft.dropdown.Option("AES-256"),
        ],
        value="ZipCrypto"
    )

    progress_bar = ft.ProgressBar(width=800, height=20)
    start_button = ft.ElevatedButton(text="OK", on_click=start_compression)

    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    page.overlay.append(file_picker)

    # Add widgets to the page
    page.add(
        ft.Container(
            ft.Column([
                ft.Row([input_file_path, ft.IconButton(icon=ft.icons.FOLDER_OPEN, on_click=lambda e: file_picker.pick_files())]),
                ft.Row([archive_format_picker, compression_level_picker, compression_method_picker]),
                ft.Row([dictionary_size_picker, word_size_picker, cpu_threads_picker]),
                ft.Row([memory_usage_picker, update_mode_picker, path_mode_picker]),
                ft.Row([create_sfx_checkbox, compress_shared_files_checkbox, delete_files_after_compression_checkbox]),
                ft.Row([password_field, reenter_password_field, encryption_method_picker]),
                progress_bar,
                start_button
            ]),
            padding=10,
            expand=True
        )
    )

# Run the application
ft.app(target=main)
