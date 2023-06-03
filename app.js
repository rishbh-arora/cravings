const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");

const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

app.get("/", function (req, res) {
    res.render("home-page");
});
app.get("/menu",function(req,res){
    res.render("menu");
});
app.get("/messmenu",function(req,res){
    res.render("mess-menu");
});
app.get("/profile",function(req,res){
    res.render("profile");
});

app.listen(3000, () => console.log(`Application is listening on port 3000!`));