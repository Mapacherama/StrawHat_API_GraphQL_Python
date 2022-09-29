from .models import OnePieceCharacter
from ariadne import convert_kwargs_to_snake_case


def listOnePieceCharacters_resolver(obj, info):
    try:
        onePieceCharacters = [
            character for character in OnePieceCharacter.query.all()
        ]
        print(onePieceCharacters)
        payload = {"success": True, "onepiececharacters": onePieceCharacters}
    except Exception as error:
        payload = {"success": False, "errors": [str(error)]}
    return payload


@convert_kwargs_to_snake_case
def getSingleCharacter_resolver(obj, info, id):
    try:
        character = OnePieceCharacter.query.get(id)
        print(character)
        payload = {"success": True, "character": character}
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["Character item matching {id} not found"]
        }
    return payload
