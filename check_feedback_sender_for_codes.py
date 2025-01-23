import os
import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return list(yaml.safe_load_all(file))

def load_codes(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file and split by comma to get individual codes
        return file.read().strip().split(', ')

def check_codes_in_yaml(yaml_data, codes):
    missing_codes = []
    campaigns = []

    # Collect all campaigns from all documents
    for document in yaml_data:
        campaigns.extend(document.get('banners-api', {}).get('campaignsForFeedback', []))

    for code in codes:
        if code not in campaigns:
            missing_codes.append(code)
            print(f"Code not found: {code}")

    return missing_codes

def main():
    yaml_file_path = os.path.join('resources', 'corp-showcase-advertisement-feedback-sender-api.yml')
    codes_file_path = os.path.join('resources', 'new-codes.txt')

    yaml_data = load_yaml(yaml_file_path)
    codes = load_codes(codes_file_path)

    missing_codes = check_codes_in_yaml(yaml_data, codes)

    if not missing_codes:
        print("All codes are present in the YAML file.")
    else:
        print(f"Total missing codes: {len(missing_codes)}")

if __name__ == "__main__":
    main()