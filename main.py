from file_operations import VERSION
import file_operations
from faker import Faker
import random




fake = Faker("ru_RU")


skills = [("Стремительный прыжок".replace("Стремительный прыжок", "С͒'т͒'р̋͠'е͠'м͒͠'и'т͒'е͠'л̋͠'ь̋'н͒'ы̋͠'й͒͠' п̋͠'р̋͠'ы̋͠'ж͒'о̋'к̋̋'")), ("Электрический выстрел".replace("Электрический выстрел", "Э͒͠͠'л̋͠'е͠'к̋̋'т͒'р̋͠'и'ч̋͠'е͠'с͒'к̋̋'и'й͒͠' в͒͠'ы̋͠'с͒'т͒'р̋͠'е͠'л̋͠'")), ("Ледяной удар".replace("Ледяной удар", "Л̋͠'е͠'д̋'я̋'н͒'о̋'й͒͠' у͒͠'д̋'а͠'р̋͠'")), ("Стремительный удар".replace("Стремительный удар", "С͒'т͒'р̋͠'е͠'м͒͠'и'т͒'е͠'л̋͠'ь̋'н͒'ы̋͠'й͒͠' у͒͠'д̋'а͠'р̋͠'")), ("Кислотный взгляд".replace("Кислотный взгляд", "К̋̋'и'с͒'л̋͠'о̋'т͒'н͒'ы̋͠'й͒͠' в͒͠'з̋̋͠'г͒͠'л̋͠'я̋'д̋'")), ("Тайный побег".replace("Тайный побег", "Т͒'а͠'й͒͠'н͒'ы̋͠'й͒͠' п̋͠'о̋'б̋'е͠'г͒͠'")), ("Ледяной выстрел".replace("Ледяной выстрел", "Л̋͠'е͠'д̋'я̋'н͒'о̋'й͒͠' в͒͠'ы̋͠'с͒'т͒'р̋͠'е͠'л̋͠'")), ("Огненный заряд".replace("Огненный заряд", "О̋'г͒͠'н͒'е͠'н͒'н͒'ы̋͠'й͒͠' з̋̋͠'а͠'р̋͠'я̋'д̋'"))]


runic_skills = []


for skill in skills:
    runic_skills.append(skills)


def main():
    for i in  range(10):
        skills3 = random.sample(skills,3)
        print(skills3)
        context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(3, 18),
        "agility": random.randint(3, 18),
        "endurance": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "luck": random.randint(3, 18),
        "skill_1": skills3[0],
        "skill_2": skills3[1],
        "skill_3": skills3[2]  
    }
    
        file_operations.render_template("charsheet-0.svg", f"Files/result_{i}.svg", context)


if __name__ ==  '__main__':
    main()