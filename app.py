import json
from pathlib import Path
from data_parser import parse_input
from decision_maker import DecisionMaker
def main():
    try:
        # 1. Загрузка данных
        input_path = Path('input.json')
        print(f"[INFO] Загрузка данных из {input_path}")
        input_data = parse_input(input_path)

        # 2. Расчет результатов
        print("[INFO] Расчет результатов...")
        dm = DecisionMaker(input_data)
        results = dm.calculate()

        # 3. Экспорт в json
        output_path = Path('output.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        print(f"[INFO] Результаты сохранены в {output_path}")

    except Exception as e:
        print(f"[FATAL] Критическая ошибка: {str(e)}")


if __name__ == "__main__":
    main()