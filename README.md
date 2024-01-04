# Tableau-Dynamic-User-Filter
Create a large dynamic user filter using boolean values, that filters the data at row level

User filtering is based on the following principle:

x = User Email
Y = Filter Value

IF USERNAME() = x THEN Y = [Tableau Row Field]
ELIF USERNAME() = x THEN Y = [Tableau Row Field]
ELSE FALSE
END
