import pandera as pa
from pandera.typing import DataFrame
from pandera.typing import Series


class MyModel(pa.DataFrameModel):
    field1: Series[int] = pa.Field(coerce=True)
    field2: Series[str] = pa.Field(coerce=True)


def process_data(data: DataFrame[MyModel]):
    print(data.field1)
    print(data.field2)
