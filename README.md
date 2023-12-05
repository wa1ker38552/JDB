# JDB
A nice and simple JSON database class

> Although it's not a very efficient or practical database since it's using JSON, it can be useful for small projects, just a simple database to get you started. I personally use it in a lot of my projects since I'm not expecting a huge influx of incoming data in them and a JSON database is sufficient.

**Getting Started** <br>
Simply just create a new file called `jdb.py` or anything you want and past the code from `jdb.py` into that file. You can now import the database using `from {filename} import Database` where `filename` is the filename that you pasted the code into. <br>
> **Make sure to create a JSON file first where you want the data to be stored and pass that filename into the parameter of the constructor**

**Usage**<br>
```py
from jdb import Database

db = Database('YOUR_DATABASE_FILE_NAME.json')
```

**Functions** <br>
There are 6 functions in the class, `load`, `save`, `get`, `set`, `append`, and `delete`<br>
`load` - Returns the database as a dictionary<br>
`save` - Saves the dictionary to the database<br>
`get` - Gets a key or a list of keys<br>
`set` - Sets a key or a list of keys<br>
`append` - Appends to the value of a key or a list of keys<br>
`delete` - Deletes the value of a key or a list of keys<br>

To use `get`, `set`, `append`, or `delete`, you can pass in keys as a list or just a single one. This may be confusing so let me provide an example:
Provided you have the database below:
```json
{
  "a": "b",
  "c": {
    "d": "e"
  }
}
```
You can call it using the following code
```py
db.get("a")
```
As expected, it'll return the value which the key `a` is at, `'b'`. All it does is run this: `data['a']`. If you wanted to get the value `'e'`, you would normally do this: `data['c']['d']`. With the database class, the equivalent would be:
```py
db.get(['c', 'd'])
```
Instead of calling a key on a previous key, you can just past in the keys you want as a list making it much simpler. The function uses an `eval` statement to write this more concisely. 
