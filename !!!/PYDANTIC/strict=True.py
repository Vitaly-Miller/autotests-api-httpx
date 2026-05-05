"""
Pydantic strict=True
Строгое соответствие типов

'Числовая строка' воспринимается как int - это не всегда нужно для валидации:
    * strict=True при инициализации модели (⚠️НЕ УДОБНО)
    * strict=True в схеме (✅)
"""


from pydantic import BaseModel, Field
#====================================== strict=True при инициализации модели (⚠️НЕ УДОБНО) =============================
class Schema(BaseModel):
    a: int
    b: int

int_json = '{"a": 1, "b": 2}'
model_int_str = Schema.model_validate_json(int_json)          # a=1 b=2   <-ok
print(model_int_str)


str_json = '{"a": "1", "b": "2"}'
model_str_str = Schema.model_validate_json(str_json)         # a=1 b=2   <-ЛОГИЧЕСКИ НЕ КОРРЕКТНО
print(model_str_str)


str_json = '{"a": "1", "b": "2"}'
model_str_str = Schema.model_validate_json(str_json, strict=True)    # ValidationError <-ok, но не удобно
print(model_str_str)

#============================================== strict=True в схеме (✅) ===============================================
class SchemaStrict(BaseModel):
    a: int = Field(strict=True)
    b: int = Field(strict=True)

int_json = '{"a": 1, "b": 2}'
model_int_str = SchemaStrict.model_validate_json(int_json)    # a=1 b=2  <-ok
print(model_int_str)


str_json = '{"a": "1", "b": "2"}'
model_str_str = SchemaStrict.model_validate_json(str_json)    # ValidationError  <-ok
print(model_str_str)

#=======================================================================================================================
