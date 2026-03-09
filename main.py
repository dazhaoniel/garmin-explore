import io
import gzip
import pandas as pd

from pathlib import Path
from garmin_fit_sdk import Decoder, Stream


SOURCE_DIR = 'data'
EXPORT_DIR = 'export'

directory_path = Path(SOURCE_DIR)
files_in_dir = [p for p in directory_path.iterdir() if p.is_file()
                and p.suffix == '.gz']

for file_path in files_in_dir:
    file_name = str(file_path).split('/')[-1] + '.csv'
    gz = gzip.open(file_path, 'rb').read()

    temp_file = io.BytesIO(gz)

    stream = Stream.from_byte_array(temp_file.getbuffer())
    decoder = Decoder(stream)
    messages, errors = decoder.read()

    # print(errors)
    # print(messages)

    df = pd.DataFrame({k: pd.Series(v) for k, v in messages.items()})
    df.to_csv(Path(EXPORT_DIR) / file_name, index=False)
