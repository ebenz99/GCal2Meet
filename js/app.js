function myFunction() {
  window.open("https://www.when2meet.com/?8207981-daEOS");
}

function getElementByXpath(path) {
	return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

var i = 1;
var moreDates = true;
start = '//*[@id="GroupGrid"]/div[3]/div[';

while (moreDates == true){
	try {
		var el = start.concat(i.toString(10),']');
		var date = getElementByXpath(el);
		console.log(date);
		if (date == null){
			moreDates = false;
		}
		i+=1;
	}
	catch {
		moreDates = false;
	}
	if (i > 10){
		break;
	}
}
