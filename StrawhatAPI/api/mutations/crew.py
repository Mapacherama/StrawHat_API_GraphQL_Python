from api import db
from api.models import crew
from api.extra_features.creation import create_result
from ariadne import convert_kwargs_to_snake_case
@convert_kwargs_to_snake_case
def create_crew_resolver(obj, _info, **kwargs):

    Crew = crew(**kwargs)
    db.session.add(Crew)
    db.session.commit()

    return create_result(Crew)

@convert_kwargs_to_snake_case
def update_crew_resolver(obj, _info, **kwargs):
    Crew = crew.query.get(kwargs["id"])
    if not Crew:
        return create_result(status=False, errors=[Errors.OBJECT_NOT_FOUND])
    db.session.update(**kwargs)
    db.session.commit()

    return create_result(crew = Crew)

#Origin

@convert_kwargs_to_snake_case
def delete_crew_resolver(obj, info, **kwargs):
    crew = Crew.query.get(kwargs["id"])
    db.session.delete(crew)
    db.session.commit()

    return create_result()