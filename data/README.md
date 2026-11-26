# Dataset instructions

1. Download the dataset from [Mendeley Data version 3](https://data.mendeley.com/datasets/rmmmf2dp8d/3). If the download is unavailable, inspect the CSV in the [authors' GitHub repository](https://github.com/IhyaKhoir/A-Weighted-Sentiment-Dataset-for-Indonesian-Telemedicine-Text-Classification/tree/main/Dataset).
2. Verify that the file is the intended version and record the download date and source.
3. Place the CSV at `data/raw/WeightedSentimentTelemedicineDataset.csv`.
4. Do not commit the dataset to Git unless the lecturer and team have explicitly approved it and the license/source requirements are satisfied. The default `.gitignore` excludes raw and processed data.

Expected columns (case-insensitive): `platform`, `app_name`, `rating`, `review`, `sentiment`, `weight`.

The project uses `review` as text input and `sentiment` as the target. The `weight` column is a categorical review-informativeness label, not a numerical sample weight.

## Provenance record

Complete this before training:

- Dataset title: A Weighted Sentiment Dataset for Indonesian Telemedicine Text Classification
- Mendeley version: 3 (verify the actual downloaded file)
- Download date: TODO
- Download URL: TODO
- SHA-256 checksum: TODO
- License shown in source metadata: CC BY 4.0 (verify)
