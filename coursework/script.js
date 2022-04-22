
var planes_prices = new Array();
planes_prices["!---select---!"]=0;
planes_prices["London - Glasgow"]=20;
planes_prices["Manchester - Bristol"]=30;
planes_prices["Bristol - London"]=15;
planes_prices["Glasgow - Cardiff"]=35;
planes_prices["Bristol - Manchester"]=20;
planes_prices["Glasgow - London"]=30;
planes_prices["London - Bristol"]=15;
planes_prices["Cardiff - Glasgow"]=35;

function getPlanePrice()
{
    var planeprice=0;
    var theForm = document.forms["planeform"];
    var selectedPlane = theForm.elements["planes"];
    planeprice = planes_prices[selectedPlane.value];
    return planeprice;
}


var adult_nos = new Array();
adult_nos["0"]=0;
adult_nos["1"]=1;
adult_nos["2"]=2;
adult_nos["3"]=3;
adult_nos["4"]=4;
adult_nos["5"]=5;

function getAdults()
{
    var Adults=0;
    var theForm = document.forms["planeform"];
    var selectedAdults = theForm.element["adults"];
    Adults = adult_nos[selectedAdults.value];

    var aprice = 0;
    aprice = Adults * getPlanePrice();
    return aprice;
    
}

/*var child_nos = new Array();
child_nos["0"]=0;
child_nos["1"]=1;
child_nos["2"]=2;
child_nos["3"]=3;
child_nos["4"]=4;
child_nos["5"]=5;
*/
function getChildren ()
{
    var nos = 0;
    var theForm = document.forms["planeform"];
    var selectedChildren = theForm.elements["children"];
    if(children.value!="")
    {
        nos = parseInt(children.value)
    }

    var cprice = 0;
    var x = 50/100 * nos;
    cprice =  x * getPlanePrice();
    return cprice;
}

function calculateTotal()
{
    var planeprice = getChildren() + getAdults();
    document.getElementById('totalPrice').innerHTML = "Total Travel Cost £"+planeprice; 
}