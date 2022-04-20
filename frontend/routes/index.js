var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Dylans Shop' });
});

router.get('/login', function(req, res, next){
  res.render('login')
});

router.get('/logout', function(req, res, next){
  res.render('logout')
});

router.get('/register', function(req, res, next){
  res.render('register')
});

router.get('/productindividual', function(req, res, next){
  res.render('productindividual')
});

router.get('/basket', function(req, res, next){
  res.render('basket')
});

router.get('/order-confirmation', function(req, res, next){
  res.render('order-confirmation')
});

router.get('/previous-orders', function(req, res, next){
  res.render('previous-orders')
});


module.exports = router;