

function launchDivi(e){
	console.log("STARTING.FOR REAL..")
	const url = "/launchDivi"

	fetch(url).then((response) => {
		console.log(response)
		if(response.status === 200){
			console.log("received response")
		} else {
			console.log("Error Occurred: Response code was not 200")
		}
	})
}

function sendMessage(e){
	var message = document.getElementsByClassName("enterMessage")[0].value;
	console.log("SENDING MESSAGE: " + message + "...")

	const url = "/message"

	fetch(url).then((response) => {
		console.log(response)
		if(response.status === 200){
			console.log("received message from server")
		} else {
			console.log("Error Occurred: Response Code was not 200")
		}
	})
}

