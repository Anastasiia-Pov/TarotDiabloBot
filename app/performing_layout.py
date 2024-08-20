from tarot_cards.arcanas import major_arcanas, all_arcanas
from tarot_cards.arcanas_interpretation import arcanas_interpretation
from app.messages import layout_questions
from random import sample, choices


def compile_answer(result, result_keys, list_of_questions, i):
    if str(*result[result_keys[i]]) == 'True':
        answer = f"""<b>{list_of_questions[i]} - Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
    else:
        answer = f"""<b>{list_of_questions[i]} - Перевернутая Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
    return answer


def perform_layout(data):
    # If value for a card is True it is Upright,
    # If it is False - it is Reversed
    # Generate cards layout
    if data['arcanas'] == 'Все Арканы':
        result = {k: choices([True, False], weights=[70, 30]) for k in sample(all_arcanas, layout_questions[data['layout']]['number'])}
    elif data['arcanas'] == 'Только Старшие Арканы':
        result = {k: choices([True, False], weights=[70, 30]) for k in sample(major_arcanas, layout_questions[data['layout']]['number'])}

    # Forming answer
    answer = ''
    result_keys = list(result.keys())
    list_of_questions = layout_questions[data['layout']]['questions']

    for i in range(layout_questions[data['layout']]['number']):
        if i == 5:
            answer += f"<b>6.-9. Пандемониум: символизирует битвы, с которыми вы столкнетесь, принимая все части себя и пытаясь найти путь к мастерству и свободе.</b>\n"
            answer += compile_answer(result, result_keys, list_of_questions, 5)
        else:
            answer += compile_answer(result, result_keys, list_of_questions, i)

    return answer
