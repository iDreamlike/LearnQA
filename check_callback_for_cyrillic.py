import os
import yaml
import re


def contains_cyrillic(text):
    # Проверяем содержание кириллических символов
    check = re.search('[\u0400-\u04FF]', text)
    if bool(check):
        print(f"Найдена строка с кириллицей: {check}")
    return bool(check)


def check_yaml_for_cyrillic(data, fields_to_check, path=""):
    # Рекурсивно проверяем указанные поля в yaml-файле на наличие кириллических символов
    issues = {}
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{path}.{key}" if path else key
            if key in fields_to_check and isinstance(value, str):
                # print(f"Проверяем поле '{new_path}' со значением: {value}")
                if contains_cyrillic(value):
                    issues[new_path] = value
            elif isinstance(value, (dict, list)):
                issues.update(check_yaml_for_cyrillic(value, fields_to_check, new_path))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{path}[{index}]"
            issues.update(check_yaml_for_cyrillic(item, fields_to_check, new_path))
    return issues


if __name__ == "__main__":
    # Собираем путь к yaml-файлу
    file_path = os.path.join('resources', 'corp-showcase-callback.yml')
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        documents = yaml.safe_load_all(file)
        fields_to_check = ['productCode', 'requestType', 'advCode', 'landings']
        all_issues = {}
        print(f"Проверяем поля: {fields_to_check}")

        for doc_index, data in enumerate(documents):
            issues = check_yaml_for_cyrillic(data, fields_to_check)
            if issues:
                all_issues[doc_index] = issues

    if all_issues:
        print("В этих полях есть кириллица:")
        for doc_index, issues in all_issues.items():
            for field_path, value in issues.items():
                print(f"Document {doc_index}, {field_path}: {value}")
    else:
        print("В указанных полях кириллица не найдена")