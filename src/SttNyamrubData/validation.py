import os

import pandas as pd


def transform_csv(input_file, output_file):
    """
    Transforms the input CSV file to the required format.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the transformed CSV file.
    """
    try:
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created directory: {output_dir}")

        # Load the CSV file
        df = pd.read_csv(input_file)

        # Map levels to scores
        level_to_score = {"easy": 5, "medium": 10, "hard": 15}

        # Add the required columns
        df["origin_id"] = df["file_name"]
        df["source_audio_url"] = df["url"]
        df["target"] = df["reviewed_transcript"]
        df["score"] = df["level"].map(level_to_score)
        df["source_dialect"] = "U-tsang"
        df["source_language"] = "Tibetan"
        df["target_language"] = "Tibetan"

        # Select the required columns
        transformed_df = df[
            [
                "origin_id",
                "source_audio_url",
                "target",
                "score",
                "source_dialect",
                "source_language",
                "target_language",
            ]
        ]

        # Save the transformed DataFrame to a new CSV file
        transformed_df.to_csv(output_file, index=False)

        print(
            f"Transformed CSV saved to {output_file}. Total rows: {len(transformed_df)}"
        )
    except Exception as e:
        print(f"Error while transforming CSV: {e}")


# Example usage
input_csv = (
    "data/validation_data/utsang_training.csv"  # Replace with your input file path
)
output_csv = "data/validation_data_transformed/utsang_training_transformed.csv"  # noqa  # Replace with your desired output file path

transform_csv(input_csv, output_csv)
