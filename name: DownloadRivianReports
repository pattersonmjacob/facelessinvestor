# Run the script every day at 00:00 UTC
on:
  schedule:
    - cron: '0 0 * * *'

jobs:
  download:
    runs-on: ubuntu-latest
    steps:
      # Step 1: Check out the repository
      - name: Check out the repository
        uses: actions/checkout@v3

      # Step 2: Set up Python environment
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      # Step 3: Install required Python packages
      - name: Install dependencies
        run: |
          pip install requests beautifulsoup4

      # Step 4: Run the download script
      - name: Run download script
        run: python download_rivian_reports.py

      # Step 5 (Optional): Commit and push the new files if any
      - name: Commit and push changes
        run: |
          git config --local user.name "github-actions[bot]"
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git add .
          git commit -m "Add latest Rivian report"
          git push
        if: success()  # Only push if download was successful
