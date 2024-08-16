about_project = '''Данный бот является пет-проектом для разрботчика и практикой его навыков в разработке ТГ-бота на основе библиотеки aiogram3.
<b>Предистория:</b> разработчик, будучи фанатом серии игр Diablo и фанатом всего мистического, приобрел колоду карт и решил, сделать их использование более мобильным.
Чтобы карты всегда были под рукой, разработчик не только перенес все символы и интерпретацию карт в бот, но и реализовал мобильный расклад.
Если необходимо срочно получить ответ на волнующий вопрос, бот всегда под рукой
Проект основан на картах Diablo от Blizzard: https://uk.gear.blizzard.com/products/diabgp0003-diablo-the-sanctuary-tarot-deck-and-guidebook'''

layouts = {'about_layouts': """Количество карт и их значение будет меняться в зависимости от расклада.
Позиции карт в раскладе предаст ответу форму на поставленный вопрос,
в то время как каждая конкретная карта расскажет о деталях и раскроет свои тайны.
Есть расклады с использованием одной карты, однако в большинстве случаев больше карт помогут сформировать более полную картину и получить подробный ответ на заданный вопрос.
Старайтесь избегать инфальтильных вопросов.
Карты описывают общую картину, ваша задача при интерпретации переложить их на свою жизнь и опыт, и рассматривать их через призму себя.

О каком раскладе мне поведать более подробно?""",
           'scrying_the_future_spread': '''
Это простой трех-карточный расклад. Вариация всем известного "Что было-Есть-Что будет".
Данный расклад позволит тебе увидеть следующую информацию по твоему вопросу:
1. Настоящее: показывает что происходит сейчас.
2. Ближайшее будущее: укажет на то, чего стоит ожидать в ближайшем будущем.
3. Будущее: расскажет о наиболее вероятном исходе по заданному вопросу.''',

           'advice_spread': '''
Расклад используется для того, чтобы изменить результат прочтения карт, а также предложить рекомендации о том, что делать и чего не делать.
Можно использовать как самостоятельный расклад, так и в качестве дополнения к раскладу "Предсказание будущего".
1. Что можно сделать: действие, которое вы можете предпринять, чтобы изменить ситуацию.
2. Чего делать не следует: то, что вы не должны делать, даже если вам кажется, что это хорошая идея.
3. Потенциальный результат: как сложится ситуация в результате выполения и невыполнения вышеперечисленных действий''',

           'five_card_overview_spread': '''
Данный расклад позволит рассматреть ситуацию более пристально, чем расклад "Предсказание будущего" или "Расклад - совет".
Используйте его, чтобы изучить ситуацию и увидеть потенциальные проблемы, найти решения и получить секретную полезную информацию.
1. Ситуация: обзор ситуации, о которой вы спрашиваете.
2. Вызов: вызов, с которым вам предстоит столкнуться.
3. Решение: как можно устранить препятствие.
4. Спрятанная жемчужина: информация, которую вы, скорее всего, не знаете, но которая может оказаться полезной.
5. Результат: вероятный исход, если вы успешно справитесь с задачей.
''',

           'from_heavens_to_hell_spread': '''
Этот расклад, состоящий из девяти карт, представляет собой сложный расклад, раскрывающий подробную информацию, которую вы сможете использовать в некоторые моменты своего жизненного пути.
Расклад будет говорить правду, поэтому, читая расклад, будьте готовы столкнуться как со своими худшими чертами, так и с самыми яркими способностями.
Она также укажет вам путь, по которому вы можете пойти, балансируя между этими тенденциями, ориентируясь в окружающем вас хаотичном мире и создавая свой собственный центр свободы.
1. Ваш Рай: олицетворяет ваши самые высокие идеалы.
2. Алмазные Врата: питает вашу природу и влияет на ваши позитивные склонности.
3. Горящий Ад: олицетворяет ваши самые опасные желания.
4. Адская кузница: питает вашу худшую природу и влияет на ваши негативные cклонности.
5. Санктуарий: олицетворяет ваше лучшее "я", здоровое сочетание света и тьмы.
6.-9. Пандемониум: символизирует битвы, с которыми вы столкнетесь, принимая все части себя и пытаясь найти путь к мастерству и свободе.
'''}

about_arcanas = {
    'Старшие Арканы': '''Карты старших арканов представляют мощные энергии, которые формируют мир.
Иногда эта энергия доступна вам, а иногда карты представляют силы, которые вам неподвластны. Относитесь к ним с благоговением и уважением, подобающим их высокому положению в Таро, и они могут раскрыть свои секреты.''',

    'Младшие Арканы': '''От возвышенных карт Старших Арканов пора спуститься в земную сферу, которая представлена в Младших Арканах.
В то время как нумерованные карты рисуют картины повседневной жизни, любви, успеха и потерь, карты двора обычно представляют других людей, вовлеченных в ситуацию, о которой вы читаете. Поэтому в толкованиях придворных карт персонажи описываются так, как если бы они были кем-то другим, а не вами. Иногда, однако, они будут представлять вас, и вы соответствующим образом скорректируете толкование.''',

    'Мечи': '''Масть Мечей раскрывает ваши представления об истине, разуме и общении. В этих картах вам будет предложено задуматься о том, как вы думаете о мире и как подходите к решению жизненных задач. Люди, представленные мастью Мечей, обладают высоким интеллектом, прекрасно общаются и превыше всего ценят разум.
Карты двора: Паж, Рыцарь, Король, Королева.
Помните, что карты двора обычно обозначают других людей, вовлеченных в ситуацию, о которой вы читаете.
Толкования помогут вам идентифицировать этих людей, понять их характеры и узнать, как реагировать на них, чтобы достичь своих целей.''',

    'Жезлы': '''Масть Жезлов раскроет то, что движет вами, силу вашей решимости, силу ваших страстей и то, как вы выражаете их в мире.
Они также иллюстрируют профессии и начинания, которые наиболее важны для вас. Люди, представленные придворными картами в масти Жезлов, харизматичны, уверены в себе, энергичны и волевы.
Помните, что карты двора обычно обозначают других людей, вовлеченных в ситуацию, о которой вы читаете. Толкования помогут вам определить этих людей, понять их характер и узнать, как реагировать на них, чтобы достичь своих целей.''',

    'Кубки': '''Масть Кубков исследует ваши эмоции, отношения и творческие порывы.
От самой глубокой любви до самых страшных страхов, от самых крепких отношений до еще не сформировавшихся - все это вы найдете в Кубках. Люди, представленные придворными картами в масти Кубков, - чувствительные, творческие, мечтательные, любящие заботу.
Помните, что карты двора обычно обозначают других людей, вовлеченных в ситуацию, о которой вы читаете. Толкования помогут вам идентифицировать этих людей, понять их характеры и найти, как реагировать на них, чтобы достичь своей цели.''',

    'Пентакли': '''Масть Пентаклей выражает ваши представления о физическом мире и имеющихся в вашем распоряжении ресурсах.
Эти карты иллюстрируют рост и падение удачи, результаты упорного труда и дары щедрости. Люди, представленные придворными картами в масти Пентаклей, обладают прекрасным вкусом, они преданны, практичны и трудолюбивы.
Помните, что карты двора обычно обозначают других людей, вовлеченных в ситуацию, о которой вы читаете. Толкования помогут вам идентифицировать этих людей, понять их характеры и найти, как реагировать на них, чтобы достичь своей цели.'''
}

layout_questions = {
    'Предсказание Будущего': {'number': 3,
                              'questions': ["1. Настоящее: показывает что происходит сейчас.",
                                            "2. Ближайшее будущее: укажет на то, чего стоит ожидать в ближайшем будущем.",
                                            "3. Будущее: расскажет о наиболее вероятном исходе по заданному вопросу."]},

    'Расклад - Совет': {'number': 3,
                        'questions': ["1. Что можно сделать: действие, которое вы можете предпринять, чтобы изменить ситуацию.",
                                      "2. Чего делать не следует: то, что вы не должны делать, даже если вам кажется, что это хорошая идея.",
                                      "3. Потенциальный результат: как сложится ситуация в результате выполения и невыполнения вышеперечисленных действий"]},

    'Пятикарточный Расклад': {'number': 5,
                              'questions': ["1. Ситуация: обзор ситуации, о которой вы спрашиваете.",
                                            "2. Вызов: вызов, с которым вам предстоит столкнуться.",
                                            "3. Решение: как можно устранить препятствие.",
                                            "4. Спрятанная жемчужина: информация, которую вы, скорее всего, не знаете, но которая может оказаться полезной.",
                                            "5. Результат: вероятный исход, если вы успешно справитесь с задачей."]},

    'От Рая до Ада': {'number': 9,
                      'questions': ["1. Ваш Рай: олицетворяет ваши самые высокие идеалы.",
                                    "2. Алмазные Врата: питает вашу природу и влияет на ваши позитивные склонности.",
                                    "3. Горящий Ад: олицетворяет ваши самые опасные желания.",
                                    "4. Адская кузница: питает вашу худшую природу и влияет на ваши негативные cклонности.",
                                    "5. Санктуарий: олицетворяет ваше лучшее 'я', здоровое сочетание света и тьмы.",
                                    "6.-9. Пандемониум: символизирует битвы, с которыми вы столкнетесь, принимая все части себя и пытаясь найти путь к мастерству и свободе."]}}
