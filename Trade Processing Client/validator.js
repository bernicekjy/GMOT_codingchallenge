//jshint esversion:6

const express=require("express");
const bodyParser=require("body-parser");

const app=express();
app.use(bodyParser.urlencoded({extended:true})); //extended:true allows nesting, REQUIRED to declare when using bodyParser

const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('/Users/bern/Documents/GitHub/GMOT_codingchallenge/Database/client.sql');


app.get("/",function(req,res){
    res.sendFile(__dirname+"/clientrequest.html");
});

app.post("/",function(req,res){
    var clientID = Number(req.body.clientID);

    db.serialize(() => {
        const stmt = db.prepare('SELECT * FROM users WHERE clientID=?');
        stmt.all(clientID, (err, rows) => {
          if (err) {
            console.error(err.message);
          }
          console.log(rows);
        });
        stmt.finalize();
      });
      
});

app.listen(3000,function(){
    console.log("Server started on port 3000.")
});