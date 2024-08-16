from tarot_cards.arcanas import major_arcanas, all_arcanas
from tarot_cards.arcanas_interpretation import arcanas_interpretation
from app.messages import layout_questions
from random import sample, choices


def perform_layout(data):

    # If value for a card is True it is Upright,
    # If it is False - it is Reversed
    if data['arcanas'] == 'Все Арканы':
        result = {k: choices([True, False], weights=[70, 30]) for k in sample(all_arcanas, layout_questions[data['layout']]['number'])}
    elif data['arcanas'] == 'Только Старшие Арканы':
        result = {k: choices([True, False], weights=[70, 30]) for k in sample(major_arcanas, layout_questions[data['layout']]['number'])}

    answer = ''
    result_keys = list(result.keys())
    list_of_questions = layout_questions[data['layout']]['questions']

    if data['layout'] != 'От Рая до Ада':
        for i in range(len(result_keys)):
            if str(*result[result_keys[i]]) == 'True':
                answer += f"""<b>{list_of_questions[i]} - Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
            else:
                answer += f"""<b>{list_of_questions[i]} - Перевернутая Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
    else:
        # очень много костылей, переписать
        for i in range(5):
            if str(*result[result_keys[i]]) == 'True':
                answer += f"""<b>{list_of_questions[i]} - Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
            else:
                answer += f"""<b>{list_of_questions[i]} - Перевернутая Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
        answer += f"<b>{list_of_questions[-1]}</b>\n"
        for i in range(5, 9):
            if str(*result[result_keys[i]]) == 'True':
                answer += f"""<b>{i+1}. - Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
            else:
                answer += f"""<b>{i+1}. - Перевернутая Карта {result_keys[i]}:</b> {arcanas_interpretation[result_keys[i]][bool(*result[result_keys[i]])]}\n\n"""
    return answer
