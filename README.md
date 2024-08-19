# TarotDiabloBot

This Telegram Bot (@tarot_diablo_bot) is created to practise aiogram3 skills.
Based on Tarot Diablo by Blizzard: https://uk.gear.blizzard.com/products/diabgp0003-diablo-the-sanctuary-tarot-deck-and-guidebook.
All the cards' interpretations were taken from the GuideBook by Blizzard.

To implement layout mode - random.choices was used.
Also, Upright and Reversed positions for Tarot cards were implemented.

### Requirements
Python 3.12 with all the [requirements.txt](https://github.com/Anastasiia-Pov/TarotDiabloBot/blob/main/requirements.txt) dependencies installed.

### Project structure:
```
TarotDiabloBot/
├─ app/
│  ├─ handlers.py
│  ├─ keyboards.py
│  ├─ messages.py
│  ├─ performing_layout.py
├─ tarot_cards/
│  ├─ arcanas.py
│  ├─ arcanas_interpretation.py
├─ cards_layouts/
├─ comands.txt
├─ main.py
```

- ```main.py``` - entry point
- ```app``` - contains all the neccessary files to run the bot correctly
- ```tarot_cards``` - contains all the messages that are needed to be printed by the bot

User has an option of 5 layouts: Card of the Day, Scrying the Future Spread, Advice Spread, Five Card Overview Spread, From Heavens to Hell Spread.

### Commands
- ```new_layout``` - новый расклад - to start a new layout;
- ```help``` - помощь - ask for help;
- ```how_to_use``` - как пользоваться - tells a user how to use a bot;
- ```about_layouts``` - о раскладах - tells a user about available layouts;
- ```about_arcanas``` - хочу знать больше об арканах - provides a user with more information about Major and Minor Arcanas and suit cards;
- ```interpretation``` - интерпретация отдельной карты - bot provides an opportunity to learn more about interpretationa of each card separately.