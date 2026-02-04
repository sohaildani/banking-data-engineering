def check_nulls(df, columns):
for col in columns:
null_count = df.filter(df[col].isNull()).count()
if null_count > 0:
raise ValueError(f"Column {col} has {null_count} null values")