from data_types import SearchMode, Language
from tesslang import standardize


def determine_mode(query_obj):
    user_res = (input("Would you like to search for an acrostic (a) or telestich (t)?\n> ")
                .strip().lower())
    if user_res == 'a' or user_res == 'acrostic':
        query_obj['mode']: SearchMode = 'ACROSTIC'
    elif user_res == 't' or user_res == 'telestich':
        query_obj['mode']: SearchMode = 'TELESTICH'
    else:
        print("Invalid choice. Please try again.\n")
        determine_mode(query_obj)
        return
    print("mode:", query_obj['mode'])


def determine_lang(query_obj):
    user_res = (input("Would you like to search within Latin (la), Greek (grc), or English (en) texts?\n> ")
                .strip().lower())
    if user_res == 'la' or user_res == 'latin':
        query_obj['lang']: Language = 'la'
    elif user_res == 'grc' or user_res == 'greek':
        query_obj['lang']: Language = 'grc'
    elif user_res == 'en' or user_res == 'english':
        query_obj['lang']: Language = 'en'
    else:
        print("Invalid choice. Please try again.\n")
        determine_lang(query_obj)
        return
    print("lang:", query_obj['lang'])


def determine_term(query_obj):
    user_res = (input("What sequence of letters are you looking for?\n> ")
                .strip().lower())
    query_obj['term'] : str = standardize(query_obj['lang'], user_res)
    if len(query_obj['term']) < 2:
        print("Sequence must be at least 2 characters long.\n")
        determine_term(query_obj)
        return
    print("term:", query_obj['term'])

def determine_buflen(query_obj):
    user_res = (input("How many lines should be printed before and after each match (default 0)?\n> ")
                .strip())
    try:
        if user_res == '':
            user_res = '0'
        query_obj['buflen'] : int = int(user_res)
        print(query_obj['buflen'])
        return query_obj
    except ValueError:
        print("Invalid choice. Please try again.\n")
        determine_buflen(query_obj)


def get_human_readable_lang(query_obj):
    lang = query_obj['lang']
    if lang == 'la':
        return 'Latin'
    if lang == 'grc':
        return 'Greek'
    if lang == 'en':
        return 'English'


def determine_searchspace(query_obj):
    user_res = (input("Would you like to search all " + get_human_readable_lang(query_obj) + " texts?\n> ")
                .strip().lower())
    if user_res[:1] == 'y':
        query_obj['pathname']: str = '../texts/' + query_obj['lang']
    else:
        example = 'ovid.ars_amatoria'
        if query_obj['lang'] == 'grc':
            example = 'homer.odyssey'
        elif query_obj['lang'] == 'en':
            example = 'milton.paradise_lost'
        user_res = (input(f"Which work would you like to search? (ex. {example})\n> ")
                    .strip().lower())
        query_obj['pathname']: str = '../texts/' + query_obj['lang'] + '/' + user_res


def build_query():
    query_obj = {}

    determine_mode(query_obj)
    determine_lang(query_obj)
    determine_term(query_obj)
    determine_buflen(query_obj)
    determine_searchspace(query_obj)

    return query_obj