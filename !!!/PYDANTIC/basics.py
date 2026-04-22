"""
Pydantic Basics
"""
from pydantic import BaseModel

#=======================================================================================================================
#-------------------------------------------------- Pydantic Schema-----------------------------------------------------
class DataSchema(BaseModel):
    id: str
    title: str


#=========================================== MODEL INITIALIZATION & VALIDATION =========================================
data_model = DataSchema(
    id='course_id',
    title='API'
)

#--------------------------------------------------  API Objects -------------------------------------------------------
# Dict
data_dict = {
    'id': 'course_id',
    'title': 'API',
}
#--------------------------------------------------
# JSON-string
data_json = """
{
    "id": "course_id",
    "title": "API"
}
"""


#--------------------------------------------- DESERIALIZATION (validate ⬅︎) -------------------------------------------
# Dict -> Model                ┌──────┐
data_model_dict = DataSchema.model_validate(data_dict)         # id='course_id' title='API'
# JSON -> Model                ┌──────┬──────┐
data_model_json = DataSchema.model_validate_json(data_json)    # id='course_id' title='API'


#------------------------------------------------ SERIALIZATION (dump ⮕) ----------------------------------------------
# model_dump()            —> Python Dict           (могут быть UUID, datetime и т.д.)
# model_dump(mode='json') —> JSON-совместимый dict (для API payload)
# model_dump_json()       —> JSON строка           (raw body)
#-----------------------------------------------------------------------------------------------------------------------

# Model -> Python Dict             ┌─────┐
data_model_dump_dict = data_model.model_dump()                 # {'id': 'course_id', 'title': 'API'}

# Model -> JSON-совместимый Dict✨         ┌─────┐╴╴╴╴╴┐
data_model_dump_json_dict = data_model.model_dump(mode='json') # {'id': 'course_id', 'title': 'API'}

# Model -> JSON-string             ┌─────┬─────┐
data_model_dump_json = data_model.model_dump_json()            # {"id":"course_id","title":"API"}


#------------------------------------------------------ Output ---------------------------------------------------------
print(data_model)
print(data_model_dict)
print(data_model_json)
print(data_model_dump_dict)
print(data_model_dump_json_dict)
print(data_model_dump_json)
