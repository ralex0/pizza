# pizza
Simulation of a pizza shop interface. For fun/demonstation purposes.

I want this package to be able to do a few things:
1) Build menu of options from a stored file. Introduce a class "pizza"
2) Display an menu of options from the command line. Should be as user frendly as possible providing descriptions, prices etc.
3) Build "orders" which I suppose are just collections of pizzas. Classes & Inheritance will come in handy here.
4) The fun part: Make suggestions on what to order based predictions from doing bayesian inference on stored data on previous orders. This could include challenges like 
* determining what toppings seem to go well together based on order history
* predicting what a person is likely to order based on both their history, and any proposed correlation with the history of others
* anything else interesting!

If I (we?) ever finish this it'd be interesting to see how it would perform on real data. I think for now the implementation has to proceed roughly in order as I have outlined it, except for the user interface part.
