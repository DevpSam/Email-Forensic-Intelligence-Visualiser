import pandas as pd
import re
import os


def extract_email(text):
    """Extracts email address from the 'From' or 'To' headers."""
    if not isinstance(text, str):
        return None
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None


def process_enron(input_file, output_file, limit=10000):
    """
    Processes the large Enron emails.csv to extract a source-target network.

    Args:
        input_file: Path to the 1.5GB Kaggle emails.csv
        output_file: Path to save the small processed CSV
        limit: Number of emails to process (helps keep the graph readable)
    """
    print(f"Reading {input_file}...")

    # We use chunksize to avoid loading 1.5GB into RAM at once
    chunks = pd.read_csv(input_file, chunksize=limit)
    df = next(chunks)  # Just take the first chunk for a usable visualization

    edges = []

    print("Extracting network edges...")
    for message in df['message']:
        # Simple regex to find From: and To: lines in the raw message text
        from_match = re.search(r'From: (.*)\n', message)
        to_match = re.search(r'To: (.*)\n', message)

        if from_match and to_match:
            sender = extract_email(from_match.group(1))
            receiver = extract_email(to_match.group(1))

            if sender and receiver:
                edges.append({'from': sender, 'to': receiver})

    # Save to a small CSV
    edge_df = pd.DataFrame(edges)
    edge_df.to_csv(output_file, index=False)
    print(f"Done! Created {output_file} with {len(edge_df)} connections.")
    print("You can now upload this small file to your 3D Dashboard.")


if __name__ == "__main__":
    # Ensure emails.csv is in the same folder
    if os.path.exists('emails.csv'):
        process_enron('emails.csv', 'enron_edges.csv')
    else:
        print("Error: 'emails.csv' not found. Please place the Kaggle file in this directory.")