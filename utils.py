import json
from pprint import pprint as pp

from config import DATA_PATH

def _load_data(path=DATA_PATH):
    """ Загрузка данных о кандидатах"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def candidstes_get_all():
    """ Получение списка о кандидатах"""
    data = _load_data()
    return data

def candidate_get_pk(pk):
    """получение кандидата по его Pk"""
    candidates = _load_data()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate

def candidates_get_by_skill(skill_name):
    skilled_candidates = []
    skill_name_lower = skill_name.lower()
    candidates = _load_data()
    for candidate in candidates:
        skills = candidate['skills'].lower().strip().split(', ')
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
            continue
    return skilled_candidates


"""Тестирование функций"""
#pp(_load_data())
#pp(candidstes_get_all())
#pp(candidates_get_pk(3))
pp(candidates_get_by_skill('python'))