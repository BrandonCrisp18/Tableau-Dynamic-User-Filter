# Tableau-Dynamic-User-Filter
Create a large dynamic user filter using boolean values, that filters the data at row level

#### User filtering is based on the following principle:<br><br>

x = User Email<br>
Y = Filter Value<br><br>

IF USERNAME() = x THEN Y = [Tableau Row Field]<br>
ELIF USERNAME() = x THEN Y = [Tableau Row Field]<br>
ELSE FALSE<br>
END<br>

#### There is a master file that contains both email and value you to filter on
#### <br>The Python script generates the filter code for all the users in the maser file
