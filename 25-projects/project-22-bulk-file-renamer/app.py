import os

def bulk_rename(directory, prefix='', suffix='', replace_from='', replace_to='', target_extension=None, dry_run=True):
    try:
        files = os.listdir(directory)
        if target_extension:
            files = [f for f in files if f.endswith(target_extension)]

        if not files:
            print("No files found to rename.")
            return

        print(f"\nFiles to be renamed in: {directory}\n")

        for filename in files:
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}{name.replace(replace_from, replace_to)}{suffix}{ext}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            if dry_run:
                print(f"[DRY RUN] {filename} → {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_name}")

        print("\nOperation completed.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory = input("Enter the directory path: ").strip()
    prefix = input("Enter a prefix to add (leave blank for none): ").strip()
    suffix = input("Enter a suffix to add (leave blank for none): ").strip()
    replace_from = input("Text to replace in filenames (leave blank for none): ").strip()
    replace_to = input("Replace with (leave blank for none): ").strip()
    extension_filter = input("Only rename files with this extension (e.g. .txt) (leave blank for all files): ").strip()
    dry_run_input = input("Perform a dry run first? (yes/no): ").strip().lower()
    dry_run = dry_run_input != 'no'

    bulk_rename(
        directory=directory,
        prefix=prefix,
        suffix=suffix,
        replace_from=replace_from,
        replace_to=replace_to,
        target_extension=extension_filter if extension_filter else None,
        dry_run=dry_run
    )
