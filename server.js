var sqlite = require("sqlite3");
var express = require("express");
var bodyParser = require("body-parser");
var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use(function(req, res, next) { // request, response, next
   res.header("Access-Control-Allow-Origin", "*");
   res.header("Access-Control-Allow-Methods", "GET, PUT, POST, DELETE");
   res.header("Access-Control-Allow-Headers", "Content-Type, cache-control");
   return next();
});

var port = process.env.PORT || 8080; // set our port
var router = express.Router(); // get an instance of the express Router

// middleware to use for all requests ------------------------------------------
router.use(function(req, res, next) {
   // do logging
   console.log("Server in use");
   next(); // make sure we go to the next routes and don't stop here
});

// this is an alias, so people don’t know the real file-path of your application
app.use('/static', express.static(__dirname + '/app/webpage/'));
//they can ask for `static/critical.js` and get `app/important/critical.js`, but
//a hacker wouldn’t know the file path to actually get the file if they got mischievous

router.route("/something/arbitrary/")
    .get(function(req, res) { // GET requests respond with Hello World
        // res.send(err.message);
        res.json("{message: 'Hello World!'}");     // Turns structures into a string
            // JavaScript Object Notation
            // Can be parsed out by more than JavaScript (Python, etc)
});

// -----------------------------------------------------------------------------
//add-on to the IP address and port #, for minor security and/or personal flair
app.use("/api", router);

//Tell the application to listen on the port # you specified above
app.listen(port);
console.log("Express server listening on port %d in %s mode. ", port, app.settings.env)
