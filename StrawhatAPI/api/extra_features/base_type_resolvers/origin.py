from api.models import Origin

def resolve_origin_id(origin_obj: Origin, _info):
    return origin_obj.id
def resolve_origin_character_id(origin_obj: Origin, _info):
    return origin_obj.character_id
def resolve_origin_name(origin_obj: Origin, _info):
    return origin_obj.name

def resolve_origin_haskingdom(origin_obj: Origin, _info)-> bool:
    return origin_obj.hasKingdom







