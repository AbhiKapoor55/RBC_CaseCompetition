

function launchDivi(e){
	console.log("STARTING.FOR REAL..")
	const url = "/launchDivi"

	fetch(url).then((response) => {
		console.log(response)
		if(response.status === 200){
			//console.log("received response")
		} else {
			console.log("Error Occurred: Response code was not 200")
		}
	})
}

function sendMessage(e){
	var message = document.getElementsByClassName("enterMessage")[0].value;
	//console.log("SENDING MESSAGE: " + message + "...")

	const url = "/message"
	addUserMessageToDOM()
	fetch(url).then((response) => {
		//console.log(response)
		if(response.status === 200){
			//console.log("received message from server")
		} else {
			console.log("Error Occurred: Response Code was not 200 ", response.status)
		}
		return response.json()
	}).then((res) => {
	    //console.log(res)
	    wait(3000)
	    addServerMessageToDOM(res)
	}).catch((err) => {
	  console.log("There was an error, ", err)
	})
}

function wait(ms){
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}

function addUserMessageToDOM(e){

	const textEntered = document.getElementsByClassName("enterMessage")[0].value; 
	//console.log("textentere is " + textEntered)

	const newDiv = document.createElement("div")
	newDiv.className = "container"
	//const img = document.createElement("img")
	const p = document.createElement("p")
	p.appendChild(document.createTextNode(textEntered))

	const img = document.createElement("img")
	img.src="images/icon.jpg"
	img.alt = "Avatar"

	var today = new Date();
	var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

	const span = document.createElement("span")
	span.className = "time-right"
	span.appendChild(document.createTextNode(time))
	newDiv.appendChild(span)
	newDiv.appendChild(img)
	newDiv.appendChild(p)

	document.body.appendChild(newDiv)
}

function addServerMessageToDOM(e){
	const newDiv = document.createElement("div")
	newDiv.className = "container darker"
	//const img = document.createElement("img")
	const p = document.createElement("p")
	p.appendChild(document.createTextNode(e))

	const img = document.createElement("img")
	img.src="images/diviIcon.png"
	img.alt = "Avatar"

	var today = new Date();
	var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

	const span = document.createElement("span")
	span.className = "time-right"
	span.appendChild(document.createTextNode(time))
	newDiv.appendChild(span)
	newDiv.appendChild(img)
	newDiv.appendChild(p)

	document.body.appendChild(newDiv)
}

function deleteAllMessages(e){
	const messageContainer = document.getElementsByClassName("container")
	const parentElement = messageContainer[0].parentElement 

	for(let i = 0;i<messageContainer.length;i++){
		parentElement.removeChild(messageContainer[i])
	}

	const messageContainer2 = document.getElementsByClassName("container darker")
	const parentElement2 = messageContainer2[0].parentElement 

	for(let i = 0;i<messageContainer2.length;i++){
		parentElement2.removeChild(messageContainer2[i])
	}
}

