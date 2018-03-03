db.run("CREATE TABLE IF NOT EXISTS groceries(" +
    "id INTEGER PRIMARY KEY AUTOINCREMENT," +
    "name varchar(50) NOT NULL," +
    "price varchar(50) NOT NULL," +
    "type varchar(50) NOT NULL);",
    function(err) {
        if (err)
            throw err;
        console.log("Created groceries list if it didn't exist already")
    });

var query = "INSERT INTO groceries(name, price) VALUES (\"Ian\", \"$20.45\");"

/*
setTimeout(function() {
    db.all("SELECT * FROM groceries WHERE type = ?;", "Bean", function(err, users) {
        if (err)
            throw err;

        console.log(users)
    });
}, 200);
*/

