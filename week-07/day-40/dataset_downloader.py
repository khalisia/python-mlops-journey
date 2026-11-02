from pathlib import Path
import requests

# URL of a public sample dataset 
DATASET_URL = (
    "https://raw.githubusercontent.com/"
    "mwaskom/seaborn-data/master/iris.csv"
)

# Folder where datasets will be saved
DATASET_DIR = Path("datasets")
FILENAME = "iris.csv"

def download_dataset():
    # Creation of the destination folder
    DATASET_DIR.mkdir(parents=True, exist_ok=True)
    # Build the complete output path
    destination = DATASET_DIR / FILENAME

    try:
        print("Starting dataset download...")

        # Send an HTTP GET request
        with requests.get(
            DATASET_URL,
            stream=True,
            timeout=30
        ) as response:

            # Raise an error for HTTP failures
            response.raise_for_status()

            # Download the response in small chunks
            with destination.open("wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)

        # Check that the downloaded file is not empty
        if destination.stat().st_size == 0:
            destination.unlink()
            raise ValueError("Downloaded file is empty.")

        print("Download completed successfully!")
        print(f"Saved to: {destination.resolve()}")
        print(f"File size: {destination.stat().st_size:,} bytes")

    except requests.exceptions.RequestException as error:
        print(f"Download failed: {error}")

        # Remove an incomplete file after a failed download
        if destination.exists():
            destination.unlink()

    except (OSError, ValueError) as error:
        print(f"File error: {error}")
        if destination.exists():
            destination.unlink()

if __name__ == "__main__":
    download_dataset()